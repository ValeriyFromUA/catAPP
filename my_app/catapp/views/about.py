from django.views import View
from django.shortcuts import render


class AboutView(View):

    @staticmethod
    def get(request):
        return render(request, 'about.html')
