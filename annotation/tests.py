from django.test import TestCase
from .models import AnnotationProject, ImageData, AnnotatedData
from django.core.files.uploadedfile import SimpleUploadedFile
import json

# Model Tests
class AnnotationProjectModelTest(TestCase):
    def setUp(self):
        self.project = AnnotationProject.objects.create(
            name="Test Project",
            description="This is a test project"
        )

    def test_project_creation(self):
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(self.project.description, "This is a test project")
        self.assertIsNotNone(self.project.created_at)

class ImageDataModelTest(TestCase):
    def setUp(self):
        self.project = AnnotationProject.objects.create(
            name="Test Project",
            description="This is a test project"
        )
        self.image = ImageData.objects.create(
            project=self.project,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_image_creation(self):
        self.assertEqual(self.image.project, self.project)
        self.assertTrue(self.image.image.name.endswith("test_image.jpg"))
        self.assertIsNotNone(self.image.created_at)

class AnnotatedDataModelTest(TestCase):
    def setUp(self):
        self.project = AnnotationProject.objects.create(
            name="Test Project",
            description="This is a test project"
        )
        self.image = ImageData.objects.create(
            project=self.project,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )
        self.annotation = AnnotatedData.objects.create(
            image=self.image,
            annotation={"label": "test", "coordinates": [100, 200]}
        )

    def test_annotation_creation(self):
        self.assertEqual(self.annotation.image, self.image)
        self.assertEqual(self.annotation.annotation["label"], "test")
        self.assertEqual(self.annotation.annotation["coordinates"], [100, 200])
        self.assertIsNotNone(self.annotation.created_at)


# View Tests
from django.urls import reverse
from django.test import TestCase
from .models import AnnotationProject, ImageData
from django.core.files.uploadedfile import SimpleUploadedFile

class ProjectListViewTest(TestCase):
    def setUp(self):
        AnnotationProject.objects.create(name="Project 1", description="Description 1")
        AnnotationProject.objects.create(name="Project 2", description="Description 2")

    def test_project_list_view(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project 1")
        self.assertContains(response, "Project 2")
        self.assertTemplateUsed(response, 'annotation/project_list.html')

class ProjectImagesViewTest(TestCase):
    def setUp(self):
        self.project = AnnotationProject.objects.create(name="Test Project", description="This is a test project")
        self.image = ImageData.objects.create(
            project=self.project,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_project_images_view(self):
        response = self.client.get(reverse('project_images', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")
        self.assertContains(response, "test_image.jpg")
        self.assertTemplateUsed(response, 'annotation/project_images.html')

class SaveAnnotationViewTest(TestCase):
    def setUp(self):
        self.project = AnnotationProject.objects.create(name="Test Project", description="This is a test project")
        self.image = ImageData.objects.create(
            project=self.project,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        )
        self.annotation_url = reverse('save_annotation', args=[self.image.id])

    def test_save_annotation_post(self):
        data = {
            "annotation": {"label": "test", "coordinates": [100, 200]}
        }
        response = self.client.post(
            self.annotation_url,
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "success"})
        self.assertEqual(self.image.annotateddata_set.count(), 1)
        self.assertEqual(self.image.annotateddata_set.first().annotation["label"], "test")