from django.urls import path
from . import views

urlpatterns = [
    path('front_page', views.front_page, name='home'),
    path('members', views.members,name = 'home'),
]
