import json
import time

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .exceptions import handle_exception
from .service import ProjectService
from .models import Project


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "projects/index.html",)

class ProjectListView(View):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.project_service = ProjectService()
        self.project_model = Project()

    @handle_exception
    def get(self, request: HttpRequest) -> JsonResponse:
        user_id = request.user.id
        projects = self.project_service.get_project_list(user_id)
        # return JsonResponse(projects, status=200)
        return render(request, "projects/index.html", {"projects": projects})
        

    @handle_exception
    def patch(self, request: HttpRequest, project_id: int) -> JsonResponse:
        user_id = request.user.id
        data = json.loads(request.body)
        state = data["state"]
        self.project_service.update_state(project_id, user_id, state)

        return JsonResponse({"message": "Updated"}, status=201)
