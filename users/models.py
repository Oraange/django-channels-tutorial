from __future__ import annotations
from typing import Optional

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from core.models import TimeStamp


class UserManager(BaseUserManager):
    use_in_migrations: bool = True

    def _create_user(self, nickname: str, password: str, **extra_fields):
        if not nickname:
            raise ValueError("The given nickname must be set")

        user = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using="alertdb")
        return user

    def create_user(self, nickname: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(nickname, password, **extra_fields)

    def create_superuser(self, nickname: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True')

        return self._create_user(nickname, password, **extra_fields)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).using("alertdb")


class User(AbstractBaseUser, PermissionsMixin, TimeStamp):
    nickname = models.CharField("아이디", max_length=50, unique=True)
    is_staff = models.BooleanField("관리자 권한", default=False)

    objects = UserManager()

    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        app_label = "users"

    @classmethod
    def get_by_nickname(cls, nickname: str) -> Optional[User]:
        try:
            return cls.objects.get(nickname=nickname, deleted_at__isnull=True)

        except cls.DoesNotExist:
            return None

    
