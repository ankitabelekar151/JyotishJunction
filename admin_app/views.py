from django.shortcuts import render

# Create your views here.
from login.models import *
from Business_setting.models import *
import pycountry
from django.urls import reverse_lazy   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail 
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from login.forms import Signupform,customerform,EditProfileForm ,PasswordChangingForm 
import sweetify
from .models import *  
from django.contrib.auth.hashers import make_password  
import razorpay 
from django.contrib import messages  
from django.contrib.auth import authenticate  
from django.shortcuts import render,redirect
import datetime
import pytz
import pytz
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models import Count

 
# def admin_revenue(request):
#     data1=GurujiUsers.objects.filter(is_astrologer=True , is_approved= True)
#     print('llllllllllll',data1)
#     month_com = Comment.objects.all()
#     data5 = set()
#     for o in month_com:
#         fare = int(o.plan_amount) - int(o.astro_commision)
#         data4 = (o.cust_name,o.plan_purchase_date,o.plan_name,fare,o.astro_email_id,o.astro_commision)
#         if data4 not in data5:
#             data5.add(data4)
#     data = set()
#     if request.method == "POST":
#         plan_month=request.POST.get('month')
#         revnue=request.POST.get('revenue')
#         astro_name=request.POST.get('astro_name')
#         print("dataaaaaaaaaaaaaaaaa",plan_month,revnue,astro_name)
#         for i in data1:
#             for j in month_com:
#                 if i.name == astro_name and j.plan_month == plan_month:
#                     admin_fare = int(j.plan_amount) - int(j.astro_commision)
#                     #print('fareeeeeeeeeeeeeeeee',admin_fare)
#                     list_value = (j.cust_name,j.plan_purchase_date,j.plan_name,admin_fare,j.astro_email_id,j.astro_commision)
#                     if list_value not in data:
#                         data.add(list_value)
#     e_list = []
#     e_list1 = []
#     for i in data:
#         a= i[3]
#         b= i[5]
#         e_list.append(a)
#         e_list1.append(b)
         
#     admin_fare = 0
#     for k in e_list:
#         admin_fare = k + admin_fare
    
#     astro_commision = 0
#     for l in e_list1:
#         astro_commision = l + astro_commision
    
#     e_list2 = []
#     e_list3 = []
#     for m in data5:
#         admin_amt = m[3]
#         astro_com = m[5]
#         e_list2.append(admin_amt)
#         e_list3.append(astro_com)
    
    
#     admin_yearly=0
#     for n in e_list2:
#         admin_yearly = n + admin_yearly
    
#     astro_yearly = 0 
#     for c in e_list3:
#         astro_yearly = c + astro_yearly

    
#     context={
#         'data1':data1,
#         'data':data,
#         'admin_fare':admin_fare,
#         'astro_commision':astro_commision,
#         'data5':data5,
#         'admin_yearly':admin_yearly,
#         'astro_yearly':astro_yearly

#     }

#     return render(request,"admin/admin_revenue.html",context)

   
# def admin_revenue(request):

#     data1=GurujiUsers.objects.filter(is_astrologer=True , is_approved= True)
#     month_com = Comment.objects.all()
#     data5 = set()
#     for o in month_com:
#         fare = int(o.plan_amount) - int(o.astro_commision)
#         data4 = (o.cust_name,o.plan_purchase_date,o.plan_name,fare,o.astro_email_id,o.astro_commision,o.order_id)
#         if data4 not in data5:
#             data5.add(data4)
#     data = set()
#     astro_name= 0
#     plan_month= 0

#     if request.method == "POST":
#         plan_month=request.POST.get('month')
#         revnue=request.POST.get('revenue')
#         astro_name=request.POST.get('astro_name')
        


      
#         for i in data1:
#             for j in month_com:
#                 if i.name == astro_name and j.plan_month == plan_month:
#                     admin_fare = int(j.plan_amount) - int(j.astro_commision)
#                     print('admin_fare',admin_fare)
#                     list_value = (j.cust_name,j.plan_purchase_date,j.plan_name,admin_fare,j.astro_email_id,j.astro_commision)
#                     if list_value not in data:
#                         data.add(list_value)
#         data6 = list(data5)

    

#     e_list = []
#     e_list1 = []
#     for i in data:
#         a= i[3]
#         b= i[5]
#         e_list.append(a)
#         e_list1.append(b)
         
#     admin_fare = 0
#     for k in e_list:
#         admin_fare = k + admin_fare
    
#     astro_commision = 0
#     for l in e_list1:
#         astro_commision = l + astro_commision
    
#     e_list2 = []
#     e_list3 = []
#     for m in data5:
#         admin_amt = m[3]
#         astro_com = m[5]
#         e_list2.append(admin_amt)
#         e_list3.append(astro_com)
#     print('e_list2',e_list2)
    
    
#     admin_yearly=0
#     for n in e_list2:
#         admin_yearly = n + admin_yearly
    
#     astro_yearly = 0 
#     for c in e_list3:
#         astro_yearly = c + astro_yearly

    
#     total_comission = 0 
#     plan_total = 0
#     astro_name = GurujiUsers.objects.filter(id = astro_name)
#     for r in astro_name:

#         pk = Comment.objects.filter (astro_email_id = r.email_id,plan_month=plan_month)
#         for p in pk:
#             total_comission += int(p.astro_commision)
#             plan_total += int(p.plan_amount)
    
#     print('Total', plan_total,total_comission)

    
#     context={
#         'data1':data1,
#         'data':data,
#         'admin_fare':admin_fare,
#         'astro_commision':astro_commision,
#         'data5':data5,
#         'admin_yearly':admin_yearly,
#         'astro_yearly':astro_yearly,
#         'total_comission':total_comission,
#         'plan_total':plan_total,


#     }
   
