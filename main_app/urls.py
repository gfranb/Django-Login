from django.urls import path, include
from . import views

urlpatterns = [
    path('main_page/', views.main_page),
    path('accounts/logout/', views.logout_user),
    path('', views.main_page),
    path('/', views.main_page)
]