from django.shortcuts import redirect
from django.contrib import messages


def redirect_authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(
                request, "You can't access the sign-In page while logged-in")
            return redirect('task:index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def redirect_unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(
                request, "You've not logged-In'")
            return redirect('task:index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
