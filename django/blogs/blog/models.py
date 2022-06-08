from django.db import models

# Create your models here.
#更改完moedel後要記得執行以下兩行
#python manage.py makemigrations
#python manage.py migrate   

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title