#     return render(request,"admin/admin_revenue.html",context)
from django.db.models import Sum

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def admin_revenue(request):
    wallet = Wallet.objects.all()
    for w in wallet:
        print('kkkkkkkkk',w.recharge_amount)
    total_recharge_amount = Wallet.objects.aggregate(total=Sum('recharge_amount'))['total']
    total_debit_amount = Wallet.objects.aggregate(total=Sum('debit_amount'))['total']
    wallet_amount = total_recharge_amount - total_debit_amount

    print('Total recharge amount:', total_recharge_amount)
    selected_astrologer = None
    data1=GurujiUsers.objects.filter(is_astrologer=True , is_approved= True)
    month_com = Comment.objects.all()
    data5 = set()
    data4 = None
    for o in month_com:
        # fare = int(o.plan_amount) - int(o.astro_commision)
        plan_amount = float(o.plan_amount)/2
        astro_commission = float(o.astro_commision)
        if plan_amount == 0:
            fare = 0
        else:
            fare = plan_amount - astro_commission
        print('fare',fare)
        if o.send_admin:
            data4 = (o.cust_name,o.plan_purchase_date,o.plan_name,fare,o.astro_email_id,o.astro_commision,o.order_id,o.astro_name)
        # if data4 not in data5:
        if data4 is not None and data4 not in data5:
            data5.add(data4)
    data = set()
    astro_name= 0
    plan_month= 0

    if request.method == "POST":
        plan_month=request.POST.get('month')
        revnue=request.POST.get('revenue')
        astro_name=request.POST.get('astro_name')
        selected_astrologer = GurujiUsers.objects.get(id=astro_name).name
        print('selected',selected_astrologer)
        for i in data1:
            for j in month_com:   
                if i.name == astro_name and j.plan_month == plan_month:
                    admin_fare = float(j.plan_amount) - float(j.astro_commision)
                    print('admin_fare',admin_fare)
                    list_value = (j.cust_name,j.plan_purchase_date,j.plan_name,admin_fare,j.astro_email_id,j.astro_commision,j.order_id,j.astro_name)
                    if list_value not in data:
                        data.add(list_value)
        data6 = list(data5)
    e_list = []
    e_list1 = []
    for i in data:
        a= i[3]
        b= i[5]
        e_list.append(a)
        e_list1.append(b)
         
    admin_fare = 0
    for k in e_list:
        admin_fare = k + admin_fare
    
    astro_commision = 0
    for l in e_list1:
        astro_commision = l + astro_commision
    
    e_list2 = []
    e_list3 = []
    for m in data5:
        admin_amt = m[3]
        astro_com = m[5]
        e_list2.append(admin_amt)
        e_list3.append(astro_com)
    print('e_list2',e_list2)
    
    
    admin_yearly=0
    for n in e_list2:
        admin_yearly = n + admin_yearly
    
    astro_yearly = 0 
    for c in e_list3:
        astro_yearly = c + astro_yearly

    
    total_comission = 0 
    plan_total = 0
    
    ddd = set()
    
    astro_name = GurujiUsers.objects.filter(id = astro_name)
    for r in astro_name:

        rkkk = Comment.objects.filter (astro_email_id = r.email_id,plan_month=plan_month )

        
        for p in rkkk:
            data7 = (p.user,p.astro_email_id,p.plan_name,p.order_id,p.astro_commision,p.plan_amount)
            ddd.add(data7)
        for m in ddd:

            

            total_comission += float(m[4])
            plan_total += float(m[5])
        print('dddddddddd',ddd,total_comission,plan_total)
    
    # print('Total', plan_total,total_comission)
    

    
    context={
        'data1':data1,
        'data':data,
        'admin_fare':admin_fare,
        'astro_commision':astro_commision,
        'data5':data5,
        'admin_yearly':admin_yearly,   
        'astro_yearly':astro_yearly,
        'total_comission':total_comission,
        'plan_total':plan_total/2,
        'plan_month':plan_month,
        'selected_astrologer':selected_astrologer,
        'astro_name':astro_name,
        'wallet_amount':wallet_amount,


    }  
     
    return render(request,"admin/admin_revenue.html",context)



