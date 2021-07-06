import json

from core.backends import EmailModelBackend
from core.forms import LoginForm, SignUpForm
from core.mixins import BaseMixin, CustomTemplateView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView, RedirectView

# Create your views here.


class LoginView(BaseMixin, FormView):
    """
    This view handles authentication of the user, when they first time logs in
    redirects them to login page if not authenticated.
    """
    form_class = LoginForm
    template_name = 'frontend/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        if not form.is_valid():
            return render(
                request,
                self.template_name,
                {
                    'form': form, "csrf_token": form.data['csrfmiddlewaretoken'],
                    'email': email
                }
            )
        user_auth = EmailModelBackend()
        user = user_auth.authenticate(username=email, password=password)

        if user:
            login(self.request, user)
            if "next" in self.request.GET:
                url = self.request.GET["next"]
                response = HttpResponseRedirect(url)
                return response
            else:
                response = HttpResponseRedirect('/home')
                return response
        else:
            logout(self.request)
            form._errors["password"] = ["User doesn't exists."]
            return render(
                request,
                self.template_name,
                {
                    'form': form, 'email': email,
                    "csrf_token": form.data['csrfmiddlewaretoken']
                }
            )


class SignupView(BaseMixin, FormView):
    """
    This view signs up new user and validates the form on the server side
    """

    form_class = SignUpForm
    template_name = 'frontend/sign-up.html'

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        email = form.data['email']
        if not form.is_valid():
            context = {
                'form': form, "csrf_token": form.data['csrfmiddlewaretoken'],
                'email': email
            }
            return render(
                request, context=context, template_name=self.template_name)
        else:
            form.save()
            return HttpResponseRedirect(reverse('index-view'))


class LogOutView(RedirectView):
    """
    logout view
    """

    def get_redirect_url(self):
        url = reverse("login-view")
        logout(self.request)
        return url


class IndexView(LoginRequiredMixin, CustomTemplateView):
    """
    Home view for user after redirection
    """
    template_name = 'frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['dashboard_page'] = "active"
        return context


class ProfileView(LoginRequiredMixin, CustomTemplateView):
    """
    Profile page for user to update first name, last name, profile pic
    """
    template_name = 'frontend/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile_page'] = "active"
        return context


class UsersView(LoginRequiredMixin, CustomTemplateView):
    """
    This view will render list of uploaded users
    """
    template_name = 'frontend/users.html'

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['profile_page'] = "active"
        return context


class UploadView(LoginRequiredMixin, CustomTemplateView):
    """
    This view is to render upload page for json
    """
    template_name = 'frontend/upload.html'

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context['profile_page'] = "active"
        return context
