from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import redirect, render

from users.models import User


def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "users/signup.html")

    elif request.method == "POST":
        data = request.POST.dict()
        nickname = data["name"]
        password = data["password"]

        is_user = User.objects.using("alertdb").filter(nickname=nickname).exists()

        if is_user:
            return redirect("https://http.cat/409")

        User.objects.create_user(nickname=nickname, password=password)

        return redirect("signin")

def signin(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "users/signin.html")

    elif request.method == "POST":
        data = request.POST.dict()
        nickname = data["name"]
        password = data["password"]

        user_model: User = get_user_model()
        user = user_model.get_by_nickname(nickname)

        if not user:
            return redirect("https://http.cat/401")

        if not user.check_password(password):
            return JsonResponse({"message": "Log in Failed"}, status=401)

        login(request, user)

        return redirect("/projects")

def signout(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        logout(request)
        return redirect("/users/signin")
