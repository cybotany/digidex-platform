from digidex.accounts.models import Activity


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            Activity.objects.update_or_create(user=request.user)
        return response
