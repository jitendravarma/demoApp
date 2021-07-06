from django.conf.urls import url

from .views import TextAPIView, UpdateProfileAPIView, UploadJson

app_name = "v1"
urlpatterns = [
    url(r'^user/$', UpdateProfileAPIView.as_view(), name="user-api"),
    url(r'^upload/$', UploadJson.as_view(), name="json-api"),
    url(r'^text/$', TextAPIView.as_view(), name="text-api"),
]
