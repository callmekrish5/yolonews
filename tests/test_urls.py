from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import home , national, international


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url= reverse('news:home')
        f = resolve(url).func
        # self.assertEqual(f.__name__, Inbox.__name__)
        self.assertEqual(f.__module__, home.__module__)



    def test_national_url(self):
        url= reverse('news:national')
        f = resolve(url).func
        self.assertEqual(f.__module__, national.__module__)


    def test_international_url(self):
        url= reverse('news:international')
        f = resolve(url).func
        self.assertEqual(f.__module__, international.__module__)
        
    
