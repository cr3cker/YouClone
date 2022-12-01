from django.test import TestCase
from .models import Video


class VideoModelTest(TestCase):
    
        @classmethod
        def setUpTestData(cls):
            # Set up non-modified objects used by all test methods
            Video.objects.create(title='test title', description='test description', image='test image', file='test file')
    
        def test_title_content(self):
            video = Video.objects.get(id=1)
            expected_object_name = f'{video.title}'
            self.assertEquals(expected_object_name, 'test title')
    
        def test_description_content(self):
            video = Video.objects.get(id=1)
            expected_object_name = f'{video.description}'
            self.assertEquals(expected_object_name, 'test description')
    
        def test_image_content(self):
            video = Video.objects.get(id=1)
            expected_object_name = f'{video.image}'
            self.assertEquals(expected_object_name, 'test image')
    
        def test_file_content(self):
            video = Video.objects.get(id=1)
            expected_object_name = f'{video.file}'
            self.assertEquals(expected_object_name, 'test file')
    
        def test_object_name_is_title(self):
            video = Video.objects.get(id=1)
            expected_object_name = video.title
            self.assertEquals(expected_object_name, str(video))
    