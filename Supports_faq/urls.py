from django.urls import path, include
from . import views

urlpatterns = [
    path("add-blog/", views.Add_Blog, name="add-blog"),
    path("delete-blog/<int:id>", views.Delete_Blog, name="delete-blog"),
    path("get-blog-data/<int:id>/", views.GetBlogData, name="get-blog-data"),
    path("Add-currency/", views.Add_currency, name="Add-currency"),
    path("Add_support_faqs/", views.Add_support_faqs, name="Add_support_faqs"),
]