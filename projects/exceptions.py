from django.http import JsonResponse

def handle_exception(func):
    def wrapper(request, *args, **kwargs):
        try:
            func()

        except ProjectNotFound:
            return JsonResponse({"message": "Project does not exist"}, status=404)


class ProjectNotFound(Exception): ...