def admin_login_view(request):
    error_message = ""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # Check if user_id is an email or a mobile number
        if '@' in user_id:  # If '@' is present, consider it an email
            try:
                user = GurujiUsers.objects.get(email_id=user_id)
            except GurujiUsers.DoesNotExist:
                user = None
        else:  # Otherwise, consider it a mobile number
            try:
                user = GurujiUsers.objects.get(whatsapp_no=user_id)
            except GurujiUsers.DoesNotExist:
                user = None

        # Authenticate user
        if user is not None:
            user = authenticate(username=user.user_id, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/dash_admin/')
        else:
            error_message = 'Invalid email, or password'

    return render(request, 'admin/admin_login.html', {'error_message': error_message})  

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def UserEditViewAdmin(request):
    print('111111111111111111111',request.user.email_id)
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    print('data',data)
    if request.method == 'POST':
        data.user_id = request.POST.get('user_id')
        data.first_name =request.POST.get('first_name')
        data.last_name =request.POST.get('last_name')
        # data.dob = request.POST.get('dob')   
        data.whatsapp_no = request.POST.get('whatsapp_no')
        # data.address = request.POST.get('address')
        # data.pincode = request.POST.get('pincode')
        # data.city = request.POST.get('city')
        # data.state = request.POST.get('state')
        # data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        # data.birth_place = request.POST.get('birth_place')        
        # # country_code = request.POST.get('country')
        # try:
        #     country = pycountry.countries.get(alpha_2=country_code)
        #     if country:
        #         country_full_name = country.name
        # except:
        #     pass
        # data.country = country_full_name
        data.save()
        # sweetify.success(request, "Profile Updated successfully.", timer=3000)

    context = {
    'data':data,
    }
        
    return render(request,'admin/admin-profile.html',context)

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def dashboard_admin(request):
    data = GurujiUsers.objects.filter(is_astrologer= True).count()
    data1 = GurujiUsers.objects.filter(is_customer= True).count()
    data_astro = GurujiUsers.objects.filter(is_astrologer= True)  
    customer_list = GurujiUsers.objects.filter(is_customer= True)
    unapprove = GurujiUsers.objects.filter(is_astrologer = True, is_approved = False).count()
    approve = GurujiUsers.objects.filter(is_astrologer = True, is_approved = True).count()

  
    # plan = Plan_Purchase.objects.all()
    # cust_set = []
    # for k in plan:
    #     ddd = Comment.objects.filter(cust_name = k.name,plan_name = k.plan_name,plan_purchase_date = k.plan_purchase_date,payment_id = k.payment_id,user = k.cust_email_id).first()
    #     cust_set.append(ddd)
    # print('aaaaaaaaaaaaaa',len(plan),len(cust_set),cust_set)
    # for i in cust_set:
    #         print('iiiiiiiiiiiiii',i,i.payment_id)
    plan = Plan_Purchase.objects.all()
    cust_set = []

    for k in plan:
        ddd = Comment.objects.filter(
            cust_name=k.name,
            plan_name=k.plan_name,
            plan_purchase_date=k.plan_purchase_date,
            order_id=k.invoice_number,
            user=k.cust_email_id
        ).first()

        if ddd is not None:
            cust_set.append(ddd)
        else:
            print(f"No Comment object found for Plan_Purchase with id={k.id}")

    print('aaaaaaaaaaaaaa', len(plan), len(cust_set), cust_set)

    for i in cust_set:
        print('iiiiiiiiiiiiii', i, i.order_id)


    a,b,c = 0,0,0
    for p in plan:
        for i in cust_set:
           if p.invoice_number == i.order_id and p.cust_email_id == i.user:
                if i.comment2 == "" and i.astro_email_id == "":
                    a = a+1
                if i.comment2 == "" and i.astro_email_id != "":
                    b = b+1
                if i.comment2 != "" and i.astro_email_id != "":
                    c = c+1
    print('bbbbbbbbbbbb',a,b,c)

     

    
    

    context={'unapprove':unapprove,'data':data,'data1':data1,'data_astro':data_astro,'customer_list':customer_list,'a':a,'b':b,'c':c,'approve':approve}
    return render(request,'admin/dash_admin.html',context)


@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def astro_disable(request,id):
    user = GurujiUsers.objects.get(id=id)
    data = GurujiUsers.objects.get(email_id=user.email_id)
    data.is_astrologer = False
    data.is_approved = False
    data.save()
    return redirect('/astro_admin_approved/')



@login_required
@never_cache
def customer_disable(request,id):
    user = GurujiUsers.objects.get(id=id)
    data = GurujiUsers.objects.get(email_id=user.email_id)
    Plan_Purchase.objects.filter(cust_email_id=data).delete()

            # Delete entries from Comment model
    Comment.objects.filter(user=data).delete()

    # Delete entries from Wallet model
    Wallet.objects.filter(email_id=data).delete()
    
    data.delete()
    print("Customer",data,user)
    return redirect('/customer_admin/') 


@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache

def astro_admin_approved(request):
    astro = GurujiUsers.objects.filter(is_approved=True,is_astrologer = True).order_by('-astro_date')
    #print('astro',astro)

    context={
        'astro':astro,
    }
    return render(request,'admin/astro_admin_approved.html',context)

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def approve_astrologer(request, user_id):
    astrologer = GurujiUsers.objects.get(id=user_id)
    astrologer.save()
    return redirect('/admin_approval_astro/')







@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def admin_approval_astro(request):
    
    astro = GurujiUsers.objects.filter(is_approved=False,is_astrologer = True).order_by("-date_joined")
    print('astro',astro)

    context={
        'astro':astro,
    }
    return render(request,'admin/admin_approval_astro.html',context)

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def customer_admin(request):
    cust = GurujiUsers.objects.filter(is_customer=True).order_by('-date_joined')
    
    #print('astro',astro)

    context={
        'cust':cust,
        
    }
    return render(request,'admin/customer_info2_admin.html',context)

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def cust_pay_admin(request):
    #user= request.user.get()
    #print('ppppppppppppp',user)
    customers = GurujiUsers.objects.filter(email_id__in=Plan_Purchase.objects.values_list('cust_email_id', flat=True).distinct())
    plan=Plan_Purchase.objects.all()
    
    context ={
         'customers':customers,
         'plan':plan
              }
    
    return render(request,'admin/cust_pay_admin.html',context)



def logout_admin(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            logout(request)
            messages.success(request, "Logout successful")
    return redirect('/admin-login/')



from django.contrib.auth.hashers import make_password   
from django.contrib.auth.hashers import check_password
import re

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def changepass_admin(request):
    print(request.user.email_id)
    error_message = ''
    message = ''
    print(request.user.email_id)
    data = GurujiUsers.objects.get(email_id=request.user.email_id)
    print('data', data)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        new_pass1 = request.POST.get('new_pass1')
        new_pass2 = request.POST.get('new_pass2')

        if new_pass1 and new_pass2:
            if new_pass1 != new_pass2:
                error_message = 'Passwords do not match.'
            elif len(new_pass1) < 8:
                error_message = 'Password must be at least 8 characters long.'
            elif len(new_pass1) > 100:
                error_message = 'Password cannot exceed 100 characters.'    
            elif not re.match(r'^(?=.*[a-zA-Z])(?=.*[@!#$])(?=.*[0-9])[a-zA-Z0-9@!#$]{8,}$', new_pass1):
              error_message = 'Password must contain lowercase and uppercase letters (a to z or A to Z), numbers (0 to 9), and at least one of the symbols @, !, #, or $.'
            else:
                user = GurujiUsers.objects.get(user_id=request.user.user_id)
                check_password(password, user.password)
                user.password = make_password(new_pass1)
                user.save()
                message = 'Password updated successfully.'
                if request.user.is_superuser:
                    return redirect('/admin-login/')
                # if request.user.is_admin:
                #     return redirect('/admin-login/')
                # if request.user.is_astrologer:
                #     return redirect('/astrologer-login/')
    return render(request, 'admin/changepass_admin.html', {'error_message': error_message, 'message': message})
import requests
import json
import base64

def send_sms_approved(recipient_numbers,name):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Congratulations {$var1}, Your onboarding request is approved. Happy Consulting. Regards NKB Divine Vedic Sciences"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name)

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": recipient_numbers,
        "data": {
            "var1": name
        },
        "type": "sms",
        "reference": "XOXO",
        "validity": "30",
        "type_details": "",
        "data_coding": "plain",
        "flash_message": False,
        "scheduled_dt": "2019-12-17T14:26:57+00:00",
        "created_dt": "2019-12-15T14:26:57+00:00",
        "campaign_id": "25083275",
        "template_id": "383825074"
    }

    # Prepare headers with authentication
    credentials = f"{app_id}:{app_key}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200 and response.json().get("result") == 0:
        print("SMS sent successfully")
        print(response.json())
        return response.json().get("job_id")
    else:
        print("Failed to send SMS")
        print(response.json())
        return None

import pytz
from datetime import datetime

from django.core.mail import send_mail

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def commisionastro(request,id):
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    formatted_date = current_date.strftime('%Y-%m-%d')
    user = GurujiUsers.objects.get(id=id)
    print(request)
    data = GurujiUsers.objects.get(email_id = user.email_id)    
    whatsapp_no = data.whatsapp_no
    name = data.name
    # print('data1',appro_astro)
    print('data',data)
    if request.method == 'POST':
        commision = request.POST.get('commision')
        print('commision',commision)
        user.commision = commision
        subject = 'Astrologer Onboarding Approved - Request for Acceptance and Additional Information '
        message = f"Dear {user.name},\n\n" \
                f"Greetings from Guruji Speaks! We hope this email finds you in good health and high spirits. We are pleased to inform you that your application for onboarding as an Astro consultant on our platform has been approved.\n\n "\
                f"We believe that your profound knowledge and expertise in astrology will greatly benefit our users, providing them with valuable insights and guidance. We are excited to have you join our team of esteemed astrologers and look forward to a fruitful and mutually beneficial association. \n\n"\
                f"To proceed further, we kindly request you to confirm your acceptance of our offer and provide us with the necessary information and documents mentioned below: \n\n"\
                f"Acceptance Confirmation: Kindly revert to this email, indicating your acceptance of the onboarding offer and your willingness to sign the Memorandum of Understanding (MOU) that outlines the terms and conditions of our engagement.\n\n"\
                f"Bank Account Details: Please provide us with the following details: \n\n"\
                f"Bank Account Number:\n Bank Name:\n Branch Address:\n IFSC Code:\n Personal Identification Details:\n\n"\
                f"PAN Number:\n Aadhar Number:\n Contact Address: Kindly provide your complete residential address, including the city, state, and postal code. \n\n"\
                f"Scanned Copies of Documents: Please attach the following scanned copies: \n\n"\
                f"Cancelled Cheque (bearing your name and account details)\n PAN Card\n Aadhar Card\n Recent Photograph (passport size)\n We assure you that all the information provided will be handled with strict confidentiality and will only be used for the purpose of onboarding and maintaining our records. \n\n"\
                f"Once we receive your acceptance and the requested details, we will proceed with the preparation of the MOU for your review and signature. We kindly request you to send the required information and documents within Three days to avoid any delays in the onboarding process. \n\n"\
                f"If you have any questions or need further clarification regarding the onboarding process, please feel free to reach out to us. We are here to assist you at every step.  \n\n"\
                f"We once again congratulate you on being approved as an astrologer on our platform and eagerly await your response. We are certain that your presence will enrich our community and help countless individuals seeking guidance and enlightenment.\n\n"\
                f"Thank you for choosing Guruji Speaks as your platform for sharing your astrological wisdom. We are honored to have you on board.\n\n"\
                f"Best Regards,\n" \
                f"The Team at Guruji Speaks"
        from_email = settings.CAREERS_FROM_EMAIL
        send_mail(
            subject,
            message,
            from_email,
            [user.email_id],
            fail_silently=False,
            auth_user=settings.EMAIL_HOST_USER_CAREERS,
            auth_password=settings.EMAIL_HOST_PASSWORD_CAREERS,
            connection=None
        )

        user.is_approved = True
        user.astro_date =formatted_date
        user.astro_approve_time =current_time
        user.save()

        recipient_number = [whatsapp_no]  
        send_sms_approved(recipient_number,name)
        return redirect("/admin_approval_astro/")
    # if request.method == 'POST':
    #     data.name =request.POST.get('name')
        
    #     data.whatsapp_no = request.POST.get('whatsapp_no')
    #     data.country = request.POST.get('country')
    #     data.gender = request.POST.get('gender')
    #     data.experience = request.POST.get('experience')
    #     data.expertise = request.POST.get('expertise')
    #     data.languages_known = request.POST.get('languages_known')
    #     data.birth_time = request.POST.get('birth_time')
    #     data.email_id = request.POST.get('email_id')
    #     data.about_me = request.POST.get('about_me')
        
    #     data.save()
        # sweetify.success(request, "Profile created successfully.", timer=3000)
    
    # vend = venders.objects.all()

    context = {
    # 'vend':vend,
    'data':data,
    }
    
        
    return render(request,'admin/view_astro_profile.html',context)

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def UserEditView(request,id):
    print('111111111111111111111',request.user.email_id)
    user= GurujiUsers.objects.get(id=id)
    data = GurujiUsers.objects.get(email_id = user.email_id)
    print('data',data)
    if request.method == 'POST':
        #data.user_id = generate_random_password11()
        data.first_name =request.POST.get('first_name')
        data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        data.whatsapp_no = request.POST.get('whatsapp_no')
        data.address = request.POST.get('address')
        data.pincode = request.POST.get('pincode')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        data.country = request.POST.get('country')       
        country_code = request.POST.get('country')
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_full_name = country.name
        except:
            pass
        data.country = country_full_name
        data.save()
    context = {
    'data':data,
    }
        
    return render(request,'admin/cust_prof.html',context)

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def cus_to_ad_question(request):
    return render(request,'admin/ask-question-admin.html')

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def view_profile(request,id):
    data = GurujiUsers.objects.get(id=id)
    if request.method == 'POST':
        data.country = request.POST.get('country')
        data.gender = request.POST.get('gender')
        data.ifsc_no = request.POST.get('ifsc_no')
        data.account_no = request.POST.get('account_no')
        data.bank_name = request.POST.get('bank_name')
        data.aadhar_no= request.POST.get('aadhar_no')
        data.experience = request.POST.get('experience')
        data.expertise = request.POST.get('expertise')
        data.languages_known = request.POST.get('languages_known')
        data.about_me = request.POST.get('about_me')
        data.pan_no= request.POST.get('pan_no')
        data.save()
        sweetify.success(request, "Profile updated successfully.", timer=3000)
    data2 = GurujiUsers.objects.get(id=id)
    context = {
        'data':data2,
    }
    return render(request,'admin/view_profile.html',context)


@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def customer_to_admin(request):
    customer_que=''
    
    customer_plan = Plan_Purchase.objects.all().order_by('-purchase_date')
    
    
    for i in customer_plan:
        customer_que = Comment.objects.filter(user=i.cust_email_id,order_id = i.invoice_number)
        print('00000000000',customer_que)
        for j in customer_que:
           print('55555555',j) 
    cust_set = [] 
    for k in customer_plan:
        ddd = Comment.objects.filter(cust_name = k.name,plan_name = k.plan_name,order_id = k.invoice_number,user = k.cust_email_id).last()
        cust_set.append(ddd)
    print('222222222222222222222',len(cust_set),len(customer_plan))

    context = {
        # 'customer': customer,
        # 'comment_data': comment_data,
        # 'data1':data1,  
        # 'customer_plan_data': customer_plan_data,
        'customer_plan':customer_plan,
        'customer_que':customer_que,
        'cust_set':cust_set,
    }

    return render(request, 'admin/customer_to_admin.html', context)   

from django.core.mail import send_mail
# def admin_view_que(request,id):
#     print('jjjjjjjjjjj',id)
#     user = Plan_Purchase.objects.get(id=id)
#     # print('oooooooooooo',user.name)
#     astro = GurujiUsers.objects.filter(is_approved=True,is_astrologer=True)
#     que = Comment.objects.filter(user=user.cust_email_id,plan_name = user.plan_name)
    
#     data_que = Comment.objects.filter(user=user.cust_email_id,plan_name = user.plan_name).first()
#     if request.method == 'POST':
        
#         selected_astrologer_id = request.POST.get('astro_email_id')
#         print('selected_astrologer_id',selected_astrologer_id)
#         name = GurujiUsers.objects.get(email_id=selected_astrologer_id)
#         subject = f'Question Assignment'
#         message = f"Dear {name.name},\n\nWe have assigned {user.name}'s questions to you. This Question\n\nBest Regards,\nTeam Guruji Speaks"
#         sender_email = 'sender@example.com'  # Replace with your email address
#         recipient_email = selected_astrologer_id

#         send_mail(
#             subject,
#             message,
#             sender_email,
#             [recipient_email],
#             fail_silently=False,
#         )


#         for i in que:
#             i.astro_name = selected_astrologer_id
#             user2 = GurujiUsers.objects.get(email_id = selected_astrologer_id)
#             i.astro_email_id = user2.email_id
#             i.astro_commision = (int(i.plan_amount)*user2.commision)/100
#             i.save()
     
#     context={
#         'astro':astro,
#         'user':user,
#         "que": que,
#         'data_que':data_que,
       

#     }   
#     return render(request,'admin/admin_view_que.html',context)



from django.core.mail import send_mail

# def admin_view_que(request, id):
#     print('jjjjjjjjjjj', id)
#     user = Plan_Purchase.objects.get(id=id)
#     astro = GurujiUsers.objects.filter(is_approved=True, is_astrologer=True)
#     que = Comment.objects.filter(user=user.cust_email_id, plan_name=user.plan_name,payment_id = user.payment_id)
#     value1 = GurujiUsers.objects.get(email_id=user.cust_email_id)
#     print('111111111111111111',value1)

#     ans = Comment.objects.all()


    


#     for i in ans:
#         print('xxxxxxxxxxxxxxxxxxxx',i.comment2)
    
#     data_que = Comment.objects.filter(user=user.cust_email_id, plan_name=user.plan_name).first()
#     print('333333333333333333333333',data_que.astro_email_id)
#     if request.method == 'POST':
#         if request.POST.get('astro_email_id'):
#             selected_astrologer_id = request.POST.get('astro_email_id')
#             print('selected_astrologer_id', selected_astrologer_id)
#             name = GurujiUsers.objects.get(email_id=selected_astrologer_id)
#             subject = f'Guruji Speaks - A Question has been assigned to you'
#             message = f" Dear {name.name}\n\n"\
#             f" We have assigned {user.name} questions to you. Request you to go through the same and share your answers within 24 hours.\n\n 'Best Regards, \n Team Guruji Speaks"
#             sender_email = 'sender@example.com'  # Replace with your email address
#             recipient_email = selected_astrologer_id
#             send_mail(
#                 subject,
#                 message,
#                 sender_email,
#                 [recipient_email],
#                 fail_silently=False,
#             )

#             for i in que:
#                 i.astro_name = selected_astrologer_id
#                 user2 = GurujiUsers.objects.get(email_id=selected_astrologer_id)
#                 i.astro_email_id = user2.email_id
#                 i.astro_commision = (int(i.plan_amount) * user2.commision) / 100
#                 i.save()

#             edited_answer = request.POST.get('edited_answer')
#             if edited_answer:
#                 data_que.comment2 = edited_answer
#                 data_que.save()
#         else:
#             que1 = Comment.objects.filter(user=user.cust_email_id, plan_name=user.plan_name,payment_id = user.payment_id)
#             name = GurujiUsers.objects.get(email_id=data_que.astro_email_id)
#             for comment in que1:
#                 comment2_key = f'comment2_{comment.id}'  
#                 comment2 = request.POST.get(comment2_key)
#                 comment.comment2 = comment2
#                 comment.save()


     
#     context = {
#         'astro': astro,
#         'user': user,
#         "que": que,
#         'data_que': data_que,
#         'value1':value1,
#     }   
#     return render(request, 'admin/admin_view_que.html', context)
 
from django.urls import reverse
from django.core.mail import send_mail
import datetime

import pytz




def send_sms_astrologer(recipient_numbers,name):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Hello {$var1}, A user has asked a question. Please respond promptly. Happy Consulting. Regards NKB Divine."

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name)

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": recipient_numbers,
        "data": {
            "var1": name
        },
        "type": "sms",
        "reference": "XOXO",
        "validity": "30",
        "type_details": "",
        "data_coding": "plain",
        "flash_message": False,
        "scheduled_dt": "2019-12-17T14:26:57+00:00",
        "created_dt": "2019-12-15T14:26:57+00:00",
        "campaign_id": "25083275",
        "template_id": "898861735"
    }

    # Prepare headers with authentication
    credentials = f"{app_id}:{app_key}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200 and response.json().get("result") == 0:
        print("SMS sent successfully")
        print(response.json())
        return response.json().get("job_id")
    else:
        print("Failed to send SMS")
        print(response.json())
        return None




