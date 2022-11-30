from django.db import models

from core.models import TimeStamp


class ProjectManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).using("alertdb")

class Project(TimeStamp):
    state = models.PositiveSmallIntegerField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    objects = ProjectManager()

    class Meta:
        db_table = 'project'

    @classmethod
    def patch_state(cls, project_id: int, user_id: int, state: int) -> None:
        project: Project = cls.objects.get(id=project_id, user_id=user_id, deleted_at__isnull=True)
        project.state = state
        project.save(using="alertdb")

    @classmethod
    def generate(cls, state: int) -> None:
        project = cls(state=state)
        project.save(using="alertdb")

    @classmethod
    def get_by_user(cls, user_id: int):
        return cls.objects.filter(user_id=user_id)
