from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content1 = models.TextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)
    content4 = models.TextField(null=True, blank=True)
    content5 = models.TextField(null=True, blank=True)
    content6 = models.TextField(null=True, blank=True)
    content7 = models.TextField(null=True, blank=True)
    content8 = models.TextField(null=True, blank=True)
    content9 = models.TextField(null=True, blank=True)
    content10 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.title