@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def admin_view_que(request, id):
    current_datetime_utc = datetime.datetime.now(pytz.utc)
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    current_time = current_datetime.time().strftime('%H:%M:%S')


    user = Plan_Purchase.objects.get(id=id)
    astro = GurujiUsers.objects.filter(is_approved=True, is_astrologer=True)
    que = Comment.objects.filter(user=user.cust_email_id, plan_name=user.plan_name,order_id = user.invoice_number)
    value1 = GurujiUsers.objects.get(email_id=user.cust_email_id)
    ans = Comment.objects.all()
   
        # print('xxxxxxxxxxxxxxxxxxxx',i.comment2)
    data_que = Comment.objects.filter(user=user.cust_email_id, plan_name=user.plan_name,order_id = user.invoice_number).last()
    astro_name = GurujiUsers.objects.filter(name = data_que.astro_name)
    # print(data_que.comment2)
    if request.method == 'POST':
        if request.POST.get('astro_email_id'):
            selected_astrologer_id = request.POST.get('astro_email_id')
            name = GurujiUsers.objects.get(name=selected_astrologer_id)
            print('nameeeeeeeeeeee',name)
            subject = f'Guruji Speaks - A Question has been assigned to you'
            message = f" Dear {name.name}\n\n"\
            f" We have assigned {user.name} questions to you. Request you to go through the same and share your answers within 24 hours.\n\n 'Best Regards, \n Team Guruji Speaks"
            sender_email = 'sender@example.com' 
            recipient_email = name.email_id
            send_mail(
                subject,   
                message,
                sender_email,
                [recipient_email],
                fail_silently=False,
            )
            for i in que:
                i.astro_name = selected_astrologer_id 
                i.admin_to_astrologer_time=current_time
                user2 = GurujiUsers.objects.get(name=selected_astrologer_id)

                recipient_numbers=user2.whatsapp_no
                print('uuuuuuuuuuu',recipient_numbers)
                name = user2.name
                print('astronameeeeeeeeeeee',name)
                i.astro_email_id = user2.email_id
                if i.plan_amount == '99':
                    i.astro_commision = 75
                    
                else:
                    i.astro_commision = (float(i.plan_amount)/2 * user2.commision) / 100
                # i.astro_commision = (int(i.plan_amount) * user2.commision) / 100
                i.save()
            send_sms_astrologer([recipient_numbers],name)
            edited_answer = request.POST.get('edited_answer')
            if edited_answer:
                data_que.comment2 = edited_answer
                data_que.save()

        else:
            que1 = Comment.objects.filter(user=user.cust_email_id, plan_name=user.plan_name,order_id = user.invoice_number)
            name = GurujiUsers.objects.get(email_id=data_que.astro_email_id)
            for comment in que1:
                comment2_key = f'comment2_{comment.id}'  
                comment2 = request.POST.get(comment2_key)
                comment.comment2 = comment2
                comment.save()
        
        

            

        # url = reverse('admin_view_que',args=[user.id])
        # return redirect(url)
        

        url = reverse('cust_to_admin')
        return redirect(url)


    data4 = Customer_profile.objects.filter(cust_id = user.cust_id)
    user_profile = GurujiUsers.objects.get(email_id = user.cust_email_id)
    context = {
        'astro': astro,
        'user': user,
        "que": que, 
        'data_que': data_que,
        'value1':value1,
        'data4':data4,
        'user_pro':f'{user_profile.first_name} {user_profile.last_name}',
        'astro_name':astro_name,
    }   
    return render(request, 'admin/admin_view_que.html', context)          







