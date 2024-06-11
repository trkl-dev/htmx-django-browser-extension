from django.urls import path

from . import views

urlpatterns = [
    path("", views.ExtensionView.as_view(), name="extension"),
]
