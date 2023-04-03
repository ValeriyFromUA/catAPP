from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from ..forms import ConfirmationForm
from ..models import Confirmations


class ConfirmView(View):
    template_name = 'confirmation.html'

    def get(self, request):
        form = ConfirmationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
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
        return render(request, self.template_name, {'form': form})
