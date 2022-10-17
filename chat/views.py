from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html") # chat 디렉토리에 있는 index.html 파일을 렌더링

