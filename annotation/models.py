from django.db import models
from django.conf import settings

class AnnotationProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

class ImageData(models.Model):
    project = models.ForeignKey(AnnotationProject, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.project.name}'

class AnnotatedData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ForeignKey(ImageData, on_delete=models.CASCADE)
    annotation = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ('-created_at',)

    def __str__(self):
        return f'{self.image.project}-annotated-{self.annotation["annotation"]}'