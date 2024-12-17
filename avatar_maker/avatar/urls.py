# avatar/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('avatar/<int:avatar_id>/', views.view_avatar, name='view_avatar'),
]
