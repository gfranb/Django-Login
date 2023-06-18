from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LogInUser

# Create your views here.
def login_user(request):
    if request.method == "POST":
        current_user = authenticate(username = request.POST["username"], password = request.POST["password"])
        if current_user is not None:
                login(request,current_user)
                return redirect("/main_page/")
    else:
        return render(request, "login_page.html", {
            'login_form' : LogInUser
        })

