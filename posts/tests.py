from django.test import TestCase
from .models import post
from django.utils import timezone
# Create your tests here.


class PostTest(TestCase):
    def setUp(self):
        post.objects.create(
            post_header='Python',
            post_content='Learning python.',
            post_date=timezone.now(),
        )
        post.objects.create(
            post_header='C++',
            post_content='Learning C++.',
            post_date=timezone.now(),
        )

    def test_post_header(self):
        obj1 = post.objects.get(post_header='Python')
        obj2 = post.objects.get(post_content='Learning C++.')

        self.assertEqual(obj1.post_header, 'Python')
        self.assertEqual(obj2.post_header, 'C++')

    def test_post_content(self):
        obj1 = post.objects.get(post_header='Python')
        obj2 = post.objects.get(post_header='C++')

        self.assertEqual(obj1.post_content, 'Learning python.')
        self.assertEqual(obj2.post_content, 'Learning C++.')

    def test_post_date(self):
        obj1 = post.objects.get(post_header='Python')
        obj2 = post.objects.get(post_header='C++')

        self.assertIsNotNone(obj1.post_date, timezone.now())
        self.assertIsNotNone(obj2.post_date, timezone.now())
        
