from django.contrib import admin
from .models import AnnotationProject, ImageData, AnnotatedData

admin.site.register(AnnotationProject)
admin.site.register(ImageData)
admin.site.register(AnnotatedData)
