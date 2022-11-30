from django.db.models import QuerySet

from .serializers import ProjectSerializer
from .models import Project


class ProjectService:
    def __init__(self) -> None:
        self._model = Project()

    def get_project_list(self, user_id: int) -> QuerySet[Project]:
        return self._model.get_by_user(user_id=user_id)
        # return ProjectSerializer(projects, many=True)

    def update_state(self, project_id: int, user_id: int, state: int) -> None:
        self._model.patch_state(project_id=project_id, user_id=user_id, state=state)
