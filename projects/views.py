import json
import time
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from .service import StateUpdate


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "projects/index.html")

def my_test(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        data = json.loads(request.body)

        state_service = StateUpdate()

        for state in [1, 2, 3, 4, 5]:
            state_service.update_state(1, state)
            time.sleep(5)

        return JsonResponse({"message": "Updated"}, status=201)
