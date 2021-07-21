from django.test import TestCase
from app1.models import Post
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint

class TestAppModels(TestCase):


    @classmethod
    def setUpTestData(self):
        testuser1 = User.objects.create_user(
            username='user1',password='1234')
        testuser2 = User.objects.create_user(
            username='user2',password='4321')
        self.title = Post.objects.create(
            title="django", content="New content", slug="django")
        self.title.likes.set([testuser1.pk, testuser2.pk])

    def test_model_str1(self):
        self.assertEqual(str(self.title), "django")

    def test_post_has_an_author(self):
        self.assertEqual(self.title.likes.count(), 2)

    def test_get_absolute_url(self):
        self.title.slug = Post.objects.get(id=1)
        self.assertEqual("/django/", self.title.slug.get_absolute_url())

class TestNew(TestCase):
    def setUp(self):
        self.post = baker.make('app1.Post')
        pprint(self.post.__dict__)

    def test_model_str(self):
        title = Post.objects.create(title="Django Testing")
        content = Post.objects.create(content="This is some content")
        self.assertEqual(str(title), "Django Testing")



    