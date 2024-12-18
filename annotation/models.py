from django.db import models

class AnnotationProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ImageData(models.Model):
    project = models.ForeignKey(AnnotationProject, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

class AnnotatedData(models.Model):
    image = models.ForeignKey(ImageData, on_delete=models.CASCADE)
    annotation = models.JSONField()  # Store annotation data as JSON
    created_at = models.DateTimeField(auto_now_add=True)
