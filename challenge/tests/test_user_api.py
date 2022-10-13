from django.test import SimpleTestCase
from django.urls import reverse,resolve
from rest_framework.test import APITestCase
from challenge.views import UserViewSet

class ApiUrlTests(SimpleTestCase):
    def test_get_users_is_resolved(self):
        url = reverse('users-list')
        self.assertEqual(resolve(url).func.__name__, UserViewSet.__name__)
        
        
class CourseAPIViewTest(APITestCase):
    courses_urls = reverse('course-list')
    
    def test_get_courses(self):
        response = self.client.get(self.courses_urls)
        self.assertEqual(response.status_code, 200)
        
    def test_post_courses(self):
        data = {
            "name":  "ingles"
        }
        response = self.client.post(self.courses_urls, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], "ingles")