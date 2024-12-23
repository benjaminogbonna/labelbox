from django.contrib import admin
from .models import AnnotationProject, ImageData, AnnotatedData

admin.site.register(AnnotationProject)
admin.site.register(ImageData)
# admin.site.register(AnnotatedData)

@admin.register(AnnotatedData)
class AnnotatedDataAdmin(admin.ModelAdmin):
    list_display = ('image', 'annotation', 'user', 'created_at')