from django.http import HttpResponse
from django.core.mail import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# def generate_pdf_and_send_email(paragraph,email):
#     # Create a response object with PDF mimetype
#     response = HttpResponse(content_type='application/pdf')

#     # Set the filename of the PDF
#     pdf_filename = "example.pdf"
#     response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'

#     # Create a canvas and draw the paragraph on it
#     p = canvas.Canvas(response, pagesize=letter)
#     p.drawString(50, 700, paragraph)

#     # Save the PDF
#     p.save()

#     # Get the PDF content
#     pdf_content = response.getvalue()

#     # Create the EmailMessage object
#     subject = "PDF Report"
#     message = "Please find the attached PDF report."
#     from_email = "info@gurujispeaks.com"  # Replace this with your email
#     recipient_list = ["ramakantdubey1996@gmail.com"]  # Replace this with recipient's email

#     email = EmailMessage(subject, message, from_email, recipient_list)

#     # Attach the PDF to the email
#     email.attach(pdf_filename, pdf_content, 'application/pdf')

#     # Send the email
#     email.send()

#     return HttpResponse("Email sent with PDF attachment.")

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.urls import reverse
from django.core.mail import send_mail
import pytz
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import EmailMessage
import textwrap

# working but content is not coming properly

# def generate_pdf_and_send_email(cust_id,question, answer,customer_name,que_type):

