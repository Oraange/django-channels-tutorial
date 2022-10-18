from django.http import HttpRequest
from django.shortcuts import HttpResponse, render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html") # chat 디렉토리에 있는 index.html 파일을 렌더링

def room(request: HttpRequest, room_name) -> HttpResponse:
    return render(request, "chat/room.html", {"room_name": room_name})
