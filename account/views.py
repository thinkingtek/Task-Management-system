from .tokens import account_activation_token
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegForm, UserLoginForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from .decorators import *
from django.contrib.auth.views import LoginView

User = get_user_model()


@redirect_authenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Activate your Account"
            message = render_to_string('account/email_activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            send_email = EmailMessage(subject, message, to=[email])
            send_email.send()
            return render(request, 'account/email_sent.html')
    else:
        form = UserRegForm()

    context = {
        'title': 'Create Account',
        'form': form
    }
    return render(request, 'account/register.html', context)


# activate account registration
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, f'Account successfully activated {user.full_name} you can now login')
        return redirect('login')
    else:
        return HttpResponse('registered succesfully and activation sent')


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def form_invalid(self, form):
        return super(UserLoginView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Login | eLiteProps"
        return context


@redirect_unauthenticated_user
def userLogout(request):
    messages.info(
        request, f"{request.user.username} You have successfully logged out")
    logout(request)
    return redirect("login")
