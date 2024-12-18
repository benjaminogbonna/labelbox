from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import AnnotationProject, ImageData, AnnotatedData
from django.views.decorators.csrf import csrf_exempt
import json

def project_list(request):
    projects = AnnotationProject.objects.all()
    return render(request, 'annotation/project_list.html', {'projects': projects})

def project_images(request, project_id):
    project = get_object_or_404(AnnotationProject, id=project_id)
    images = project.images.all()
    return render(request, 'annotation/project_images.html', {'project': project, 'images': images})

@csrf_exempt
def save_annotation(request, image_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        image = get_object_or_404(ImageData, id=image_id)
        AnnotatedData.objects.create(image=image, annotation=data)
        return JsonResponse({'status': 'success'})
