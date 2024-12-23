from django.urls import path
from . import views

app_name = 'annotation'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_images, name='project_images'),
    path('save_annotation/<int:image_id>/', views.save_annotation, name='save_annotation'),
]
