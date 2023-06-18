from django.urls import path, include
from . import views

urlpatterns = [
    path('main_page/', views.main_page),
    path('logout/', views.logout_user)
]