from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import AnnotationProject, ImageData, AnnotatedData
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
import json

def index(request):
    return render(request, 'index.html')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def project_list(request):
    projects = AnnotationProject.objects.all()
    return render(request, 'annotation/project_list.html', {'projects': projects})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def project_images(request, project_id):
    project = get_object_or_404(AnnotationProject, id=project_id)
    # images = project.images.all()
    # return render(request, 'annotation/project_images.html', {'project': project, 'images': images})
    images = ImageData.objects.filter(project=project).exclude(annotateddata__isnull=False)
    return render(request, "annotation/project_images.html", {"project": project, "images": images})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_annotation(request, image_id):
    if request.method == "POST":
        try:
            image = get_object_or_404(ImageData, id=image_id)
            data = json.loads(request.body)
            annotation_text = data.get('annotation')

            if not isinstance(annotation_text, dict):
                return JsonResponse({"status": "error", "message": "Invalid annotation format"}, status=400)

            AnnotatedData.objects.create(
                image=image,
                annotation=annotation_text,
                user=request.user
            )
            return JsonResponse({"status": "success"})
        except ImageData.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Image not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)