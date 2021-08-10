from django.db import models
from django.db.models.base import Model

class Video(models.Model):
    video = models.FileField(upload_to='videos/%Y/%m', blank=True)

class Works(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=50)
    work_banner = models.ImageField(upload_to = 'images/works/banner/%Y/%m')

class Team(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/team')
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkdin = models.URLField(max_length=200, blank=True)
    designation = models.CharField(max_length=100, default="Member")
    country= models.CharField(max_length=100, default="Bangladesh")