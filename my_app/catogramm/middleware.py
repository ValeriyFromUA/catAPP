from django.shortcuts import redirect

ALLOWED_URLS = ['/confirm/', '/login/', '/logout/', '/home/']


class ConfirmUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if not request.user.is_confirmed:
                if request.path not in ALLOWED_URLS:
                    return redirect('/confirm/')
        response = self.get_response(request)
        return response
