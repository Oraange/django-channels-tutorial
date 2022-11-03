from django.db import models

from core.models import TimeStamp


class ProjectManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).using("alertdb")

class Project(TimeStamp):
    state = models.PositiveSmallIntegerField()

    objects = ProjectManager()

    class Meta:
        db_table = 'project'

    @classmethod
    def patch_state(cls, project_id: int, state: int) -> None:
        project: Project = cls.objects.get(id=project_id)
        project.state = state
        project.save(using="alertdb")

    @classmethod
    def create_project(cls, state: int) -> None:
        project = cls(state=state)
        project.save(using="alertdb")
