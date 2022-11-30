from django.http import JsonResponse

from .models import Project


def handle_exception(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            return func(self, request, *args, **kwargs)

        except Project.DoesNotExist:
            return JsonResponse({"message": "Project does not exist"}, status=404)

    return wrapper
