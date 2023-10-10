from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the URL path pattern to check

        if request.path.startswith('/dashboard'):
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                # Perform authentication logic
                user = authenticate(request)
                if user:
                    # Authenticate the user
                    login(request, user)
                else:
                    # Redirect to a login page or any other path
                    return HttpResponseRedirect('/')

        response = self.get_response(request)
        return response