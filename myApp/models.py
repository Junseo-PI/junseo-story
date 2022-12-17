from django.db import models

# Create your models here.
class Project(models.Model):
    nick = models.CharField(default='', max_length=10)
    title = models.CharField(max_length=30)
    color = models.CharField(default='white', max_length=30)
    summary = models.CharField(max_length=500)
    #detail = models.CharField(max_length=1000)
    detail = models.TextField()
    link = models.URLField(default="www.naver.com", max_length=150)
    photo = models.ImageField(blank=True, upload_to="image")

    def __str__(self):
        return self.title

class Activity(models.Model):
    nick = models.CharField(default='', max_length=10)
    title = models.CharField(max_length=30)
    color = models.CharField(default='white', max_length=30)
    summary = models.CharField(max_length=500)
    #detail = models.CharField(max_length=1000)
    detail = models.TextField()
    link = models.URLField(default="www.naver.com", max_length=150)
    photo = models.ImageField(blank=True, upload_to="image")

    def __str__(self):
        return self.title

class Future(models.Model):
    nick = models.CharField(default='', max_length=10)
    title = models.CharField(max_length=30)
    detail = models.TextField()
    photo = models.ImageField(blank=True, upload_to="image")

    def __str__(self):
        return self.title





class en_Project(models.Model):
    nick = models.CharField(default='', max_length=10)
    title = models.CharField(max_length=50)
    color = models.CharField(default='white', max_length=30)
    summary = models.CharField(max_length=500)
    #detail = models.CharField(max_length=1000)
    detail = models.TextField()
    link = models.URLField(default="www.naver.com", max_length=150)
    photo = models.ImageField(blank=True, upload_to="image")

    def __str__(self):
        return self.title

class en_Activity(models.Model):
    nick = models.CharField(default='', max_length=10)
    title = models.CharField(max_length=50)
    color = models.CharField(default='white', max_length=30)
    summary = models.CharField(max_length=500)
    #detail = models.CharField(max_length=1000)
    detail = models.TextField()
    link = models.URLField(default="www.naver.com", max_length=150)
    photo = models.ImageField(blank=True, upload_to="image")

    def __str__(self):
        return self.title

class en_Future(models.Model):
    nick = models.CharField(default='', max_length=10)
    title = models.CharField(max_length=30)
    detail = models.TextField()
    photo = models.ImageField(blank=True, upload_to="image")

    def __str__(self):
        return self.title
