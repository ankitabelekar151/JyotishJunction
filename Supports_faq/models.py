
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blogs_Model(models.Model):
    user_name = models.CharField(max_length=1000, null=True, default="")
    module_name = models.CharField(max_length=1000, null=True, default="")
    blog = RichTextUploadingField(blank=True, null=True)
    blog_title = models.CharField(max_length=1000, null=True, default="")


class Add_Module_Name (models.Model):
    user_name = models.CharField(max_length=1000, null=True, default="")
    module_name = models.CharField(max_length=1000, null=True, default="")
    
class Currency(models.Model):
    currency_data = models.CharField(max_length=1000, null=True, default="")
    country_code = models.CharField(max_length=1000, null=True, default="")
    
class Support_faq(models.Model):
    questions = models.CharField(max_length=1000, null=True, default="")
    answers = models.CharField(max_length=1000, null=True, default="")