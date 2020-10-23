from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import index, add
from .models import Posts

# Create your tests here.

class IndexTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('index')  #It takes the name of url as argument
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/blog/')   # / should also be used before blog
        self.assertEqual(view.func, index)


class NewPostsTest(TestCase):
    def setUp(self):
        Posts.objects.create(title='Django', slug='mywork', tagline='hello', content='contents')
    def test_post_view_success_status_code(self):
        url = reverse('add', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_view_not_found_status_code(self):
        url = reverse('add', kwargs={'id': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_post_url_resolves_add_view(self):
        view = resolve('/blog/add/1/')
        self.assertEqual(view.func, add)
