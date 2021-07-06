import re

from django import forms
from django.conf import settings

from core.backends import EmailModelBackend
from core.models import BaseUserProfile


class LoginForm(forms.Form):
    """
    Login form view for validating user login. Throw validation
    as handled below
    """

    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not (email or password):
            msg = "Email and password are required"
            self._errors["password"] = self.error_class(["Password is required"])
            self._errors["email"] = self.error_class(["Email is required."])
            return self.cleaned_data

        if not password:
            msg = "Password is required"
            self._errors["password"] = self.error_class([msg])
            return self.cleaned_data

        if not email:
            msg = "Email is required"
            self._errors["email"] = self.error_class([msg])
            return self.cleaned_data

        user_auth = EmailModelBackend()
        user = user_auth.authenticate(username=email, password=password)

        if user is None:
            msg = "Email or password is incorrect"
            self._errors["password"] = self.error_class([msg])
            return self.cleaned_data

        if not user.is_active:
            msg = "Your account is not activated"
            self._errors["password"] = self.error_class([msg])
            return self.cleaned_data

        return self.cleaned_data


class SignUpForm(forms.ModelForm):
    """
    SignUpForm for user sign up, it will handle validation as given below
    """

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="password",
        max_length=50,
        error_messages={"required": "Please enter your password."},
    )
    email = forms.CharField(
        label="email", error_messages={"required": "Please enter your email."}
    )
    first_name = forms.CharField(
        label="first_name",
        error_messages={"required": "Please enter your first name."}
    )
    last_name = forms.CharField(
        label="last_name",
        error_messages={"required": "Please enter your last name."}
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="confirm_password",
        max_length=50,
        error_messages={"required": "Please enter confirm password."},
    )

    class Meta:
        model = BaseUserProfile
        fields = ("password", "email", "first_name", "last_name", "confirm_password")

    def save(self):
        base_user = super(SignUpForm, self).save(commit=False)
        base_user.set_password(self.cleaned_data["password"])
        base_user.username = self.cleaned_data["email"]
        base_user.email = self.cleaned_data["email"]
        base_user.first_name = self.cleaned_data["first_name"]
        base_user.last_name = self.cleaned_data["last_name"]
        base_user.is_active = True
        base_user.save()
        return self.cleaned_data

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = cleaned_data.get("email")
        confirm_password = cleaned_data.get("confirm_password")
        password = cleaned_data.get("password")
        user = BaseUserProfile.objects.filter(email__iexact=email)

        if user:
            msg = "User with the same email already exists!"
            self._errors["email"] = self.error_class([msg])
            return self.cleaned_data

        if password != confirm_password:
            msg = "Both passwords do not match"
            self._errors["password"] = self.error_class([msg])