#     # Create a response object with PDF mimetype
#     response = HttpResponse(content_type='application/pdf')

#     # Set the filename of the PDF
#     pdf_filename = "GSAstroAns.pdf"
#     response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'

#     # Create a canvas and draw the question and answer on it
#     p = canvas.Canvas(response, pagesize=letter)

#     # Set the positions for question and answer text
#     x, y = 0, 700

#     # Wrap the entire question block
#     wrapped_question = "\n".join(textwrap.wrap(f"\n      Question : {question}", width=110))

#     # Draw the wrapped question
#     for line in wrapped_question.split('\n'):
#         p.drawString(x, y, line)
#         y -= 20  # Adjust the y-coordinate for the next line

#     # Wrap the entire answer block
#     #wrapped_answer = "\n".join(textwrap.wrap(f"\nAnswer : Dear {customer_name},\nThank you for asking a question regarding your Health. According to your horoscope.\n  {answer} \n\nWe extend our best wishes to you, hoping that the insights provided have brought you clarity. At Guruji Speaks, we are committed to being your constant source of guidance, available to assist you whenever you need it.Sincerely,The Team at Guruji Speaks", width=110))

#     wrapped_answer = f"""Answer:
#         Dear {customer_name},
#         Thank you for asking a question regarding your {que_type}. According to your horoscope.
#         {answer}

#         We extend our best wishes to you, hoping that the insights provided have brought you clarity.At Guruji Speaks, we are committed to being your constant source of guidance, available to assist you whenever you need it.
#         Sincerely,
#         The Team at Guruji Speaks"""

#     # Draw the wrapped answer
#     for line in wrapped_answer.split('\n'):
#         p.drawString(x, y, line)
        
#         y -= 20  # Adjust the y-coordinate for the next line

#     # Save the PDF
#     p.save()

#     # Get the PDF content
#     pdf_content = response.getvalue()

