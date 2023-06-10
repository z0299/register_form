from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path("", views.IndexView.as_view(), name="register"),
    path("submitted/", views.submitted, name="submitted"),
    path("registered/", views.RegisteredView.as_view(), name="registered")
]