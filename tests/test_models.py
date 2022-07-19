from django.test import TestCase
from news.models import Reporter

class ModelTests(TestCase):
    def reportertest(self):
        reporter=AppUser()
        reporter.name= 'Dipesh'
        reporter.email= 'dipesh@gmail.com'
        
        reporter.phone= '98010202202'
        reporter.profile =null
        reporter.save()

        ok=Reporter.ojbects.get(id=reporter.id)
        self.assertEqual(Reporter, ok)