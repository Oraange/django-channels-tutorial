import json
import time

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .exceptions import handle_exception, ProjectNotFound
from .service import StateUpdate
from .models import Project


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "projects/index.html")

class ProjectListView(View):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.state_service = StateUpdate()
        self.project_model = Project()

    # @handle_exception
    def post(self, request: HttpRequest) -> JsonResponse:
        user_id = request.user.id
        if not user_id:
            return JsonResponse({"message": "No Session"}, status=401)

        data = json.loads(request.body)
        state = data["state"]
        project = self.project_model.get_by_user(user_id)

        if not project:
            raise ProjectNotFound

        self.state_service.update_state(project.id, state)

        return JsonResponse({"message": "Updated"}, status=201)
