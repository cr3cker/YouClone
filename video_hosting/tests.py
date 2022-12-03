from django.test import TestCase
from .models import Video
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


class VideoModelTest(TestCase):
    """
    Tests for Video model
    """
    
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
    """
    Tests for Video views
    """
        
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


def create_valid_user():
    return UserCreationForm(data={'username': 'test', 'password1': 'Lusim010474', 'password2': 'Lusim010474'})


def create_invalid_user():
    return UserCreationForm(data={'username': 'test', 'password1': 'test', 'password2': 'test'})


class UserViewTest(TestCase):
    """
    Tests for User views
    """
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')


class UserFormTest(TestCase):
    """
    Tests for User forms
    """
        
    def test_form_valid(self):
        form = create_valid_user()
        self.assertTrue(form.is_valid())
    
    def test_form_invalid(self):
        form = create_invalid_user()
        self.assertFalse(form.is_valid())


class UserTokenTest(TestCase):
    """
    Tests for User token
    """

    def test_token_obtain(self):
        # Create user
        create_valid_user().save()
        # Get token
        response = self.client.post('/api/token/', data={'username': 'test', 'password': 'Lusim010474'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'access')
        self.assertContains(response, 'refresh')

        return response.json()['refresh']

    def test_token_refresh(self):
        response = self.client.post('/api/token/refresh/', data={'refresh': self.test_token_obtain()})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'access')



