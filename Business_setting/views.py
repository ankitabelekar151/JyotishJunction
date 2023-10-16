from django.shortcuts import render


import os
import random
import sweetify

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django import template
from django.contrib.auth.decorators import login_required, user_passes_test
from Business_setting.forms import generalSettingForm
from login.models import *

# Create your views here.

def general_setting(request):
    form = generalSettingForm()
    if request.method == "POST":
        form = generalSettingForm(request.POST)
        if not form.is_valid():
            print('XXXXXXXXXXXX',form.errors)
        if form.is_valid():
            print('ssssssssssss')
            business_name = form.cleaned_data.get("business_name")
            business_category = form.cleaned_data.get("business_category")
            pin_code = form.cleaned_data.get("pin_code")
            business_code = form.cleaned_data.get("business_code")
            city = form.cleaned_data.get("city")
            area = form.cleaned_data.get("area")
            district = form.cleaned_data.get("district")
            state = form.cleaned_data.get("state")
            address = form.cleaned_data.get("address")
            alternate_mobile_number = form.cleaned_data.get("alternate_mobile_number")
            company_email = form.cleaned_data.get("company_email")
            alternate_email = form.cleaned_data.get("alternate_email")
            aadhaar = form.cleaned_data.get('aadhaar')

            temp= generalSetting.objects.update_or_create(id=1, defaults={'business_name': business_name,
                                                                                        'business_category':business_category,
                                                                                       'business_code': business_code,
                                                                                       'pin_code': pin_code,
                                                                                       'city': city, 'area': area,
                                                                                       'district': district,
                                                                                       'state': state,
                                                                                       'address': address,
                                                                                       'alternate_mobile_number': alternate_mobile_number,
                                                                                       'company_email': company_email,
                                                                                       'alternate_email': alternate_email,
                                                                                       'aadhaar': aadhaar})
         
         
         
         
            sweetify.success(request, title="Success", icon='success',
                             text='Business Settings Stored Successfully !!!')
            return redirect('/general-setting/')
        else:
            sweetify.error(request, title="error",
                           icon='error', text='Failed !!!')
    else:
        user = request.user
        if generalSetting.objects.all():
            data = generalSetting.objects.latest('id')
        else:
            data = None
            
        form = generalSettingForm()

    context = {
        'form': form,
        'data':data,
    }

    return render(request, "setting/Business_setting.html", context)



def privacy_policy(request):
    return render(request, "setting/privacy_policy.html")

def terms_of_service(request):
    return render(request, "setting/terms_of_service.html")

def Refund_Cancellation_Policy(request):
    return render(request, "setting/Refund_Cancellation_Policy.html")

def intellactual_property(request):
    return render(request, "setting/intellactual_property.html")
    
def faqs(request):
    return render(request, "setting/faqs.html")

def disclaimer(request):
    return render(request, "setting/disclaimer.html")


from admin_app.models import BlogPost

