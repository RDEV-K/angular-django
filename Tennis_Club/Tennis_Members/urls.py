from django.urls import path
from .views import users
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', users, name="users"),
    # path('create-user', createUser, name="create-user"),
    # path('<int:pk>/update', home, name="update-user"),
    # path('<int:pk>/delete', home, name="delete-user"),
]