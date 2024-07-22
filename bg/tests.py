from django.test import TestCase, Client

# Create your tests here.

class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()

    def test_correct_static_template_for_mainpage(self):
        response = self.client.get('')
        template = 'bg/index.html'
        self.assertTemplateUsed(response, template)

