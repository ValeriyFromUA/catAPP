from random import randrange
from PIL import Image
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from cofirmation import send_confirmation_email
from .forms import NewUserForm, UserForm, ConfirmationForm, PostsForm, ImagesForm, TagsForm
from .models import User, Confirmations, Posts, Likes, Images, PostTags


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Username OR password does not exit')
        login(request, user)
        return redirect(reverse('profile', args=[user.id]))

    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))


def register_page(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            key = randrange(10000, 99999)
            confirmation = Confirmations(user_id=user, confirmation_key=key)
            confirmation.save()
            send_confirmation_email(user.email, key)
            return redirect('confirm')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'register.html', {'form': form})


@login_required
def confirm(request):
    if request.method == 'POST':
        form = ConfirmationForm(request.POST)
        if form.is_valid():
            confirmation_key = form.cleaned_data['confirmation_key']
            confirmation = Confirmations.objects.filter(confirmation_key=confirmation_key).first()
            if confirmation is not None:
                user = confirmation.user_id
                user.is_confirmed = True
                user.save()
                confirmation.delete()
                return redirect(reverse('edit_profile', args=[user.id]))
            else:
                form.add_error('confirmation_key', 'invalid code')
    else:
        form = ConfirmationForm()
    return render(request, 'confirmation.html', {'form': form})


@login_required
def edit_profile(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.bio = form.cleaned_data['bio']
            if form.cleaned_data['avatar']:
                user.avatar = form.cleaned_data['avatar']
            user.save()
            return redirect(reverse('profile', args=[pk]))
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def user_profile(request, pk):
    user = User.objects.get(id=pk)
    posts = Posts.objects.filter(user_id=pk)
    images = Images.objects.filter(post_id__user_id=pk).select_related('post_id__user_id').first
    context = {'user': user, 'posts': posts, 'images': images}
    return render(request, 'profile.html', context)


@login_required
def new_post(request):
    PostTagset = formset_factory(TagsForm, extra=3)
    tagset = PostTagset()
    if request.method == 'POST':
        tagset = PostTagset(request.POST)
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
                print(data.get('tag'))
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
    return render(request, 'new_post.html', {'formset': tagset})


def post_details(request, pk):
    post = Posts.objects.get(id=pk)
    images = Images.objects.filter(post_id=pk).all()
    tags = PostTags.objects.filter(post_id=pk).all()
    context = {'post': post, 'images': images, 'tags': tags}

    return render(request, 'post.html', context)
