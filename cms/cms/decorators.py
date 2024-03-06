from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from functools import wraps


def group_required(*group_names):
    """
    Requires user membership in at least one of the groups passed in.
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return _wrapped_view
    return decorator


def require_authenticated(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def require_ajax(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.is_ajax():
            return JsonResponse({"error": "Not an AJAX request"}, status=400)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
