from PIL import Image
from django.forms import formset_factory
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from ..forms import PostsForm, ImagesForm, TagsForm
from ..models import Images, PostTags


class NewPostView(View):
    PostTagset = formset_factory(TagsForm, extra=3)
    tagset = PostTagset()

    def get(self, request):
        return render(request, 'new_post.html', {'formset': self.tagset})

    def post(self, request):
        tagset = self.PostTagset(request.POST)
        post_form = PostsForm(request.POST)
        images_form = ImagesForm(request.POST, request.FILES)

        if not post_form.is_valid():
            messages.error(request, 'Invalid post_form')
        if not images_form.is_valid():
            messages.error(request, 'Invalid images_form')

        post = post_form.save(commit=False)
        post.user_id = request.user
        post.save()

        if tagset.is_valid():
            for tag_form in tagset:
                data = tag_form.cleaned_data
                tag = PostTags(post=post, tag=data.get('tag'))
                tag.save()

        for image in request.FILES.getlist('image'):
            image = Images(post_id=post, image=image)
            image.save()

        first_image = Images.objects.filter(post_id=post.id).first()

        if first_image:
            post.preview_image = first_image.image
            img = Image.open(post.preview_image.path)
            img.thumbnail((300, 300))
            img.save(post.preview_image.path)
            post.save()

        return redirect(reverse('profile', args=[request.user.id]))
