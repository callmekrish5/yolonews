from django.test import TestCase, Client
from django.urls import reverse
from news_user.models import *
import json


class TestViews(TestCase):

    def test_login_get(self):
        client= Client()
        response= client.get(reverse('news_user:login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'news_user/login.html')

    def test_register_get(self):
        client= Client()
        response= client.get(reverse('news_user:register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'news_user/register.html')



   
