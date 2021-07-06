from django.conf.urls import url
from django.contrib.auth import logout

from .views import (IndexView, LoginView, LogOutView, ProfileView, SignupView,
                    UploadView, UsersView)

urlpatterns = [
    # for user authentication
    url(r'^login/$', LoginView.as_view(), name="login-view"),
    url(r'^signup/$', SignupView.as_view(), name="signup-view"),
    url(r'^logout/$', LogOutView.as_view(), name="logout-view"),

    # dashboard views
    url(r'^home/$', IndexView.as_view(), name="home-view"),
    url(r'^profile/$', ProfileView.as_view(), name="profile-view"),
    url(r'^users/$', UsersView.as_view(), name="users-view"),
    url(r'^upload/$', UploadView.as_view(), name="upload-view"),
]
