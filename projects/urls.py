from django.urls import path

from projects import views


urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.ProjectListView.as_view()),
    path("/<int:project_id>", views.ProjectListView.as_view()),
]
