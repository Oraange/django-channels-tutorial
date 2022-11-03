from django.urls import path

from projects import views


urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.my_test, name="my_test"),
]
