from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import User


class MainModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "main_test_user",
            "email@domain.com",
            "testpassword",
        )

    def test_model(self):
        # instance = Model.objects.get(name = "Tag 1")
        # self.assertNotEqual(instance.slug, None)
        pass


class MainViewTest(TestCase):
    def setUp(self):
        MainModelTest.setUp(self)

        self.client.login(username=self.user.username, 
            password='testpassword')

    def test_home(self):
        url = reverse('main_home')
        response = self.client.get(url)


class MainFormTest(TestCase):

    def setUp(self):
        MainViewTest.setUp(self)

    def test_blog_create_form(self):
        pass
        # url = reverse('blog_create')

        # post = {
        #     "title":"Posted Title",
        #     "headline":"My headline",
        #     "body":"<h1>Incoming from test</h1>",
        #     "city":self.city
        # }

        # response = self.client.post(url, post)

        # # make sure the response has the newly created post
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, post['title'])
    

