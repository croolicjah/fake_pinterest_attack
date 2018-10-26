from django.db import models

class MyUser(models.Model):
    email = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Photo(models.Model):
    photo = models.ImageField(max_length=255)
    description = models.TextField()
    likes = models.ManyToManyField(MyUser)

class Comment(models.Model):
    content = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)