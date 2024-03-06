from django.http import JsonResponse
from functools import wraps

def require_ajax(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({"error": "Not an AJAX request"}, status=400)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
