from .models import Project


class StateUpdate:
    def __init__(self) -> None:
        self._model = Project()

    def update_state(self, project_id: int, state: int):
        self._model.patch_state(project_id=project_id, state=state)