#     # Create the EmailMessage object
#     subject = "PDF Report"
#     message = "Please find the attached PDF report."
#     from_email = "info@gurujispeaks.com"  # Replace this with your email
#     recipient_list = [cust_id]  # Replace this with recipient's email

#     email = EmailMessage(subject, message, from_email, recipient_list)

#     # Attach the PDF to the email
#     email.attach(pdf_filename, pdf_content, 'application/pdf')

#     # Send the email
#     email.send()

#     return HttpResponse("Email sent with PDF attachment.")
  

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph,Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
import re

def generate_pdf_and_send_email(cust_id,question, answer,customer_name,que_type):

    # Create a response object with PDF mimetype
    response = HttpResponse(content_type='application/pdf')

    # Set the filename of the PDF
    pdf_filename = "GSASTROANS.pdf"
    response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'

    # Create a PDF document using ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Create a list of elements to build the PDF content
    elements = []

    # Define custom styles for the question and answer headings
    heading_style = ParagraphStyle(
        name='HeadingStyle',
        parent=getSampleStyleSheet()["Normal"],
        fontSize=12,  # Adjust the font size
        leading=14,  # Adjust the line spacing
        fontName="Helvetica-Bold",  # Use a bold font
    )

    # Add a title
    title_style = getSampleStyleSheet()["Title"]
    elements.append(Paragraph("", title_style))

    # Add a spacer
    elements.append(Spacer(1, 12))

    # Add the question heading with custom style
    elements.append(Paragraph("Question:", heading_style))

    # Add the question
    question_style = getSampleStyleSheet()["Normal"]
    elements.append(Paragraph(f"{question}", question_style))

    # Add a spacer
    elements.append(Spacer(1, 12))

    # Define a regex pattern to find <br/> tags
    br_pattern = re.compile(r'<br/>')

    # Replace <br/> tags with actual line breaks
    answer_text = f"""
Dear {customer_name},<br/>
<br/>
{answer}<br/>

We extend our best wishes to you, hoping that the insights provided have brought you clarity.
At Guruji Speaks, we are committed to being your constant source of guidance, available to assist you whenever you need it.<br/><br/>
<br/>
Sincerely,<br/>
The Team at Guruji Speaks"""

    # Split the text using <br/> tags
    split_text = br_pattern.split(answer_text)

    # Add the answer heading with custom style
    elements.append(Paragraph("Answer:", heading_style))

    # Create a custom style for the answer with line spacing and bold font
    custom_style = ParagraphStyle(
        name='CustomAnswerStyle',
        parent=getSampleStyleSheet()["Normal"],
        fontSize=12,  # Adjust the font size
        leading=14,  # Adjust the line spacing
        fontName="Helvetica-Bold",  # Use a bold font
    )

    # Add the answer as paragraphs with the custom style
    for text in split_text:
        elements.append(Paragraph(text, custom_style))

    # Build the PDF document
    doc.build(elements)

    # Get the PDF content
    pdf_content = response.getvalue()

    # Create the EmailMessage object
    subject = "PDF Report"
    message = "Please find the attached PDF report."
    from_email = "info@gurujispeaks.com"  # Replace this with your email
    recipient_list = [cust_id]  # Replace this with recipient's email

    email = EmailMessage(subject, message, from_email, recipient_list)

    # Attach the PDF to the email
    email.attach(pdf_filename, pdf_content, 'application/pdf')

    # Send the email
    email.send()

    return HttpResponse("Email sent with PDF attachment.")




def send_sms_customer(recipient_numbers,name):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Dear {$var1}, Our expert astrologer has answered a question your recently asked. Please visit our site / e mail to read your response. Stay blessed. NKB Divine Vedic Sciences"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name)

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": recipient_numbers,
        "data": {
            "var1": name
        },
        "type": "sms",
        "reference": "XOXO",
        "validity": "30",
        "type_details": "",
        "data_coding": "plain",
        "flash_message": False,
        "scheduled_dt": "2019-12-17T14:26:57+00:00",
        "created_dt": "2019-12-15T14:26:57+00:00",
        "campaign_id": "32670970",
        "template_id": "933090696"
    }

    # Prepare headers with authentication
    credentials = f"{app_id}:{app_key}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200 and response.json().get("result") == 0:
        print("SMS sent successfully")
        print(response.json())
        return response.json().get("job_id")
    else:
        print("Failed to send SMS")
        print(response.json())
        return None



def admin_sms_astro(number,name1):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name1 # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Dear {$var1}, Your answer has been sent to the user. Thank you for your valuable insights. Regards NKB Divine"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}",str(name1))
    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": number,
        "data": {
            "var1": name1
        },
        "type": "sms",
        "reference": "XOXO",
        "validity": "30",
        "type_details": "",
        "data_coding": "plain",
        "flash_message": False,
        "scheduled_dt": "2019-12-17T14:26:57+00:00",
        "created_dt": "2019-12-15T14:26:57+00:00",
        "campaign_id": "25083275",
        "template_id": "530367421"
    }

    # Prepare headers with authentication
    credentials = f"{app_id}:{app_key}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200 and response.json().get("result") == 0:
        print("SMS sent successfully")
        print(response.json())
        return response.json().get("job_id")
    else:
        print("Failed to send SMS")
        print(response.json())
        return None
# original

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def approved_question_admin(request, user):
    # ... (your existing code)

    current_datetime_utc = datetime.datetime.now(pytz.utc)
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    plan = Plan_Purchase.objects.get(id = user)
    name=plan.name
    recipient_numbers = plan.cust_whatsapp_no
    ffff=''
    email=plan.cust_email_id
    cust = Comment.objects.filter(user = plan.cust_email_id , plan_name = plan.plan_name,order_id = plan.invoice_number)
    for k in cust:
        k.astro_email_id
    # print('llllllllllllll',k.astro_email_id,k)
    astro_mail = k.astro_email_id
    aparna = GurujiUsers.objects.filter(email_id=astro_mail)
    for j in aparna:
        astrologer_name = j.name
        ffff = j.whatsapp_no

    # print('ffff',ffff,astrologer_name)
    number = ffff
    name1=astrologer_name


    for i in cust:
        if i.order_id != '':
            i.qapprove = True
            i.admin_to_customer_time=current_time
            i.save()


    subject = "Astrologer has answered your question"
    message = f"Dear {plan.name},\n\nWe would like to inform you that our esteemed astrologer has provided a response to your recent inquiry. Kindly visit our website or check your email to access the answer.\n\n"\
              f"We kindly request you to take a moment to rate the provided response, as it will greatly assist us in improving our services and meeting your expectations more effectively.\n\n"\
              f"Thank you for your continued support.\n\n"\
              f"Best regards,\nThe Team at Guruji Speaks\n"

    for i in cust:
        question = i.comment1
        answer = i.comment2
        cust_id = plan.cust_email_id
        customer_name = i.cust_name
        que_type = i.ques_type
        generate_pdf_and_send_email(cust_id,question, answer,customer_name,que_type)

    from_email = "aparna.b@zappkode.com"  # Update with your actual email address
    to_email = plan.cust_email_id
    send_mail(subject, message, from_email, [to_email])
    print('kkkkkkk', to_email)
    print('customer_name',plan.name)

    admin_sms_astro([number],name1)
    send_sms_customer([recipient_numbers],name)

    # url = reverse('admin_view_que', args=[plan.id])
    # return redirect(url)


    url = reverse('cust_to_admin')
    return redirect(url)







