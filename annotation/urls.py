from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_images, name='project_images'),
    path('save_annotation/<int:image_id>/', views.save_annotation, name='save_annotation'),
]
