from django.test import TestCase
from .models import Video
from django.urls import reverse


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


class VideoViewTest(TestCase):
        
            @classmethod
            def setUpTestData(cls):
                # Set up non-modified objects used by all test methods
                Video.objects.create(title='test title', description='test description', image='test image', file='test file')
        
            def test_view_url_accessible_by_name(self):
                response = self.client.get(reverse('video', args=[1]))
                self.assertEqual(response.status_code, 200)
        
            def test_view_uses_correct_template(self):
                response = self.client.get(reverse('video', args=[1]))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'video_hosting/video.html')
        
            def test_view_url_accessible_by_name(self):
                response = self.client.get(reverse('stream', args=[1]))
                self.assertEqual(response.status_code, 200)
        
            def test_view_uses_correct_template(self):
                response = self.client.get(reverse('stream', args=[1]))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'video_hosting/video.html')
        
            def test_view_url_accessible_by_name(self):
                response = self.client.get(reverse('home'))
                self.assertEqual(response.status_code, 200)
        
            def test_view_uses_correct_template(self):
                response = self.client.get(reverse('home'))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'video_hosting/home.html')    
    