from django.test import TestCase, Client
from .models import DesireInfo
from django.urls import reverse, resolve
from .views import *

# Create your tests here.
class ModelTestCase(TestCase):
    def test_upload_title_blank(self):
        pk =DesireInfo.objects.create(title="milan")
        self.assertTrue(pk.upload_title_blank())
    def test_image_blank(self):
        pk =DesireInfo.objects.create(pdf="")
        self.assertTrue(pk.image_blank())
    def test_title_char(self):
        pk =DesireInfo.objects.create(title="milan")
        self.assertTrue(pk.title_char())
    # def test_cover(self):
    #     pk =DesireInfo.objects.create(pdf==True)
    #     self.assertTrue(pk.cover())

    def test_string_representation(self):
        info = DesireInfo(title="My string title")
        self.assertEqual(str(info), info.title)

    def test_post_list_view(self):
    # template_name = 'class_Order_list.html'
        response = self.client.get(reverse('info'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'class_Order_list.html')
        

