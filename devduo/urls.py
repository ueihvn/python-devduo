from rest_framework import routers, urlpatterns
from django.urls import include, path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>', views.user_detail)
]
