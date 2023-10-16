from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import * 

from django.shortcuts import render
from .models import Add_Module_Name,Blogs_Model
import sweetify
from django.http import JsonResponse
from .forms import BlogsForm, EditBlogForm, CkEditBlogsForm
from django.contrib.auth.decorators import login_required, user_passes_test



# Create your views here.


# def Add_Blog(request):
#     if request.method == "POST":
#         user_name = request.POST.get('user_name')  # Use get() method instead of indexing directly
#         module_name = request.POST.get('module_name')
#         blog = request.POST.get('blog')
#         blog_title = request.POST.get('blog_title')
#         obj1 = ""
#         obj2 = ""
#         if user_name is not None:  # Check if the 'user_name' key exists
#             if request.POST.get('module_id') != "":
#                 obj1 = Blogs_Model.objects.update_or_create(
#                     id=int(request.POST["module_id"]),
#                     defaults={"user_name": user_name, "module_name": module_name, "blog": blog, "blog_title": blog_title}
#                 )
#             else:
#                 obj2 = Blogs_Model.objects.create(
#                     user_name=user_name, module_name=module_name, blog=blog, blog_title=blog_title
#                 )
#             if obj1:
#                 sweetify.success(request, title="Success", icon='success',
#                                  text='Blog updated Successfully.', timer=1500)
#             elif obj2:
#                 sweetify.success(request, title="Success", icon='success',
#                                  text='Blog created Successfully.', timer=1500)
#             else:
#                 sweetify.success(request, title="Oops...",
#                                  icon='error', text='Fail to create.', timer=1000)
#         else:
#             # Handle the case when 'user_name' key is not present in the request
#             sweetify.success(request, title="Error", icon='error',
#                              text='Invalid user name.', timer=1500)

#     all_module = Add_Module_Name.objects.all()
#     all_blog = Blogs_Model.objects.all().order_by('-id')

#     for blog in all_blog:
#         try:
#             module_name_temp = Add_Module_Name.objects.get(id=blog.module_name)
#             module_name = module_name_temp.module_name
#         except Add_Module_Name.DoesNotExist:
#             module_name = ""

#         blog.module_name_new = module_name

#     context = {
#         "all_module": all_module,
#         "all_blogs": all_blog,
#         "BlogsForm": BlogsForm,
#         "CkEditBlogsForm": CkEditBlogsForm,
#     }
#     return render(request, "supports_faq/add_blogs.html", context)


# @login_required(login_url="/login/")
# @user_passes_test(is_owner, login_url="/login/")
def Add_Blog(request):
    if request.method == "POST":
        module_name = request.POST.get('module_name')
        blog = request.POST['blog']
        blog_title = request.POST['blog_title']
        obj1 = ""
        obj2 = ""
        if request.POST['module_id'] != "":
            obj1 = Blogs_Model.objects.update_or_create(
                id=int(request.POST["module_id"]), defaults={ "module_name": module_name, "blog": blog, "blog_title": blog_title})
        else:
            obj2 = Blogs_Model.objects.create(
                 module_name=module_name, blog=blog, blog_title=blog_title)
        if obj1:
            sweetify.success(request, title="Success", icon='success',
                             text='Blog updated Successfully.', timer=1500)

        elif obj2:
            sweetify.success(request, title="Success", icon='success',
                             text='Blog created Successfully.', timer=1500)
        else:
            sweetify.success(request, title="Oops...",
                             icon='error', text='Fail to create.', timer=1000)
    all_module = Add_Module_Name.objects.all()
    all_blog = Blogs_Model.objects.all().order_by('-id')

    for blog in all_blog:
        try:
            module_name_temp = Add_Module_Name.objects.get(id = blog.module_name)
            module_name = module_name_temp.module_name
        except:
            module_name = ""

        blog.module_name_new = module_name

    context = {
        "all_module": all_module,
        "all_blogs": all_blog,
        "BlogsForm": BlogsForm,
        "CkEditBlogsForm": CkEditBlogsForm,
        
    }
    return render(request, "supports_faq/add_blogs.html", context)


# @login_required(login_url="/login/")
# @user_passes_test(is_owner, login_url="/login/")
def Delete_Blog(request, id):
    status = Blogs_Model.objects.get(id=id).delete()
    if status:
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})
    
    
# @login_required(login_url="/login/")
# @user_passes_test(is_owner, login_url="/login/")
def GetBlogData(request, id):
    blog = Blogs_Model.objects.get(id=id)

    data = {
        'blog_messages':blog.blog,
        'id': blog.id,
        'user_name': blog.user_name,
        'module_name': blog.module_name,
        'blog_title': blog.blog_title,
    }
    
    if blog:
        return JsonResponse({"data":data})
    else:
        return JsonResponse({"success": False})
    
    
def Add_currency(request):
    if request.method == 'POST':
        currency_data = request.POST.get('currency_data')
        country_code = request.POST.get('country_code')
        value=Currency(currency_data=currency_data,country_code=country_code)
        value.save()
    data=Currency.objects.all()
    context={
        'data':data,
    }
    return render(request,'currency/currency.html',context)

def Add_support_faqs(request):
    if request.method == 'POST':
        questions = request.POST.get('questions')
        answers = request.POST.get('answers')
        value=Support_faq(questions=questions,answers=answers)
        value.save()
    data=Support_faq.objects.all()
    context={
        'data':data,
    }
    return render(request,'supports_faq/Support_faq.html',context)
    