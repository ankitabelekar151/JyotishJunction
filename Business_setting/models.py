from django.db import models

# Create your models here.

class BannerPost(models.Model):
    title = models.CharField(max_length=200) 
    image1 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='banner_images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title