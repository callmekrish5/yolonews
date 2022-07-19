from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Reporter(models.Model):
    name= models.CharField(max_length=80)
    email= models.EmailField()
    phone=models.CharField(max_length=15)
    profile=models.ImageField(upload_to='reporters_pp')
    joined_date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url=self.profile.url
        except:
            url=''
        return url


class Category(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category


class News(models.Model):
    date= models.DateField(auto_now_add=True)
    heading= models.CharField(max_length=300)
    details= models.TextField()
    photo= models.ImageField(upload_to='news_photos')
    reporter= models.ForeignKey(Reporter, on_delete=models.CASCADE)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    recent= models.BooleanField(default=False)
   
    def __str__(self):
        return self.heading

    @property
    def imageUrl(self):
        try:
            url=self.photo.url
        except:
            url=''
        return url



    


