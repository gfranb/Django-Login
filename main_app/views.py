from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(redirect_field_name="/login/")
def main_page(request):
    return render(request, "main_page.html", {
        'user' : request.user
    })

def logout_user(request):
    logout(request)
    print(request.user)
    return redirect("/login/")
