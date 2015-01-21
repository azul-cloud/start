from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from .models import User
from .factories import NormalUserFactory


class MainSetUp(TestCase):
    def setUp(self):
        self.user = NormalUserFactory


class MainModelTest(MainSetUp):

    def test_model(self):
        # instance = Model.objects.get(name = "Tag 1")
        # self.assertNotEqual(instance.slug, None)
        pass


class MainViewTest(MainSetUp, WebTest):
    def setUp(self):
        MainModelTest.setUp(self)

    def test_home(self):
        url = reverse('main_home')
        response = self.app.get(url, user=self.user)


class MainFormTest(MainSetUp, WebTest):
    def test_blog_create_form(self):
        pass
        # url = reverse('blog_create')

        # post = {
        #     "title":"Posted Title",
        #     "headline":"My headline",
        #     "body":"<h1>Incoming from test</h1>",
        #     "city":self.city
        # }

        # response = self.app.post(url, post, user=self.user)

        # # make sure the response has the newly created post
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, post['title'])
    

