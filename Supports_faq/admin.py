from django.contrib import admin

# Register your models here.
from Supports_faq.models import Blogs_Model,Add_Module_Name,Currency,Support_faq
admin.site.register(Blogs_Model)
admin.site.register(Add_Module_Name)
admin.site.register(Currency)
admin.site.register(Support_faq)