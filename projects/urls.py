from django.urls import path

from projects import views


urlpatterns = [
    path("", views.index, name="index"),
    path("/test", views.ProjectListView.as_view()),
]