# def approved_question_admin(request,user):
#     current_datetime_utc = datetime.datetime.now(pytz.utc)
#     timezone = pytz.timezone('Asia/Kolkata')
#     current_datetime = current_datetime_utc.astimezone(timezone)
#     current_date = current_datetime.date()
#     current_time = current_datetime.time().strftime('%H:%M:%S')
#     plan = Plan_Purchase.objects.get(id = user)
#     print('zzzzz',plan.name)
#     email=plan.cust_email_id
#     cust = Comment.objects.filter(user = plan.cust_email_id , plan_name = plan.plan_name,order_id = plan.invoice_number)
#     for i in cust:
#         if i.order_id != '':
#             i.qapprove = True
#             i.admin_to_customer_time=current_time
#             i.save()

#     subject = "Astrologer has answered your question"
#     message = f"Dear  {plan.name},\n\nWe would like to inform you that our esteemed astrologer has provided a response to your recent inquiry. Kindly visit our website or check your email/WhatsApp to access the answer.\n\n"\
#     f"We kindly request you to take a moment to rate the provided response, as it will greatly assist us in improving our services and meeting your expectations more effectively.\n\n"\
#     f"Thank you for your continued support.\n\n"\
#     f"Best regards,\nThe Team at Guruji Speaks\n"\
    
#     paragraph = ""
#     end='\n'
#     print('eeeeeeeeeee')
#     for i in cust:

#         # Assuming you have the paragraph content in a variable named 'my_paragraph'
#         paragraph += f"Question",
#         paragraph += f"{i.comment1}"
#         paragraph += f"Answers",
#         paragraph +=f"{i.comment2}"

#         # Call the function with the variable
#         generate_pdf_and_send_email(paragraph)
    
#     # message = message.replace("palash", plan.cust_email_id)
#     from_email = "aparna.b@zappkode.com"  # Update with your actual email address
#     to_email = plan.cust_email_id
#     send_mail(subject, message, from_email, [to_email])
#     print('kkkkkkk',to_email)

    
    
#     url = reverse('admin_view_que',args=[plan.id])
#     return redirect(url)

#



# code of without half plan amount and woorking 

# def astro_payment(request,id ):
#     data = GurujiUsers.objects.get(id = id)
#     info = Comment.objects.filter(astro_email_id = data.email_id)
#     print('kkkkkkkkkkkkkkk',info)
#     same_combine = set()
#     for i in info:
#         same_info=(i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.astro_commision,i.user)
#         if same_info not in same_combine:
#             same_combine.add(same_info)
#     context={ 
#         'same_combine' : same_combine
#     }      
#     return render(request,'admin/astro_payment.html',context)
@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def astro_payment(request,id):
    data = GurujiUsers.objects.get(id=id)
    info = Comment.objects.filter(astro_email_id=data.email_id)
    total_earnings = 0 
    print('kkkkkkkkkkkkkkk', info)
    same_combine = set()
    for i in info:
        try:
            plan_amount = float(i.plan_amount)
            half_plan_amount = plan_amount / 2
        except ValueError:
            half_plan_amount = i.plan_amount
        same_info = (i.order_id, i.plan_name, half_plan_amount, i.purchase_date, i.astro_commision, i.user,i.cust_name)
        if same_info not in same_combine:
            same_combine.add(same_info)
            total_earnings += float(i.astro_commision)
    context = {
        'same_combine': same_combine,
        'total_earnings': total_earnings, 
    }
    return render(request, 'admin/astro_payment.html', context)  


# def astro_payment(request, id):
#     data = GurujiUsers.objects.get(id=id)
#     info = Comment.objects.filter(astro_email_id=data.email_id)
#     print('kkkkkkkkkkkkkkk', info)
#     same_combine = set()
#     for i in info:
#         try:
#             plan_amount = float(i.plan_amount)
#             half_plan_amount = plan_amount / 2
#         except ValueError:
#             half_plan_amount = i.plan_amount
#         same_info = (i.order_id, i.plan_name, half_plan_amount, i.purchase_date, i.astro_commision, i.user)
#         if same_info not in same_combine:
#             same_combine.add(same_info)
#     context = {
#         'same_combine': same_combine
#     }
#     return render(request, 'admin/astro_payment.html', context)

@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def monthly_admin(request,astro_email_id):
    # Get unique values of plan_month and their counts
    unique_months = Comment.objects.values('plan_month').annotate(month_count=Count('plan_month')).distinct()
    print('llll',unique_months)
    
    return render(request, 'admin/month_admin.html', {'unique_months': unique_months,'astro_email_id':astro_email_id})


@login_required(login_url=settings.ADMIN_LOGIN_URL)
@never_cache
def monthly_commission_admin(request,astro_email_id,plan_month):
    data = Comment.objects.filter(plan_month=plan_month,astro_email_id=request.user.email_id)
    info = Comment.objects.filter(astro_email_id=astro_email_id,plan_month=plan_month)
    total_commission = sum(float(i.astro_commision) for i in info)
    print('kkkkkkk',total_commission)
    # same_combine = set()
    for i in info:
        print(i.astro_commision,i.plan_month)
        
    context = {     
        # 'same_combine': same_combine,
        'info':info,
        'total_commission':total_commission
        }
    return render (request,'admin/monthly.html',context)  
