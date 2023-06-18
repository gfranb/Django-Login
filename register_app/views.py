from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateNewUser

# Create your views here.
def register_user(request):
    if request.method == "POST":
        new_user = User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
            email=request.POST["email"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            )
        new_user.save()
        return redirect("/login/")
    else:
        return render(request, "register_page.html", {
            'register_form' : CreateNewUser
        })
