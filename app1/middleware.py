from django.shortcuts import redirect

class RedirectIfLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path == '/login/' or request.path == '/':
                return redirect('home')  

        response = self.get_response(request)
        return response