def add_blogs(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content1 = request.POST.get('content1')
        content2 = request.POST.get('content2')
        content3 = request.POST.get('content3')
        content4 = request.POST.get('content4')
        content5 = request.POST.get('content5')
        content6 = request.POST.get('content6')
        content7 = request.POST.get('content7')
        content8 = request.POST.get('content8')
        content9 = request.POST.get('content9')
        content10 = request.POST.get('content10')
        image = request.FILES.get('image')
        print()
        print('photo',image)
        print()
        BlogPost(title=title,image=image,content1=content1,content2=content2,content3=content3,content4=content4,content5=content5,content6=content6,content7=content7,content8=content8,content9=content9,content10=content10).save()
        
    return render(request,"setting/add_blogs.html")


from .models import *

def show_banner(request):
    data = BannerPost.objects.all()
    print()
    print('dataaaaaaaaaaa',data)
    print()
    return render(request,'setting/show_banner.html',{'data':data})


def del_banner(request,id):
    data = BannerPost.objects.get(id=id)
    data.delete()
    return redirect('/show_banner/')

def add_banner(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        BannerPost(title=title,image1=image1,image2=image2,image3=image3).save()
        return redirect("/show_banner/")
    return render(request,"setting/add_banner.html")


@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def astro_blog(request):
    blog = BlogPost.objects.all().order_by('-date')
    return render(request,"setting/astro_blog.html",{'blog':blog})


@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def astro_blog1(request,id):
    blogs = BlogPost.objects.all()
    blog = BlogPost.objects.get(id=id)
    return render(request,"setting/astro_blog1.html",{'blog':blog,'blogs':blogs})


def blogs_list(request):
    blog = BlogPost.objects.all().order_by('-date')
    return render(request,"setting/blogs_list.html",{'blog':blog})

# def blogs(request):
#     blog = BlogPost.objects.all().order_by('-date_created')
#     for i in blog :
#         print('iiiiiiiiiiiiii',i.title)
#     return render(request,"setting/blog.html",{'blog':blog})


def delete(request,id):
    blog = BlogPost.objects.get(id = id)
    blog.delete()
    return redirect('/blogs_list/')


# def blogs_1(request):
#     return render(request,"setting/blogs_1.html")

def blogs_2(request):
    return render(request,"setting/blogs_2.html")

def blogs_3(request):
    return render(request,"setting/blogs_3.html")

def blogs_4(request):
    return render(request,"setting/blogs_4.html")

def blogs_5(request):
    return render(request,"setting/blogs_5.html")

def blogs_6(request):
    return render(request,"setting/blogs_6.html")











def cust_refund(request):
	return render(request,"setting/cust_Refund_Cancellation_Policy.html")

def cust_faq(request):
	return render(request,"setting/cust_faq.html")

def cust_intel_property(request):
	return render(request,"setting/cust_intel_property.html")

def cust_disclaimer(request):
	return render(request,"setting/cust_disclaimer.html")

def cust_privacy_policy(request):
	return render(request,"setting/cust_privacy_policy.html")

def cust_tos(request):
	return render(request,"setting/cust_tos.html")

def cust_refund(request):
	return render(request,"setting/cust_refund.html")





def customer_blogs(request):
    blog = BlogPost.objects.all().order_by('-date_created')
    return render(request,"setting/customer_blog.html",{'blog':blog})





def blogs(request):
    blog = BlogPost.objects.all().order_by('-date_created')
    for i in blog :
        print('iiiiiiiiiiiiii',i.title)
    return render(request,"setting/dynamic_blog.html",{'blog':blog})  

# left


def blogs_1(request,id):
    blogs = BlogPost.objects.all().order_by('-date')
    blog = BlogPost.objects.get(id = id)
    return render(request,"setting/dynamic_blog1.html",{'blog':blog ,'blogs':blogs})

def before_login_blog(request,id):
    blogs = BlogPost.objects.all().order_by('-date')
    blog = BlogPost.objects.get(id = id)
    return render(request,"setting/dynamic_blog_before.html",{'blog':blog ,'blogs':blogs})



# def customer_blogs_1(request):
#     return render(request,"setting/customer_blog1.html")


# right
def customer_blogs_1(request,id):
    blog = BlogPost.objects.get(id = id)
    blogs = BlogPost.objects.all().order_by('-date_created')
    return render(request,"setting/customer_blog1.html",{'blog':blog,'blogs':blogs})


def customer_blogs_right(request,id):
    blog = BlogPost.objects.get(id = id)
    blogs = BlogPost.objects.all().order_by('-date_created')
    return render(request,"setting/customer_blog_right.html",{'blog':blog,'blogs':blogs})


def customer_blogs_2(request):
    return render(request,"setting/customer_blog2.html")

def customer_blogs_3(request):
    return render(request,"setting/customer_blog3.html")

def customer_blogs_4(request):
    return render(request,"setting/customer_blog4.html")

def customer_blogs_5(request):
    return render(request,"setting/customer_blog5.html")

def customer_blogs_6(request):
    return render(request,"setting/customer_blog6.html")
























def after_self_question(request):
    return render(request,"setting/after_self_question.html") 

def after_wealth_question(request):
    return render(request,"setting/after_wealth_question.html")

def after_health_question(request):
    return render(request,"setting/after_health_question.html") 

def after_family_question(request):
    return render(request,"setting/after_family_question.html")

def after_marriage_question(request):  
    return render(request,"setting/after_marriage_question.html")

def after_love_question(request):  
    return render(request,"setting/after_love_question.html")

def after_education_question(request):  
    return render(request,"setting/after_education_question.html")     


def after_carrier_question(request):  
    return render(request,"setting/after_carrier_question.html")

def after_business_question(request):  
    return render(request,"setting/after_business_question.html")

def after_hardtime_question(request):  
    return render(request,"setting/after_hardtime_question.html")

def after_puja_question(request):  
    return render(request,"setting/after_puja_question.html")

def after_spirituality_question(request):  
    return render(request,"setting/after_spirituality_question.html")    






def self_question(request):
    return render(request,"setting/self_question.html") 

def wealth_question(request):
    return render(request,"setting/wealth_question.html")

def health_question(request):
    return render(request,"setting/health_question.html") 

def family_question(request):
    return render(request,"setting/family_question.html")

def marriage_question(request):  
    return render(request,"setting/marriage_question.html")

def love_question(request):  
    return render(request,"setting/love_question.html")

def education_question(request):  
    return render(request,"setting/education_question.html")     


def carrier_question(request):  
    return render(request,"setting/carrier_question.html")

def business_question(request):  
    return render(request,"setting/business_question.html")

def hardtime_question(request):  
    return render(request,"setting/hardtime_question.html")

def puja_question(request):  
    return render(request,"setting/puja_question.html")

def spirituality_question(request):  
    return render(request,"setting/spirituality_question.html")    






    
# def ask_a_question_inr(request):  
#     return render(request,"setting/ask_a_question_inr.html")

from django.urls import reverse
import requests
def ask_a_question_inr(request):  
    print('rrrrrrrrrrrrrrrrrrrrr', request.user)
    data = admin_setting_plan.objects.all()
    plan = Plan_Purchase.objects.all()
    plan_data = Plan_Purchase.objects.filter(payment_id='')

    # Add the 'geolocation_url' context variable to be used in the template
    
    context={
        
        'plan': plan,
        'data': data,
    }   


    # if data.get('country', '') == 'IN':
    return render(request, 'setting/ask_a_question_inr.html',context)
    # else:     
    #     return render(request, 'setting/ask_a_question_dollor.html',context)


def ask_a_question_dollor(request):  
    return render(request,"setting/ask_a_question_dollor.html")


