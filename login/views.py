from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.template import loader
from django.http import HttpResponse
import pycountry
from django.urls import reverse_lazy   
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordChangeView 
from django.views import generic 
from django.contrib.auth import authenticate, login, logout  
import sweetify
from .models import *    
from django.contrib.auth.hashers import make_password  
import razorpay 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import datetime
# from dateutil.relativedelta import relativedelta 
import datetime   
from django.urls import reverse
import paypalrestsdk
import random
from django.contrib.auth.decorators import login_required

import requests
import json
import base64

import random
from django.contrib.auth.decorators import login_required
import string
from django.contrib import messages


# def send_sms(recipient_numbers):
#     # EnableX credentials
#     app_id = "64b4bd31112b540fbd054d49"
#     app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

#     # SMS details
#     sender_id = "NKBDVN"
#     var1 = {{name}}  # Replace this with the actual value you want to pass
#     # Template message with {$ var1} placeholder
#     message_template = "Hello {$var1}, thank you for registering as an astrologer."

#     # Replace {$ var1} with the actual value
#     message = message_template.replace("{$var1}", var1)
#     # message = "Thank you for registering as an astrologer."
#     # API endpoint
#     url = "https://api.enablex.io/sms/v1/messages/"

#     print('var1',var1)

#     # Prepare the payload
#     payload = {
#         "from": sender_id,
#         "to": recipient_numbers,
#         "data": {
#             "message": message
#         },
#         "type": "sms",
#         "reference": "XOXO",
#         "validity": "30",
#         "type_details": "",
#         "data_coding": "plain",
#         "flash_message": False,
#         "scheduled_dt": "2019-12-17T14:26:57+00:00",
#         "created_dt": "2019-12-15T14:26:57+00:00",
#         "campaign_id": "25083275",
#         "template_id": "531785614"
#     }

#     # Prepare headers with authentication
#     credentials = f"{app_id}:{app_key}"
#     encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
#     headers = {
#         "Authorization": f"Basic {encoded_credentials}",
#         "Content-Type": "application/json"
#     }

#     # Send the POST request
#     response = requests.post(url, headers=headers, data=json.dumps(payload))

#     # Check the response
#     if response.status_code == 200 and response.json().get("result") == 0:
#         print("SMS sent successfully")
#         print(response.json())
#         return response.json().get("job_id")
#     else:
#         print("Failed to send SMS")
#         print(response.json())
#         return None



import json
import base64
import hashlib
import requests
from django.shortcuts import render


def initiate_phonepe_payment(request):
    # Define the payload
    payload = {
        "merchantId": "M1V0CXVZ7AGF",
        "merchantTransactionId": transaction_id,
        "merchantUserId": request.user.user_id,
        "amount": paisa * 100,
        "redirectUrl": "https://www.gurujispeaks.com/",
        "redirectMode": "POST",
        "callbackUrl": "https://www.gurujispeaks.com/",
        "mobileNumber": request.user.user_id,
        "paymentInstrument": {
            "type": "PAY_PAGE"
        } 
}
    url = "https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/pay"
    encoded_payload = json.dumps(payload, separators=(',', ':')).encode('utf-8')
    print('encoded_payload',encoded_payload)


    base64_payload = base64.b64encode(encoded_payload).decode('utf-8')
    print('base64_payload',base64_payload)


    salt_key = "099eb0cd-02cf-4e2a-8aca-3e6c6aff0399"
    salt_index = "1"
    # x_verify_data = (base64_payload + "/pg/v1/pay" + salt_key) + "###" + salt_index

    x_verify_data = (base64_payload + "/pg/v1/pay" + salt_key) 

    print('x_verify_data',x_verify_data)


    x_ver = hashlib.sha256(x_verify_data.encode('utf-8')).hexdigest() + "###" + salt_index
    print('x_verifyooooooooooooooooooooooooo',x_ver)


    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "X-VERIFY": x_ver
    }
    response = requests.post(url, headers=headers, json=json.dumps(payload))
    print('response',response.text)


    response_data = response.json()
    print('response_data',response_data)
    if response_data["success"]:
        redirect_info = response_data["data"]["instrumentResponse"]["redirectInfo"]
        redirect_url = redirect_info.get("url", "Redirect URL not provided")
        return render(request, 'payment_form.html', {'success': True, 'result': redirect_url})
    else:
        error_message = response_data.get("message", "Unknown error occurred")        
        if error_message == "Unknown error occurred":
            print("PhonePe API response:", response_data)


        return render(request, 'payment_form.html', {'success': False, 'result': error_message})




def send_sms(recipient_numbers,name):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Greetings {$var1}, We have received your request for onboarding at NKB Divine Vedic Sciences platform. We will get back to you soon."

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name)
    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
    # print("var1:", var1)
    print("message_template:", message_template)
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
        "template_id": "612088229"
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





def astrologer_signup(request):
    if request.method == "POST":
        user_id = generate_random_password11()
        whatsapp_no = request.POST.get('whatsapp_no')   
        password = request.POST.get('password')
        email_id = request.POST.get('email_id')
        expertise_values = request.POST.getlist('expertise')
        languages_knowns = request.POST.getlist('languages_known')
        name = request.POST.get('name')
        expertise_values_str = ', '.join(expertise_values)
        languages_knowns_str = ', '.join(languages_knowns)

        print('lllll',user_id,whatsapp_no,password,email_id)

        password = make_password(request.POST['password'])
        conform_password = make_password(request.POST['confirm_password'])
        country_code = request.POST.get('country')
        password_no = request.POST.get('password')
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_full_name = country.name
        except:
            pass
        country = country_full_name  


        if GurujiUsers.objects.filter(email_id=email_id).exists():
            return redirect('/error_email/')

        # Check for duplicate whatsapp_no
        if GurujiUsers.objects.filter(whatsapp_no=whatsapp_no).exists():
            return redirect('/error_mobile/')  

        guruji_user = GurujiUsers( user_id =user_id, whatsapp_no = whatsapp_no, email_id=email_id ,country=country, name=name, password=password,expertise=expertise_values_str,
            languages_known=languages_knowns_str,is_astrologer=True,is_active=True,is_staff=True,)
        guruji_user.save()


        # sms
        recipient_number = [whatsapp_no]  
        # send_sms(recipient_number,name)
        # Save the job_id in the user's model instance
        
        # end sms

        subject = 'Welcome to Our Astrologer Platform'
        message = f"Dear {name},\n\n" \
          f"Welcome to Jyotish Junction. We are thrilled to have you on-board. Kindly note, we will be having verification call soon for the process forward. \n\nYou cannot Login Until Admin Approve \n\n" \
          f"Looking forward to speaking to you soon.\n\n" \
          f"Best Regards,\n" \
          f"Team Jyotish Junction"
        from_email = settings.CAR_FROM_EMAIL
        recipient_list = [email_id]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD, connection=None)

        return redirect('/astrologer-login/')
        
    return render(request, 'login/astrologer-signup.html')





def generate_random_transaction_id():
    prefix = "guru_"
    random_digits = ''.join(random.choices(string.digits, k=12 - len(prefix)))
    transaction_id = prefix + random_digits
    return transaction_id


# astrologer changepass

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import re



from django.contrib.auth.hashers import check_password

@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def astrologer_changepass(request):
    print(request.user.email_id)
    error_message = ''
    message = ''
    disable_save_button = False  # Initialize the variable
    
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_pass1 = request.POST.get('new_pass1')
        new_pass2 = request.POST.get('new_pass2')

        # Retrieve the user object
        user = GurujiUsers.objects.get(email_id=request.user.email_id)

        # Check if the old password is correct
        if not check_password(old_password, user.password):
            error_message = 'Old password is incorrect.'
        elif new_pass1 != new_pass2:
            error_message = 'Passwords do not match.'
        elif len(new_pass1) < 8:
            error_message = 'Password must be at least 8 characters long.'
        elif len(new_pass1) > 100:
            error_message = 'Password cannot exceed 100 characters.'
        else:
            # Update the password
            user.password = make_password(new_pass1)
            user.save()
            message = 'Password updated successfully.'

            if request.user.is_astrologer:
                return redirect('/astrologer-login/')
        
        # Check if old password is the same as new password or confirm password
        if old_password == new_pass1 or old_password == new_pass2:
            disable_save_button = True

    return render(request, 'login/changepass_astrologer.html', {'error_message': error_message, 'message': message, 'disable_save_button': disable_save_button})




from admin_app.models import BlogPost  
from Business_setting import *


@login_required
@never_cache
def after_login_cus(request):
    banner = BannerPost.objects.all()
    blog = BlogPost.objects.all()
    user = GurujiUsers.objects.get(email_id=request.user)
    users_with_ratings = GurujiUsers.objects.exclude(Q(review_comments1='') | Q(review_star1='')).order_by('-id')[:3]
    return render (request,'login/customer_home.html',{'blog':blog,'banner':banner,
        'users':users_with_ratings})


# original


# def forgot_pass_view(request):
#     error_message = ""
#     if request.method == "POST":
#         user_id = request.POST.get('user_id')
#         user = GurujiUsers.objects.filter(email_id=user_id).last()
#         print('mmmmmmmmmmmmmmmmmmmmm',user)
#         if user:
#             password = generate_random_otp()
#             user.set_password(password)
#             user.save()
#             send_mail(
#                 'GurujiSpeaks New Password',
#                 f'Dear Sir/Madam,\n Warm Greetings from GurujiSpeaks Team!!! \n We are glad to see you GurujiSpeaks team and below are your login credentials for the same \n Username: {user_id},\n Password: {password}, \n You are advised to login.',
#                 'zappkodesolutions@gmail.com',
#                 [user.email_id],
#                 fail_silently=False,
#             )
#             if user.is_customer:
#                 return redirect('/customer-login/')
#             elif user.is_astrologer:
#                 return redirect('/astrologer-login/')
#             elif user.is_admin:
#                 return redirect('/admin-login/')
#         else:
#             error_message = 'The user ID you entered does not exist. Please try again.'
#     return render(request, 'login/enteremail.html', {'error_message': error_message})



import random

def generate_random_otp():
    return ''.join(random.choices('0123456789', k=6))



# def forgot_sms_otp(recipient_numbers,name,otp):
#     # EnableX credentials
#     app_id = "64b4bd31112b540fbd054d49"
#     app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"  

#     # SMS details
#     sender_id = "NKBDVN"
#     var1 = name
#     var2 = otp # Replace this with the actual value you want to pass
#     # Template message with {$ var1} placeholder
#     # message_template = "Hello {$var1}, Welcome your registration is successful. Start your astrological journey now. Regards NKB Divine Divine Vedic Sciences"

#     # Replace {$ var1} with the actual value
#     message_template = "Hi {$var1}, Your OTP for Jyotish Junction password reset is {$var2}. Please use it to reset your password securely. Regards NKB Divine"

#     # Replace {$ var1} with the actual value
#     message = message_template.replace("{$var1}", name).replace("{$var1}", otp)

#     # message = "Thank you for registering as an astrologer."
#     # API endpoint
#     url = "https://api.enablex.io/sms/v1/messages/"

   
   
#     print("message:", message)

#     # Prepare the payload
#     print(recipient_numbers[0])
#     user = GurujiUsers.objects.get(whatsapp_no=recipient_numbers[0])
#     if user.is_customer:
#         payload = {
#             "from": sender_id,
#             "to": recipient_numbers,
#             "data": {
#                 "var1": name,
#                 "var2": otp
#             },
#             "type": "sms",
#             "reference": "XOXO",
#             "validity": "30",
#             "type_details": "",
#             "data_coding": "plain",
#             "flash_message": False,
#             "scheduled_dt": "2019-12-17T14:26:57+00:00",
#             "created_dt": "2019-12-15T14:26:57+00:00",
#             "campaign_id": "25083275",
#             "template_id": "460506928"
#         }
#     else:
#         payload = {
#             "from": sender_id,
#             "to": recipient_numbers,
#             "data": {
#                 "var1": name,
#                 "var2": otp
#             },
#             "type": "sms",
#             "reference": "XOXO",
#             "validity": "30",
#             "type_details": "",
#             "data_coding": "plain",
#             "flash_message": False,
#             "scheduled_dt": "2019-12-17T14:26:57+00:00",
#             "created_dt": "2019-12-15T14:26:57+00:00",
#             "campaign_id": "25083275",
#             "template_id": "982575581",
#         }


#     # Prepare headers with authentication
#     credentials = f"{app_id}:{app_key}"
#     encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
#     headers = {
#         "Authorization": f"Basic {encoded_credentials}",
#         "Content-Type": "application/json"
#     }

#     # Send the POST request
#     response = requests.post(url, headers=headers, data=json.dumps(payload))

#     # Check the response
#     if response.status_code == 200 and response.json().get("result") == 0:
#         print("SMS sent successfully")
#         print(response.json())
#         return response.json().get("job_id")
#     else:
#         print("Failed to send SMS")
#         print(response.json())
#         return None






# latest live error when any number is entering 

# def forgot_pass_view(request):
#     error_message = ""
#     if request.method == "POST":
#         try:
#             user_id = request.POST.get('user_id')
#             user = GurujiUsers.objects.get(whatsapp_no=user_id,is_customer=True)
#         except:
#             user_id = request.POST.get('user_id')
#             user = GurujiUsers.objects.get(email_id=user_id,is_customer=True)

       
        
#         if user:
#             otp = generate_random_otp()
#             print('otp',otp)
#             request.session['temporary_otp'] = otp
#             request.session['user_id'] = user.email_id 
            
#             send_mail(
#                 'GurujiSpeaks Password Reset OTP',
#                 f'Your OTP is: {otp}',
#                 'jyotishjunction11@gmail.com',
#                 [user.email_id],
#                 fail_silently=False,
#             )
#             recipient_numbers = user.whatsapp_no
#             name = f"{user.first_name} {user.last_name}"
#             forgot_sms_otp([recipient_numbers],name,otp)
            
#             return render(request, 'login/enter_otp.html', {'user_id': user_id})
        
#         else:
#             error_message = 'The user ID you entered does not exist. Please try again.'
    
#     return render(request, 'login/enteremail.html', {'error_message': error_message})



from django.core.exceptions import ObjectDoesNotExist

def forgot_pass_view(request):
    error_message = ""
    if request.method == "POST":   
        user_id = request.POST.get('user_id')
        
        try:
            # Try to find the user by whatsapp_no first
            user = GurujiUsers.objects.get(whatsapp_no=user_id, is_customer=True)
        except ObjectDoesNotExist:
            try:
                # If not found, try to find the user by email_id
                user = GurujiUsers.objects.get(email_id=user_id, is_customer=True)
            except ObjectDoesNotExist:   
                # If both queries fail, the user does not exist
                user = None

        if user:
            otp = generate_random_otp()
            print('otp', otp)
            request.session['temporary_otp'] = otp
            request.session['user_id'] = user.email_id 

            send_mail(
                'jyotishjunction Password Reset OTP',
                f'Your OTP is: {otp}',
                'jyotishjunction11@gmail.com',
                [user.email_id],
                fail_silently=False,
            )
            recipient_numbers = user.whatsapp_no
            name = f"{user.first_name} {user.last_name}"
            # forgot_sms_otp([recipient_numbers], name, otp)

            return render(request, 'login/enter_otp.html', {'user_id': user_id})
        else:
            error_message = 'The Email Id does not exist. Please try again.'

    return render(request, 'login/enteremail.html', {'error_message': error_message})




def verify_otp_view(request):  
    error_message = ""  
    if request.method == "POST":
        try:
            user_id = request.session.get('user_id')
            user = GurujiUsers.objects.get(whatsapp_no=user_id)
            print(user_id)
        except:
            user_id = request.session.get('user_id')
            user = GurujiUsers.objects.get(email_id=user_id)
            print(user_id)
        d1 = request.POST.get('digit-1')
        d2 = request.POST.get('digit-2')
        d3 = request.POST.get('digit-3')
        d4 = request.POST.get('digit-4')
        d5 = request.POST.get('digit-5')
        d6 = request.POST.get('digit-6')
        otp = d1+d2+d3+d4+d5+d6
        entered_otp = otp
        print(request.session.get('user_id'))
        if request.session.get('user_id') == user.email_id and request.session.get('temporary_otp') == entered_otp:
            return render(request, 'login/set_new_password.html', {'user_id': user_id})
        else:
            error_message = 'Invalid OTP. Please try again.'
    
    return render(request, 'login/enter_otp.html', {'error_message': error_message})





def set_new_password_view(request):
    if request.method == "POST":
        try:
            user_id = request.session.get('user_id')
            user2 = GurujiUsers.objects.get(whatsapp_no=user_id)
            print(user_id)
        except:
            user_id = request.session.get('user_id')
            user2 = GurujiUsers.objects.get(email_id=user_id) 
            print(user_id)
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password == confirm_password and request.session.get('user_id') == user2.email_id:
            user = GurujiUsers.objects.get(email_id=user2.email_id)
            if user:
                print("Setting new password for user:", user.email_id)
                user.set_password(new_password)
                user.save()
                print("Password updated successfully.")   
                del request.session['temporary_otp']
                del request.session['user_id']
    
    # Redirect to the appropriate login page based on user type
                if user.is_customer:
                    print("Redirecting to customer login page...")
                    return redirect('/customer-login/')
                elif user.is_astrologer:
                    print("Redirecting to astrologer login page...")
                    return redirect('/astrologer-login/')
                elif user.is_admin:
                    print("Redirecting to admin login page...")
                    return redirect('/admin-login/')
    
    return render(request, 'login/set_new_password.html')






def astrologer_login_view(request):
    error_message=""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        # print('22222222222222222222222',user_id,password)
 
        if '@' in user_id: 
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
            user = authenticate(request, username=user.user_id, password=password)
        
        if user is not None and user.is_astrologer and user.is_approved:
            login(request, user)
            return redirect('/dash_astro/')
        else:
            if user is not None and user.is_astrologer and not user.is_approved:
                error_message = 'Astrologer not approved yet. Please wait for approval.'
            else:
                error_message = 'Invalid Email Id or password'
            
    return render(request, 'login/astro-login.html', {'error_message': error_message})
         





def generate_random_otp(length=6):
    characters = string.digits
    return ''.join(random.choice(characters) for i in range(length))







# latest with error when any number is enter

# def astrologer_forgot_pass_view(request):
#     error_message = ""
#     if request.method == "POST":
#         try:
#             user_id = request.POST.get('user_id')
#             user = GurujiUsers.objects.get(is_astrologer=True,whatsapp_no=user_id)
#         except:
#             user_id = request.POST.get('user_id')
#             user = GurujiUsers.objects.get(is_astrologer=True,email_id=user_id)

#         if user:
#             otp = generate_random_otp() 
#             print('otp',otp)
#             request.session['temporary_otp'] = otp
#             request.session['user_id'] = user.email_id 
#             send_mail(
#                 'Jyotish Junction New Password',
#                 f'Dear Sir/Madam,\n Warm Greetings from Jyotish Junction Team!!! \n We are glad to see you Jyotish Junction team and below are your login credentials for the same \n Username: {user_id},\n otp: {otp}, \n You are advised to login.',
#                 'jyotishjunction11@gmail.com',
#                 [user.email_id],
#                 fail_silently=False,
#             )
#             recipient_numbers = user.whatsapp_no
#             name = f"{user.name}"
#             forgot_sms_otp([recipient_numbers],name,otp)
#             return render(request, 'login/enter_otp.html', {'user_id': user_id})
#         else:
#             error_message = 'The user ID you entered does not exist. Please try again.'
#     return render(request, 'login/astrologer_enteremail.html', {'error_message': error_message})



def astrologer_forgot_pass_view(request):
    error_message = ""
    if request.method == "POST":
        user_id = request.POST.get('user_id')


        # try:
        #     user_id = request.POST.get('user_id')
        #     user = GurujiUsers.objects.get(is_astrologer=True,whatsapp_no=user_id)
        # except:
        #     user_id = request.POST.get('user_id')
        #     user = GurujiUsers.objects.get(is_astrologer=True,email_id=user_id)
        try:
            # Try to find the user by whatsapp_no first
            user = GurujiUsers.objects.get(whatsapp_no=user_id, is_astrologer=True)
        except ObjectDoesNotExist:
            try:
                # If not found, try to find the user by email_id
                user = GurujiUsers.objects.get(email_id=user_id, is_astrologer=True)
            except ObjectDoesNotExist:
                # If both queries fail, the user does not exist
                user = None

        if user:
            otp = generate_random_otp() 
            print('otp',otp)
            request.session['temporary_otp'] = otp
            request.session['user_id'] = user.email_id 
            send_mail(
                'Jyotish Junction New Password',
                f'Dear Sir/Madam,\n Warm Greetings from Jyotish Junction Team!!! \n We are glad to see you Jyotish Junction team and below are your login credentials for the same \n Username: {user_id},\n otp: {otp}, \n You are advised to login.',
                'jyotishjunction11@gmail.com',
                [user.email_id],
                fail_silently=False,
            )
            recipient_numbers = user.whatsapp_no
            name = f"{user.name}"
            # forgot_sms_otp([recipient_numbers],name,otp)
            return render(request, 'login/enter_otp.html', {'user_id': user_id})
        else:
            error_message = 'The Mobile Number you entered does not exist. Please try again.'
    return render(request, 'login/astrologer_enteremail.html', {'error_message': error_message})





def astrologer_forgotsuccess(request):
        user_id = request.POST.get('user_id')
        print('1111111111111111111111',user_id)
        if request.user.is_authenticated and request.user.is_astrologer:
            return redirect('/astrologer-login/')
        return render(request, 'login/astrologer_forgotpass.html')





from django.conf import settings
from django.core.files.storage import FileSystemStorage


@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def UserEditViewAstro(request):
    data = GurujiUsers.objects.get(email_id=request.user.email_id)   
    if request.method == 'POST':
        data.name = request.POST.get('name')
        data.whatsapp_no = request.POST.get('whatsapp_no')
        data.country = request.POST.get('country')
        data.gender = request.POST.get('gender')
        data.experience = request.POST.get('experience')
        data.expertise = request.POST.get('expertise')
        data.languages_known = request.POST.get('languages_known')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.about_me = request.POST.get('about_me')
        data.bank_name = request.POST.get('bank_name')
        data.account_no = request.POST.get('account_no')  
        data.ifsc_no = request.POST.get('ifsc_no')
        data.aadhar_no= request.POST.get('aadhar_no')
        data.pan_no= request.POST.get('pan_no')
        data.commision= request.POST.get('commision')
   
        # Handle profile picture upload
        image = request.FILES.get('image')
        if image:
            # Delete the previous image if it exists
            if data.image:
                data.image.delete()

            # Save the new profile picture to the user's profile
            data.image = image
        
        data.save()
        sweetify.success(request, "Profile updated successfully.", timer=3000)
    
    user = GurujiUsers.objects.get(email_id=request.user.email_id)
    context = {
        'data': data,
        'user': user,
    }
        
    return render(request, 'login/astrologer-profile.html', context)





















# astrologer otp



# def astro_login_otp(request):
#     error_message = ""
#     if request.method == 'POST':

#         user_id = request.POST.get('user_id')
#         usd=GurujiUsers.objects.filter(email_id=user_id).last()
#         if usd:
#             print('aparna',usd.whatsapp_no)

#         # Check if user_id is an email
#         if '@' in user_id:
#             try:
#                 user = GurujiUsers.objects.get(email_id=user_id)
#                 whatsapp_no = user.whatsapp_no

#                 print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',whatsapp_no)

#             except GurujiUsers.DoesNotExist:
#                 user = None
#         else:
#             try:
#                 user = GurujiUsers.objects.get(whatsapp_no=user_id)
#                 print('uuuuuuuu',user)
#             except GurujiUsers.DoesNotExist:
#                 user = None

#         if user is not None and user.is_astrologer:
#             # Generate OTP and store it in the session
#             otp = get_random_string(length=6, allowed_chars='0123456789')
#             request.session['login_otp'] = otp
#             request.session['login_user_id'] = user_id

#             # Send the OTP to the user's email
#             subject = 'Login OTP'
#             message = f"Dear user,\n\nYour OTP for login is: {otp}\n\nPlease enter this OTP to log in to your account.\n\nThank you!"
#             # message = render_to_string('login/otp_email.html', {'otp': otp})
#             print('aparna',message)
           
#             send_mail(subject, message, 'care@gurujispeaks.com', [user.email_id], fail_silently=False)

#             # Redirect to OTP verification page
#             return redirect('/otp-verification-astro/')
#         else:
#             error_message = 'Invalid user ID or email'

#     return render(request, 'login/astro_otp_login.html', {'error_message': error_message})





def send_sms_otp(user_id,name1,otp):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name1
    var2 = otp # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    # message_template = "Hello {$var1}, Welcome your registration is successful. Start your astrological journey now. Regards NKB Divine Divine Vedic Sciences"

    # Replace {$ var1} with the actual value
    message_template = "Hi {var1}, Your OTP for sign up is {var2}. Happy Exploring. Regards NKB Divine Vedic Sciences"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name1).replace("{$var2}", otp)

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": user_id,
        "data": {
            "var1": name1,
            "var2": otp
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
        "template_id": "195542032"
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







import requests
import json
import base64
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import GurujiUsers



def astro_login_otp(request):
    error_message = ""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        usd = GurujiUsers.objects.filter(email_id=user_id).last()
        user_name = GurujiUsers.objects.filter(whatsapp_no = user_id)
        for i in user_name:
            name1 = i.name
        
        if '@' in user_id:
            try:
                user = GurujiUsers.objects.get(email_id=user_id)
                recipient_numbers = user.whatsapp_no
                print('aparna',recipient_numbers)
            except GurujiUsers.DoesNotExist:
                user = None
        else:
            try:
                user = GurujiUsers.objects.get(whatsapp_no=user_id)
                recipient_numbers = user.whatsapp_no
            except GurujiUsers.DoesNotExist:
                user = None

        if user is not None and user.is_astrologer:
            # Generate OTP and store it in the session
            otp = get_random_string(length=6, allowed_chars='0123456789')
            request.session['login_otp'] = otp
            request.session['login_user_id'] = user_id

            # Send the OTP to the user's email
            subject = 'Login OTP'
            message = f"Dear user,\n\nYour OTP for login is: {otp}\n\nPlease enter this OTP to log in to your account.\n\nThank you!"
            send_mail(subject, message, 'jyotishjunction11@gmail.com', [user.email_id], fail_silently=False)

            # Send the SMS to the user's mobile number
            name = "User"  
            ase=recipient_numbers
            print('vdvvvvv',ase)
            # send_sms_otp([user_id],name1,otp) # You can replace "User" with the actual name if you have it

            # Redirect to OTP verification page
            return redirect('/otp-verification-astro/')
        else:
            error_message = 'Invalid user ID or email'

    return render(request, 'login/astro_otp_login.html', {'error_message': error_message})

































# def otp_verification_view_astro(request):
#     error_message = ""
#     if request.method == 'POST':
#         otp = request.POST.get('otp')
     
#         # Retrieve the OTP from the session
#         stored_otp = request.session.get('login_otp')

#         if otp == stored_otp:
#             # OTP verification successful
#             del request.session['login_otp']  # Remove the OTP from the session
           
#             user_id = request.session.get('login_user_id')
#             user = GurujiUsers.objects.get(email_id=user_id)
#             # user.backend = 'django.contrib.auth.backends.ModelBackend'
#             login(request, user)
#             # Perform additional logic or login the user as needed
#             return redirect('/dash_astro/')  # Redirect to the dashboard or desired page after successful login

#         error_message = 'Invalid OTP'

#     return render(request, 'login/otp_verification_astro.html', {'error_message': error_message})

# original


# def otp_verification_view_astro(request):
#     error_message = ""
    
#     if request.method == 'POST':
#         otp = request.POST.get('otp')
     
#         # Retrieve the OTP from the session
#         stored_otp = request.session.get('login_otp')

#         if otp == stored_otp:
#             # OTP verification successful
#             del request.session['login_otp']  # Remove the OTP from the session
           
#             user_id = request.session.get('login_user_id')
#             user = GurujiUsers.objects.get(whatsapp_no=user_id)
            
#             if user.is_approved:
#                 # If the user's is_approved field is True, then proceed with login
#                 # user.backend = 'django.contrib.auth.backends.ModelBackend'  # You may not need this line
#                 login(request, user)
#                 # Perform additional logic or login the user as needed
#                 return redirect('/dash_astro/')  # Redirect to the dashboard or desired page after successful login
#             else:
#                 error_message = "Your account is not approved yet. Please wait for approval."
#                 return render(request, 'login/otp_verification_astro.html', {'error_message': error_message})

#         else:
#             error_message = 'Invalid OTP'
    
#     return render(request, 'login/otp_verification_astro.html', {'error_message': error_message})




def otp_verification_view_astro(request):
    error_message = ""
    if request.method == 'POST':
        otp = request.POST.get('otp')
        # Retrieve the OTP from the session
        stored_otp = request.session.get('login_otp')

        if otp == stored_otp:
            # OTP verification successful
            del request.session['login_otp']  # Remove the OTP from the session
            user_id = request.session.get('login_user_id')
            user = GurujiUsers.objects.get(whatsapp_no=user_id)
            
            if user.is_approved:
                # If the user's is_approved field is True, then proceed with login
                # user.backend = 'django.contrib.auth.backends.ModelBackend'  # You may not need this line
                login(request, user)
                # Perform additional logic or login the user as needed
                return redirect('/dash_astro/')  # Redirect to the dashboard or desired page after successful login
            else:
                error_message = "Your account is not approved yet. Please wait for approval."
                return render(request, 'login/otp_verification_astro.html', {'error_message': error_message})
        else:
            error_message = 'Invalid OTP' 
    elif request.method == 'GET' and 'resend_otp' in request.GET:
        new_otp = str(random.randint(100000, 999999))  # Generate a new OTP
        print('new_otp',new_otp)
        user_id = request.session.get('login_user_id')
        user = GurujiUsers.objects.get(whatsapp_no=user_id)
        request.session['login_otp'] = new_otp  # Store the new OTP in the session
        otp = new_otp
        name = f"{user.first_name} {user.last_name}"
        # send_sms_otp([user_id],name,otp)
        
    
    return render(request, 'login/otp_verification_astro.html', {'error_message': error_message})



  
from Business_setting.models import BannerPost


def home_view(request):
    blog = BlogPost.objects.all()
    banner = BannerPost.objects.all()
    users_with_ratings = GurujiUsers.objects.exclude(Q(review_comments1='') | Q(review_star1='')).order_by('-id')[:3]
    for i in blog:
        print('kkkk',i.title)

    return render(request, 'login/home.html',{'blog':blog,'banner':banner, 'users':users_with_ratings })





def particular_customer_wallet(request):
    plan_id=request.session.get('plan_id')
    if plan_id:
        del request.session["plan_id"]
    recipient_numbers = request.user.whatsapp_no
    print('recipient_numbers',recipient_numbers)
    amount = 0
    if request.method == "POST":
        amount = request.POST.get('amount')
        amount = int(amount)
        url = reverse('customer-recharge',args=[amount])
        return redirect(url)
    plan = Plan_Purchase.objects.filter(cust_email_id=request.user.email_id)
    customer = GurujiUsers.objects.filter(is_customer=True)
    data = Wallet.objects.filter(cust_id = request.user.user_id).order_by('-plan_recharge_date')

    e_list = []
    e_list1 = []
    for i in data:
        debit = i.debit_amount
        total = i.recharge_amount
        e_list.append(total)
        e_list1.append(debit)
    
    # print('elistttttttttttttttt',e_list1)
    

    total_debit = 0
    for o in e_list1:
        if o:
            total_debit = float(o) + total_debit

    print('amountttttttttt',amount)
    
    total_amount = 0
    for a in e_list:
        if a: 
            total_amount= float(a) +float(total_amount)
    # print('tatolllllllll',total_amount)

    grand_debit= total_amount - total_debit

    

    

    plan_id = request.session.get('plan_id')
    context = {
        'plan': plan,
        'customer': customer,
        'amount': amount,
        'data' : data,
        'total_amount' : total_amount,
        "grand_debit":int(grand_debit),
        'plan_id':plan_id,
        
    }
    return render(request, 'login/customer_wallet.html', context)  
    # else:
    #     recipient_numbers = request.user.whatsapp_no
    #     print('recipient_numbers',recipient_numbers)

    #     amount = 0
    #     if request.method == "POST":
    #         amount = request.POST.get('amount')
    #         url = reverse('customer-recharge',args=[amount])
    #         return redirect(url)
    #     plan = Plan_Purchase.objects.filter(cust_email_id=request.user.email_id)
    #     customer = GurujiUsers.objects.filter(is_customer=True)
    #     data = Wallet.objects.filter(cust_id = request.user.user_id).order_by('-recharge_date')

    #     e_list = []
    #     e_list1 = []
    #     for i in data:
    #         debit = i.debit_amount
    #         total = i.recharge_amount
    #         e_list.append(total)
    #         e_list1.append(debit)
        
        
        

    #     total_debit = 0
    #     for o in e_list1:
    #         if o:
    #             total_debit = int(o) + total_debit

    #     print('amountttttttttt',amount)
        
    #     total_amount = 0
    #     for a in e_list:
    #         if a: 
    #             total_amount= int(a) +int(total_amount)
      

    #     grand_debit= total_amount - total_debit

    #     context = {
    #         'plan': plan,
    #         'customer': customer,
    #         'amount': amount,
    #         'data' : data,
    #         'total_amount' : total_amount,
    #         "grand_debit":grand_debit,
            
    #     }
    #     return render(request, 'login/customer-wallet-dollar.html', context)      
        






# def delete_customer(request):
#     guruji_user = GurujiUsers.objects.get(email_id='kurycuxi@mailinator.com')

#     # Delete entries from Plan_Purchase model
#     Plan_Purchase.objects.filter(cust_email_id=guruji_user).delete()

#     # Delete entries from Comment model
#     Comment.objects.filter(user=guruji_user).delete()

#     # Delete entries from Wallet model
#     Wallet.objects.filter(email_id=guruji_user).delete()

#     data = GurujiUsers.objects.filter(email_id = guruji_user).delete()

#     return redirect('/dash_customer/')



from django.shortcuts import redirect

def delete_customer(request):
    # Get a list of email IDs to delete
    email_ids_to_delete = ['abhit@gmail.com']

    # Loop through the list of email IDs and delete entries for each one
    for email_id in email_ids_to_delete:
        guruji_user = GurujiUsers.objects.filter(email_id=email_id).first()

        if guruji_user:
            # Delete entries from Plan_Purchase model
            Plan_Purchase.objects.filter(cust_email_id=guruji_user).delete()

            # Delete entries from Comment model
            Comment.objects.filter(user=guruji_user).delete()

            # Delete entries from Wallet model
            Wallet.objects.filter(email_id=guruji_user).delete()

            # Delete the GurujiUser entry
            guruji_user.delete()

    return redirect('/dash_customer/')

def customer_wallet(request):  

    recipient_numbers = request.user.whatsapp_no
    print('recipient_numbers',recipient_numbers)

    amount = 0
    if request.method == "POST":
        amount = request.POST.get('amount')  
        amount = int(amount)
        url = reverse('customer-recharge',args=[amount])
        return redirect(url)
    plan = Plan_Purchase.objects.filter(cust_email_id=request.user.email_id)
    customer = GurujiUsers.objects.filter(is_customer=True)
    data = Wallet.objects.filter(cust_id = request.user.user_id).order_by('-plan_recharge_date')

    e_list = []
    e_list1 = []
    for i in data:
        debit = i.debit_amount
        total = i.recharge_amount
        e_list.append(total)
        e_list1.append(debit)
    
    # print('elistttttttttttttttt',e_list1)
    

    total_debit = 0
    for o in e_list1:
        if o:
            total_debit = float(o) + total_debit

    print('amountttttttttt',amount)
    
    total_amount = 0
    for a in e_list:
        if a: 
            total_amount= float(a) +float(total_amount)
    # print('tatolllllllll',total_amount)

    grand_debit= total_amount - total_debit

    

    

    plan_id = request.session.get('plan_id')
    context = {
        'plan': plan,
        'customer': customer,
        'amount': amount,
        'data' : data,
        'total_amount' : total_amount,
        "grand_debit":int(grand_debit),
        'plan_id':plan_id,
        
    }
    return render(request, 'login/customer_wallet.html', context)  
    # else:
    #     recipient_numbers = request.user.whatsapp_no
    #     print('recipient_numbers',recipient_numbers)

    #     amount = 0
    #     if request.method == "POST":
    #         amount = request.POST.get('amount')
    #         url = reverse('customer-recharge',args=[amount])
    #         return redirect(url)
    #     plan = Plan_Purchase.objects.filter(cust_email_id=request.user.email_id)
    #     customer = GurujiUsers.objects.filter(is_customer=True)
    #     data = Wallet.objects.filter(cust_id = request.user.user_id).order_by('-recharge_date')

    #     e_list = []
    #     e_list1 = []
    #     for i in data:
    #         debit = i.debit_amount
    #         total = i.recharge_amount
    #         e_list.append(total)
    #         e_list1.append(debit)
        
    #     # print('elistttttttttttttttt',e_list1)
        

    #     total_debit = 0
    #     for o in e_list1:
    #         if o:
    #             total_debit = int(o) + total_debit

    #     print('amountttttttttt',amount)
        
    #     total_amount = 0
    #     for a in e_list:
    #         if a: 
    #             total_amount= int(a) +int(total_amount)
    #     # print('tatolllllllll',total_amount)

    #     grand_debit= total_amount - total_debit

    #     context = {
    #         'plan': plan,
    #         'customer': customer,
    #         'amount': amount,
    #         'data' : data,
    #         'total_amount' : total_amount,
    #         "grand_debit":grand_debit,
            
    #     }
    #     return render(request, 'login/customer-wallet-dollar.html', context)      
        



def customer_payment(request):
    amount = 0
    if request.method == "POST":
        amount = request.POST.get('amount')
        url = reverse('customer-recharge',args=[amount])
        return redirect(url)
    plan = Plan_Purchase.objects.filter(cust_email_id=request.user.email_id).order_by('-purchase_date')
    print('plannnnnnnnnnnnnn',plan)
    customer = GurujiUsers.objects.filter(is_customer=True)
    data = Wallet.objects.filter(cust_id = request.user.user_id).order_by('-recharge_time')

    e_list = []
    e_list1 = []
    for i in data:
        debit = i.debit_amount
        total = i.recharge_amount
        e_list.append(total)
        e_list1.append(debit)
    
    print('elistttttttttttttttt',e_list1)   
    

    total_debit = 0
    for o in e_list1:
        if o:
            total_debit = float(o) + total_debit

    print('elistttttttttttttttt',total_debit)
    
    total_amount = 0
    for a in e_list:
        if a: 
            total_amount= float(a) +float(total_amount)
    print('tatolllllllll',total_amount)

    grand_debit= total_amount - total_debit
    print('grand_debittttttttttttttttt',grand_debit)

    


    context = {
        'plan': plan,
        'customer': customer,
        'amount': amount,
        'data' : data,
        'total_amount' : total_amount,
        "grand_debit":grand_debit,
        
    }
    return render(request, 'login/customer-payment.html', context)


def plan_error_message(request):
    return render (request,'plan_error_message.html')

import time
# original
# def ask_question_silver(request):
#     data1 = GurujiUsers.objects.get(email_id = request.user.email_id)


#     data = admin_setting_plan.objects.all()
#     plan_name = ""
#     plan= admin_setting_plan.objects.get(plan_name_1=plan_name)
#     user = request.user.email_id
    
#     profile = GurujiUsers.objects.get( email_id=request.user.email_id)
#     data = {
#         'dob':profile.dob,
#         'age':profile.age,
#         'birth_place':profile.birth_place,
        
#         'city':profile.city,
#         'state':profile.state,
#         'pincode':profile.pincode,
#         'country':profile.country,
#     }
#     missing_keys = [key for key, value in data.items() if value is None]
#     all_values_present = not missing_keys
    

#     if request.method == 'POST':    
#         selected_question = request.POST.get('selectedQuestion')    
#         valu = request.POST.get('radioGroup')
#         user = request.user.email_id
#         user_comments = Comment.objects.filter(user=user,plan_name = "Personalized Guidance",plan_amount = "500",order_id = "").count()
#         piyush = generate_random_plan()
#         plan_id = piyush
#         # print("User:", user) 
#         # print("User Comments:", user_comments)
#         if user_comments < 1:
#             comment1 = request.POST.get('comment1', '') 
#             if selected_question:
#                 new_comment = Comment(plan_id = plan_id,object_id = request.user.user_id,ques_type = valu,comment1=selected_question, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
#                 new_comment.save()
#             elif comment1: 
#                 new_comment = Comment(plan_id = plan_id,object_id = request.user.user_id,ques_type = valu,comment1=comment1, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
#                 new_comment.save()
#         else:

#             return redirect('/plan_error_message/')  
#     comment_data = Comment.objects.filter(user = request.user.email_id,plan_name = "Personalized Guidance",order_id = "")
#     data2 = GurujiUsers.objects.filter(is_customer = True)
#     balance = Wallet.objects.filter(email_id = request.user.email_id)

#     e_list = []
#     e_list1 = []
#     for i in balance:
#         e_list.append(i.recharge_amount)
#         e_list1.append(i.debit_amount)
    
#     total_debit = 0
#     for o in e_list1:
#         if o:
#             total_debit = int(o) + int(total_debit)
    
#     cust_wallet = 0
#     for j in e_list:
#         if j:
#             cust_wallet = int(j)+ int(cust_wallet)

#     grand_debit = cust_wallet - total_debit
#     user = request.user.email_id
#     count = Comment.objects.filter(user=user,plan_name = "Personalized Guidance",plan_amount = "500",order_id = "").count()
#     question_left = 1 - count
#     # print('lllllllll',question_left,count)


#     return render(request, 'login/comment1.html', {'all_values_present': all_values_present,'missing_keys_string': ", ".join(missing_keys),'data': data,'data1': data1, 'data2':data2,'comment_data':comment_data,'cust_wallet':cust_wallet,'grand_debit':grand_debit,'question_left':question_left,'count':count,})



# working


# def ask_question_silver(request):
#     data1 = GurujiUsers.objects.get(email_id = request.user.email_id)


#     data = admin_setting_plan.objects.all()
#     plan_name = ""
#     plan= admin_setting_plan.objects.get(plan_name_1=plan_name)
    
#     user = request.user.email_id
    
#     profile = GurujiUsers.objects.get( email_id=request.user.email_id)
#     data = {
#         'dob':profile.dob,
#         'age':profile.age,
#         'birth_place':profile.birth_place,
        
#         'city':profile.city,
#         'state':profile.state,
#         'pincode':profile.pincode,
#         'country':profile.country,

#     }
#     missing_keys = [key for key, value in data.items() if value is None]
#     all_values_present = not missing_keys
        

#     if request.method == 'POST':  
#         selected_question = request.POST.get('selectedQuestion')    
#         valu = request.POST.get('radioGroup')
#         user = request.user.email_id
#         user_comments = Comment.objects.filter(user=user,plan_name = "Personalized Guidance",plan_amount = "500",order_id = "").count()
#         piyush = generate_random_plan()
#         plan_id = piyush
        
#         # print("User:", user) 
#         # print("User Comments:", user_comments)
#         if user_comments < 1:
#             comment1 = request.POST.get('comment1', '') 
#             if selected_question:
#                 new_comment = Comment(plan_id = plan_id,object_id = request.user.user_id,ques_type = valu,comment1=selected_question, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
#                 new_comment.save()
#             elif comment1: 
#                 new_comment = Comment(plan_id = plan_id,object_id = request.user.user_id,ques_type = valu,comment1=comment1, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
#                 new_comment.save()
#         else:

#             return redirect('/plan_error_message/')  
#     comment_data = Comment.objects.filter(user = request.user.email_id,plan_name = "",order_id = "")  
#     data2 = GurujiUsers.objects.filter(is_customer = True)
#     balance = Wallet.objects.filter(email_id = request.user.email_id)

#     e_list = []
#     e_list1 = []
#     for i in balance:
#         e_list.append(i.recharge_amount)
#         e_list1.append(i.debit_amount)
    
#     total_debit = 0
#     for o in e_list1:
#         if o:
#             total_debit = int(o) + int(total_debit)
    
#     cust_wallet = 0
#     for j in e_list:
#         if j:
#             cust_wallet = int(j)+ int(cust_wallet)
# @never_cache
#     grand_debit = cust_wallet - total_debit
#     user = request.user.email_id
#     count = Comment.objects.filter(user=user,plan_name = "",plan_amount = "500",order_id = "").count()
#     question_left = 1 - count
#     # print('lllllllll',question_left,count)

#     return render(request, 'login/comment1.html', {'all_values_present': all_values_present,
#         'missing_keys_string': ", ".join(missing_keys),'data': data,'data1': data1, 'data2':data2,'comment_data':comment_data,'cust_wallet':cust_wallet,'grand_debit':grand_debit,'question_left':question_left,'count':count})

def ask_question_silver(request):
    que_type = "Life"
    plan_count = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id).count()

    data1 = GurujiUsers.objects.get(email_id = request.user.email_id)
    piyush = generate_random_plan()
    plan_id = piyush


    data = admin_setting_plan.objects.all()
    plan_name = "Personalized Guidance"
    plan= admin_setting_plan.objects.get(plan_name_1=plan_name)

    
    user = request.user.email_id
    
    profile = GurujiUsers.objects.get( email_id=request.user.email_id)
    data = {
        'dob':profile.dob,
        # 'age':profile.age,
        'birth_place':profile.birth_place,
        
        # 'city':profile.city,
        # 'state':profile.state,
        # 'pincode':profile.pincode,
        # 'country':profile.country,

    }
    missing_keys = [key for key, value in data.items() if value is None]
    all_values_present = not missing_keys        

    if request.method == 'POST':  
        selected_question = request.POST.get('selectedQuestion')    
        valu = request.POST.get('radioGroup')
        
        user = request.user.email_id
        user_comments = Comment.objects.filter(user=user, plan_name="Personalized Guidance", plan_amount=0).count()

        if user_comments < 1:
            comment1 = request.POST.get('comment1', '')
            
            if selected_question:
                if plan_count == 0:
                    new_comment = Comment(plan_id=plan_id, object_id=request.user.user_id, ques_type=valu,
                                          comment1=selected_question, user=user, cust_name=f'{request.user.first_name} {request.user.last_name}',
                                          plan_name=plan_name, plan_amount=0)
                else:
                    new_comment = Comment(plan_id=plan_id, object_id=request.user.user_id, ques_type=valu,
                                          comment1=selected_question, user=user, cust_name=f'{request.user.first_name} {request.user.last_name}',
                                          plan_name=plan_name, plan_amount=plan.amount_plan)
            elif comment1:
                if plan_count == 0:
                    new_comment = Comment(plan_id=plan_id, object_id=request.user.user_id, ques_type=que_type,
                                          comment1=comment1, user=user, cust_name=f'{request.user.first_name} {request.user.last_name}',
                                          plan_name=plan_name, plan_amount=0)
                else:
                    new_comment = Comment(plan_id=plan_id, object_id=request.user.user_id, ques_type=que_type,
                                          comment1=comment1, user=user, cust_name=f'{request.user.first_name} {request.user.last_name}',
                                          plan_name=plan_name, plan_amount=plan.amount_plan)
            new_comment.save()

        else:
            return redirect('/plan_error_message/')  
    comment_data = Comment.objects.filter(user = request.user.email_id,plan_name = "Personalized Guidance",order_id = "")
    data2 = GurujiUsers.objects.filter(is_customer = True)
    balance = Wallet.objects.filter(email_id = request.user.email_id)

    e_list = []
    e_list1 = []
    for i in balance:
        e_list.append(i.recharge_amount)
        e_list1.append(i.debit_amount)
    
    total_debit = 0
    for o in e_list1:
        if o:
            total_debit = int(o) + int(total_debit)
    
    cust_wallet = 0
    for j in e_list:
        if j:
            cust_wallet = int(j)+ int(cust_wallet)

    grand_debit = cust_wallet - total_debit
    user = request.user.email_id
    count = Comment.objects.filter(user=user,plan_name = "Personalized Guidance").count()
    question_left = 1 - count
    print('lllllllll',question_left,count)
    
    if Comment.objects.filter(user=user,plan_name = "Personalized Guidance",plan_amount = "0",order_id = ""):
        data23 = Comment.objects.filter(user=user,plan_name = "Personalized Guidance",plan_amount = "0",order_id = "")
        for i in data23:
            plan_id = i.plan_id 
            request.session["plan_id"] = plan_id
    else:
        plan_id = piyush   
        request.session["plan_id"] = plan_id

    
    return render(request, 'login/comment1.html', {'all_values_present': all_values_present,
        'missing_keys_string': ", ".join(missing_keys),'plan_count':plan_count,'data': data,'data1': data1, 'data2':data2,'comment_data':comment_data,'cust_wallet':cust_wallet,'grand_debit':grand_debit,'question_left':question_left,'count':count})


def customer_support(request):
    return render (request,'login/customer_support.html')



def ask_q_silver(request,id):
    request.session['id']=id
    purchase_plan = Plan_Purchase.objects.get(id=id)
    data = admin_setting_plan.objects.all()
    plan_name = "Personalized Guidance"  
    user = request.user.email_id

    if request.method == 'POST':
        selected_question = request.POST.get('selectedQuestion')
        valu = request.POST.get('radioGroup')
        # print('selected_question',selected_question)
        user = request.user.email_id
        user_comments = Comment.objects.filter(user=user, order_id = purchase_plan.invoice_number).count()
        print("User:", user)
        print("User Comments:", user_comments)
        if user_comments < 2:
            comment1 = request.POST.get('comment1', '') 
            # valu = request.POST.get('valu')
            if selected_question:
                new_comment = Comment(plan_month = purchase_plan.plan_month,object_id = request.user.user_id,ques_type=valu,order_id = purchase_plan.invoice_number, comment1=selected_question, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount = purchase_plan.plan_amount, plan_purchase_date = purchase_plan.plan_purchase_date, plan_expiry_date = purchase_plan.plan_expiry_date)
                new_comment.save()
            elif comment1: 
                new_comment = Comment(plan_month = purchase_plan.plan_month,object_id = request.user.user_id,ques_type='Life',order_id = purchase_plan.invoice_number, comment1=comment1, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount = purchase_plan.plan_amount, plan_purchase_date = purchase_plan.plan_purchase_date, plan_expiry_date = purchase_plan.plan_expiry_date)
                new_comment.save()
        else:
            return redirect('/plan_error_message/')
        
        
    comment_data = Comment.objects.filter(user = request.user.email_id,plan_name = purchase_plan.plan_name, order_id = purchase_plan.invoice_number)
    print('11111111111111111111',comment_data)
    data2 = GurujiUsers.objects.filter(is_customer = True)
    user = request.user.email_id
    count = Comment.objects.filter(user=user,plan_name = "Personalized Guidance",plan_amount = "0",order_id = purchase_plan.invoice_number).count()
    question_left = 1 - count
    print('lllllllll',question_left,count)

    return render(request, 'login/comment4.html', {'data': data,'comment_data':comment_data, 'data2':data2, 'purchase_plan':purchase_plan,'question_left':question_left,'count':count})


def ques_app_silver(request,id):
    purchase_plan = Plan_Purchase.objects.get(id=id)
    plan_name = "Personalized Guidance"
    customer=request.user.email_id 
    comment=Comment.objects.filter(plan_name=plan_name,user=customer)
    print('comment',comment)
    for i in comment:
        if i.comment1:    
            print('ddddddddddddddd',i)
            i.que_approved=True
            i.save()

    admin_name = "Admin"  # Replace with the admin's name
    message = f"Dear {admin_name},\n\n"
    message += f"You have received a new Ask a Question from {purchase_plan.name} . Login to see details.\n\n"
    message += "Best Regards,\nTeam Jyotish Junction"
    send_mail(
        'New Question Asked by Jyotish Junction Customer',
        message,
        'jyotishjunction11@gmail.com',  # Replace with your email address
        ['jyotishjunction11@gmail.com'],  # Admin email address
        fail_silently=False,
    )
    user_message = f"Dear{request.user.first_name} {request.user.last_name},\n\n"
    user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
    user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
    user_message += "Warm Regards,\nTeam Jyotish Junction"
    send_mail(
        'Question has been received by us',
        user_message,
        'jyotishjunction11@gmail.com',  # Replace with your email address
        [request.user.email_id],  # User email address
        fail_silently=False,
    )
    return redirect('/dash_customer/')




def ques_app_gold(request,id):
    purchase_plan = Plan_Purchase.objects.get(id=id)
    plan_name = "Celestial Guidance"
    customer=request.user.email_id 
    comment=Comment.objects.filter(plan_name=plan_name,user=customer)
    print('comment',comment)
    for i in comment:
        if i.comment1:    
            print('ddddddddddddddd',i)
            i.que_approved=True
            i.send_admin = True
            i.save()
    admin_name = "Admin"  # Replace with the admin's name
    message = f"Dear {admin_name},\n\n"
    message += f"You have received a new Ask a Question from {purchase_plan.name} . Login to see details.\n\n"
    message += "Best Regards,\nTeam Jyotish Junction"
    send_mail(
        'New Question Asked by Jyotish Junction Customer',
        message,
        'jyotishjunction11@gmail.com',  # Replace with your email address
        ['jyotishjunction11@gmail.com'],  # Admin email address
        fail_silently=False,
    )
    user_message = f"Dear{request.user.first_name} {request.user.last_name},\n\n"
    user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
    user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
    user_message += "Warm Regards,\nTeam Jyotish Junction"
    send_mail(
        'Question has been received by us',
        user_message,
        'jyotishjunction11@gmail.com',  # Replace with your email address
        [request.user.email_id],  # User email address
        fail_silently=False,
    )
    
    return redirect('/dash_customer/')


def ques_app_platinum(request,id):
    purchase_plan = Plan_Purchase.objects.get(id=id)
    plan_name = "Divine Revelations"
    customer=request.user.email_id 
    comment=Comment.objects.filter(plan_name=plan_name,user=customer)
    print('comment',comment)
    for i in comment:
        if i.comment1:    
            print('ddddddddddddddd',i)
            i.que_approved=True
            i.send_admin = True
            i.save()
    admin_name = "Admin"  # Replace with the admin's name
    message = f"Dear {admin_name},\n\n"
    message += f"You have received a new Ask a Question from {purchase_plan.name} . Login to see details.\n\n"
    message += "Best Regards,\nTeam Jyotish Junction"
    send_mail(
        'New Question Asked by Jyotish Junction Customer',
        message,
        'jyotishjunction11@gmail.com',  # Replace with your email address
        ['jyotishjunction11@gmail.com'],  # Admin email address
        fail_silently=False,
    )
    user_message = f"Dear{request.user.first_name} {request.user.last_name},\n\n"
    user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
    user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
    user_message += "Warm Regards,\nTeam Jyotish Junction"
    send_mail(
        'Question has been received by us',
        user_message,
        'jyotishjunction11@gmail.com',  # Replace with your email address
        [request.user.email_id],  # User email address
        fail_silently=False,
    )
    return redirect('/dash_customer/')






def ask_question_gold(request):
    piyush = generate_random_plan()
    plan_id = piyush
    data = admin_setting_plan.objects.all()
    plan_name = "Celestial Guidance"
    plan= admin_setting_plan.objects.get(plan_name_1=plan_name)
    user = request.user.email_id
    
    profile = GurujiUsers.objects.get( email_id=request.user.email_id)
    data = {
        'dob':profile.dob,
        'age':profile.age,
        'birth_place':profile.birth_place,
        'city':profile.city,
        'state':profile.state,
        'pincode':profile.pincode,
        'country':profile.country,
    }
    missing_keys = [key for key, value in data.items() if value is None]
    all_values_present = not missing_keys
  
    if request.method == 'POST':
        selected_question = request.POST.get('selectedQuestion')
        valu = request.POST.get('radioGroup')
        user = request.user.email_id
        user_comments = Comment.objects.filter(user=user,plan_name = "Celestial Guidance",plan_amount = "2001",order_id = "").count()
        
        print("User:", user)
        print("User Comments:", user_comments)
        if user_comments < 5:
            comment1 = request.POST.get('comment1', '') 
            # valu = request.POST.get('valu')
            if selected_question:
                new_comment = Comment(plan_id = plan_id,object_id = request.user.user_id,ques_type=valu,comment1=selected_question, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
                new_comment.save()
            elif comment1: 
                new_comment = Comment(plan_id = plan_id,object_id = request.user.user_id,ques_type='Life',comment1=comment1, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
                new_comment.save()
        else:
            return redirect('/plan_error_message/')
    plan_name = "Celestial Guidance"
    customer=request.user.email_id 
    comment=Comment.objects.filter(plan_name=plan_name,user=customer)
    print('comment',comment)
    for i in comment:
        if i.comment1:
            print('ddddddddddddddd',i)
            i.que_approved=True
            i.save()
    comment_data = Comment.objects.filter(user = request.user.email_id,plan_name=plan_name,order_id = "")
    data2 = GurujiUsers.objects.filter(is_customer = True)
    balance = Wallet.objects.filter(email_id = request.user.email_id)

    e_list = []
    e_list1 = []
    for i in balance:
        e_list.append(i.recharge_amount)
        e_list1.append(i.debit_amount)
    
    total_debit = 0
    for o in e_list1:
        if o:
            total_debit = float(o) + float(total_debit)
    
    cust_wallet = 0
    for j in e_list:
        if j:
            cust_wallet = float(j)+ float(cust_wallet)

    grand_debit = cust_wallet - total_debit

    print('comment_data',comment_data)
    user_comments = Comment.objects.filter(user=user,plan_name = "Celestial Guidance",plan_amount = "2001",order_id = "").count()
    question_left= 5 - user_comments
    print('ggg',question_left)
    
    if Comment.objects.filter(user=user,plan_name = "Celestial Guidance",plan_amount = "2001",order_id = ""):
        data = Comment.objects.filter(user=user,plan_name = "Celestial Guidance",plan_amount = "2001",order_id = "")
        for i in data:
            plan_id = i.plan_id 
            request.session["plan_id"] = plan_id
    else:
        plan_id = piyush   
        request.session["plan_id"] = plan_id 

    return render(request, 'login/comment2.html', {'all_values_present': all_values_present,
        'missing_keys_string': ", ".join(missing_keys),'data': data,'comment_data':comment_data, 'data2':data2,'cust_wallet':cust_wallet,'grand_debit':grand_debit,'user_comments':user_comments,'question_left':question_left})




def ask_q_gold(request,id):
    request.session['id']=id
    purchase_plan = Plan_Purchase.objects.get(id=id)
    data = admin_setting_plan.objects.all()
    user = request.user.email_id
    
    profile = GurujiUsers.objects.get( email_id=request.user.email_id)
    data = {
        'dob':profile.dob,
        'age':profile.age,
        'birth_place':profile.birth_place,
        'city':profile.city,
        'state':profile.state,
        'pincode':profile.pincode,
        'country':profile.country,
    }
    missing_keys = [key for key, value in data.items() if value is None]
    all_values_present = not missing_keys
    plan_name = "Celestial Guidance" 
    ppp = ""
    jjj= ""
    if request.method == 'POST':
        selected_question = request.POST.get('selectedQuestion')
        valu = request.POST.get('radioGroup')
        user = request.user.email_id
        user_comments = Comment.objects.filter(user=user, order_id = purchase_plan.invoice_number).count()
        rrr = Comment.objects.filter(user=user, order_id = purchase_plan.invoice_number)
        for p in rrr:
            jjj = p.astro_name
            ppp = p.astro_email_id
        # print("User:", user)
        # print("User Comments:", user_comments)
        if user_comments < 6:
            comment1 = request.POST.get('comment1', '')
            # valu = request.POST.get('valu')
            print('fdsss',comment1) 
            if selected_question:
                new_comment = Comment(astro_name = jjj,astro_email_id = ppp,plan_month = purchase_plan.plan_month,object_id = request.user.user_id,ques_type=valu,order_id = purchase_plan.invoice_number, comment1=selected_question, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount = purchase_plan.plan_amount, plan_purchase_date = purchase_plan.plan_purchase_date, plan_expiry_date = purchase_plan.plan_expiry_date)
                new_comment.save()
            elif comment1: 
                new_comment = Comment(astro_name = jjj,astro_email_id = ppp,plan_month = purchase_plan.plan_month,object_id = request.user.user_id,ques_type='Life',order_id = purchase_plan.invoice_number, comment1=comment1, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount = purchase_plan.plan_amount, plan_purchase_date = purchase_plan.plan_purchase_date, plan_expiry_date = purchase_plan.plan_expiry_date)
                new_comment.save()
        else:
            return redirect('/plan_error_message/')
    comment_data = Comment.objects.filter(user = request.user.email_id,plan_name = purchase_plan.plan_name, order_id = purchase_plan.invoice_number)
    print('comment_data',comment_data)
    data2 = GurujiUsers.objects.filter(is_customer = True)
    user = request.user.email_id
    user_comments = Comment.objects.filter(user=user,plan_name = "Celestial Guidance",plan_amount = "2001",order_id = purchase_plan.invoice_number).count()
    question_left= 5 - user_comments
    print('ggg12221',question_left)

    return render(request, 'login/comment5.html', {'all_values_present':all_values_present,'missing_keys':missing_keys,'data': data,'comment_data':comment_data, 'data2':data2, 'purchase_plan':purchase_plan,'question_left':question_left,'user_comments':user_comments})



def ask_question_platinum(request):
    piyush = generate_random_plan()
    plan_id = piyush
    data = admin_setting_plan.objects.all()
    plan_name = "Divine Revelations"
    plan= admin_setting_plan.objects.get(plan_name_1=plan_name) 
    user = request.user.email_id
    
    profile = GurujiUsers.objects.get( email_id=request.user.email_id)
    data = {
        'dob':profile.dob,
        'age':profile.age,
        'birth_place':profile.birth_place,
        'city':profile.city,
        'state':profile.state,
        'pincode':profile.pincode,
        'country':profile.country,
    }
    missing_keys = [key for key, value in data.items() if value is None]
    all_values_present = not missing_keys

    if request.method == 'POST':
        if request.POST.get("fname"):
            cust_id = request.user.user_id
            fname = request.POST.get("fname")
            pname = "Divine Revelations"
            dob = request.POST.get("dob")
            gender = request.POST.get("gender")
            birth_time = request.POST.get("birth-time")
            birth_place = request.POST.get("birth-place")
            city = request.POST.get("city")
            state = request.POST.get("state")
            country_code = request.POST.get("country")
            try:
                country = pycountry.countries.get(alpha_2=country_code)
                if country:
                    country_full_name = country.name
            except:
                pass
            country = country_full_name
            data = Customer_profile(cust_id = cust_id,fname = fname,pname = pname,dob = dob,gender = gender,birth_time = birth_time,birth_place = birth_place,city = city,state = state,country = country)
            data.save()

        elif request.POST.get('selectedQuestion') or request.POST.get('comment1', '') :
            selected_question = request.POST.get('selectedQuestion')
            flex = request.POST.get('selected_option')
            valu = request.POST.get('radioGroup')
            # print('selected_question',valu)
            user = request.user.email_id
            user_comments = Comment.objects.filter(user=user,plan_name = "Divine Revelations", plan_amount = "6000", order_id = "").count()
            print('11111111111111111111',user_comments)
            
            # print("User:", user)
            # print("User Comments:", user_comments) 
            if user_comments < 10:
                comment1 = request.POST.get('comment1', '')
                # valu = request.POST.get('valu') 
                print('comment1',comment1)
                if selected_question:
                    new_comment = Comment(plan_id=plan_id,object_id = request.user.user_id,select_cust = flex, ques_type = valu,comment1=selected_question, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
                    new_comment.save()
                elif comment1: 
                    new_comment = Comment(plan_id=plan_id,object_id = request.user.user_id,select_cust = flex, ques_type = 'Life', comment1=comment1, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount=plan.amount_plan)
                    new_comment.save()
                # Generate the 4-digit order_id and save it in the database
            else:
                return redirect('/plan_error_message/')
            
        
    comment_data = Comment.objects.filter(user = request.user.email_id,plan_name = plan_name,order_id = "")
    data2 = GurujiUsers.objects.filter(is_customer = True)
    data3 = Customer_profile.objects.filter(cust_id = request.user.user_id).count()
    print('data3',data3)
    data4 = Customer_profile.objects.filter(cust_id = request.user.user_id)
    balance = Wallet.objects.filter(email_id = request.user.email_id)

    e_list = []
    e_list1 = []
    for i in balance:
        e_list.append(i.recharge_amount)
        e_list1.append(i.debit_amount)
    
    total_debit = 0
    for o in e_list1:
        if o:
            total_debit = float(o) + float(total_debit)
     
    cust_wallet = 0
    for j in e_list:
        if j:
            cust_wallet = float(j)+ float(cust_wallet)

    grand_debit = cust_wallet - total_debit
    user = request.user.email_id
    count = Comment.objects.filter(user=user,plan_name = "Divine Revelations", plan_amount = "6000", order_id = "").count()
    question_left = 10 - count
    
    if Comment.objects.filter(user=user,plan_name = "Divine Revelations",plan_amount = "6000",order_id = ""):
        data = Comment.objects.filter(user=user,plan_name = "Divine Revelations",plan_amount = "6000",order_id = "")
        for i in data:
            plan_id = i.plan_id 
            request.session["plan_id"] = plan_id
    else:
        plan_id = piyush
        request.session["plan_id"] = plan_id 


    # print('data4',data4[0])
    return render(request, 'login/comment3.html', {'all_values_present': all_values_present,'missing_keys_string': ", ".join(missing_keys),'data': data,'comment_data':comment_data, 'data2':data2,'count':count, 'data3':data3,'data4':data4,'cust_wallet':cust_wallet,'grand_debit':grand_debit,'question_left':question_left})



def ask_q_platinum(request,id):
    request.session['id']=id
    purchase_plan = Plan_Purchase.objects.get(id=id)
    data = admin_setting_plan.objects.all()
    plan_name = "Divine Revelations" 
    user = request.user.email_id
    
    profile = GurujiUsers.objects.get( email_id=request.user.email_id)
    data = {
        'dob':profile.dob,
        'age':profile.age,
        'birth_place':profile.birth_place,
        'city':profile.city,
        'state':profile.state,
        'pincode':profile.pincode,
        'country':profile.country,
    }
    missing_keys = [key for key, value in data.items() if value is None]
    all_values_present = not missing_keys
    ppp=""
    jjj=""
    if request.method == 'POST':
        selected_question = request.POST.get('selectedQuestion')
        flex = request.POST.get('selected_option')
        valu = request.POST.get('radioGroup')
        user = request.user.email_id
        user_comments = Comment.objects.filter(user=user, order_id = purchase_plan.invoice_number).count()
        # print("User:", user)
        # print("User Comments:", user_comments)
        if user_comments < 11:
            comment1 = request.POST.get('comment1', '') 
            # valu = request.POST.get('valu')
            rrr = Comment.objects.filter(user=user, order_id = purchase_plan.invoice_number)
            for p in rrr:
                jjj= p.astro_name
                ppp = p.astro_email_id
            if selected_question:
                new_comment = Comment(astro_name = jjj,astro_email_id = ppp,plan_month = purchase_plan.plan_month,object_id = request.user.user_id,select_cust=flex,ques_type=valu,order_id = purchase_plan.invoice_number ,comment1=selected_question, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount = purchase_plan.plan_amount, plan_purchase_date = purchase_plan.plan_purchase_date, plan_expiry_date = purchase_plan.plan_expiry_date)
                new_comment.save()
            elif comment1: 
                new_comment = Comment(astro_name = jjj,astro_email_id = ppp,plan_month = purchase_plan.plan_month,object_id = request.user.user_id,select_cust=flex,ques_type='Life',order_id = purchase_plan.invoice_number ,comment1=comment1, user=user,  cust_name = f'{request.user.first_name} {request.user.last_name}', plan_name = plan_name, plan_amount = purchase_plan.plan_amount, plan_purchase_date = purchase_plan.plan_purchase_date, plan_expiry_date = purchase_plan.plan_expiry_date)
                new_comment.save()
        else:
            return redirect('/plan_error_message/')
        
    comment_data = Comment.objects.filter(user = request.user.email_id,plan_name = purchase_plan.plan_name, order_id = purchase_plan.invoice_number)
    print('comment_data',request.user.user_id)
    data4 = Customer_profile.objects.filter(cust_id = request.user.user_id)
    print('comment_data',comment_data)
    data2 = GurujiUsers.objects.filter(is_customer = True)
    user = request.user.email_id
    count = Comment.objects.filter(user=user,plan_name = "Divine Revelations", plan_amount = "6000",order_id = purchase_plan.invoice_number).count()
    print('count',count)
    question_left = 10 - count
    return render(request, 'login/comment6.html', {'all_values_present': all_values_present,'missing_keys_string': ", ".join(missing_keys),'data4':data4,'data': data,'comment_data':comment_data, 'data2':data2, 'purchase_plan':purchase_plan,'question_left':question_left})




# live

# def order_histroy(request):
#     plan = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).order_by('-plan_purchase_time','-plan_purchase_date')
#     customer = GurujiUsers.objects.filter(is_customer=True)   
#     comment = Comment.objects.filter(user = request.user.email_id)
#     ddd = []

#     cust_set = set()

#     for p in plan:
#         for i in comment:
#             if p.invoice_number == i.order_id :
#                 if Comment.objects.filter(Q(order_id=p.invoice_number) & Q(qapprove=True) & ~Q(comment2 ='')).count():
#                     op = Comment.objects.filter(Q(order_id=p.invoice_number) & Q(qapprove=True) & ~Q(comment2 ='')).count()
#                     if i.plan_name =='Celestial Guidance' and op == 2001 :
#                         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
#                         cust_set.add(value)
#                     elif i.plan_name == "Divine Revelations" and op == 6000:
#                         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
#                         cust_set.add(value)
#                     elif i.plan_name == "Personalized Guidance" and op == 500:
#                         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
#                         cust_set.add(value)
#     cust_data = list(cust_set)
    
#     for p in cust_data:
#         print('hlklgfhlkrolktrhortlmhkrtlnm',p)

#     print(cust_data)
    
#     # Debugging: Print plan_name values
#     alist=[]
#     for p in plan:
#         for j in cust_data:  
#             op=0
#             if j[1] == p.invoice_number:
#                 final_data = Comment.objects.filter(order_id = p.invoice_number).last()
#                 op = Comment.objects.filter(Q(order_id=p.invoice_number) & Q(qapprove=True) & ~Q(comment2 ='')).count()
#                 ddd.append(final_data)
#                 alist.append(op)
#                 print('op',op,alist)
                
   
#     po = alist
#     new = zip(cust_data,po)
#     for a in plan:
#         for k,j in new:
#             if k[2] == "Celestial Guidance" and k[1] == a.invoice_number  and j == 5:
#                 print('pppppppppppppppppppppppppppp',k,j)
#     combined_data = zip(cust_data, po)

#     context = {
#         'plan':plan,
#         'customer': customer,
#         'plan':plan,
#         'cust_data':cust_data,
#         'ddd':ddd,
#         'alist':alist,
#         'combined_data':combined_data,
#     }
#     return render(request,'login/order_histroy.html',context)
   
# new


# rk

@login_required
@never_cache
def order_histroy(request):
    plan = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).order_by('-plan_purchase_time','-plan_purchase_date')
    customer = GurujiUsers.objects.filter(is_customer=True)   
    comment = Comment.objects.filter(user = request.user.email_id)
    ddd = []

    cust_set = set()

    for p in plan:
        for i in comment:
            if p.invoice_number == i.order_id :
                if Comment.objects.filter(Q(order_id=p.invoice_number) & Q(qapprove=True) & ~Q(comment2 ='')).count():
                    op = Comment.objects.filter(Q(order_id=p.invoice_number) & Q(qapprove=True) & ~Q(comment2 ='')).count()
                    if i.plan_name =='Celestial Guidance' and op == 5 :
                        value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
                        cust_set.add(value)
                    elif i.plan_name == "Divine Revelations" and op == 10:
                        value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
                        cust_set.add(value)
                    elif i.plan_name == "Personalized Guidance" and op == 1:
                        value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
                        cust_set.add(value)
    cust_data = list(cust_set)
    
    for p in cust_data:
        print('hlklgfhlkrolktrhortlmhkrtlnm',p)

    print(cust_data)
    
    # Debugging: Print plan_name values
    alist=[]
    for p in plan:
        for j in cust_data:  
            op=0
            if j[1] == p.invoice_number:
                final_data = Comment.objects.filter(order_id = p.invoice_number).last()
                op = Comment.objects.filter(Q(order_id=p.invoice_number) & Q(qapprove=True) & ~Q(comment2 ='')).count()
                ddd.append(final_data)
                alist.append(op)
                print('op',op,alist)
                
   
    po = alist
    new = zip(cust_data,po)
    for a in plan:
        for k,j in new:
            if k[2] == "Celestial Guidance" and k[1] == a.invoice_number  and j == 5:
                print('pppppppppppppppppppppppppppp',k,j)
    combined_data = zip(cust_data, po)

    context = {
        'plan':plan,
        'customer': customer,
        'plan':plan,
        'cust_data':cust_data,
        'ddd':ddd,
        'alist':alist,
        'combined_data':combined_data,
    }
    return render(request,'login/order_histroy.html',context)







def delete_question_silver(request,id):
    data = Comment.objects.get(id = id)
    data.delete()
    return redirect("/ask_question_silver/")



def delete_question_gold(request,id):
    data = Comment.objects.get(id = id)
    data.delete()
    return redirect("/ask_question_gold/")



def delete_question_platinum(request,id):
    data = Comment.objects.get(id = id)
    data.delete()
    return redirect("/ask_question_platinum/")





def delete_que_platinum(request, id_value, plan_value):
    purchase_plan = Plan_Purchase.objects.get(id=plan_value)
    ddd = purchase_plan.id
    data = Comment.objects.get(id = id_value)
    data.delete()
    url = reverse('ask_q_platinum', args=[ddd]) 
    return redirect(url)




def delete_que_gold(request, id_value, plan_value):
    purchase_plan = Plan_Purchase.objects.get(id=plan_value)
    ddd = purchase_plan.id
    data = Comment.objects.get(id = id_value)
    data.delete()
    url = reverse('ask_q_gold', args=[ddd]) 
    return redirect(url)




def delete_que_silver(request, id_value, plan_value):
    purchase_plan = Plan_Purchase.objects.get(id=plan_value)
    ddd = purchase_plan.id
    data = Comment.objects.get(id = id_value)
    data.delete()
    url = reverse('ask_q_silver', args=[ddd]) 
    return redirect(url)




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
            error_message = 'Invalid user ID, email, or password'

    return render(request, 'login/admin_login.html', {'error_message': error_message})


from django.http import HttpResponseRedirect




from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.shortcuts import redirect, render


def otp_login_sms(user_id,name,otp):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name
    var2 = otp # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Greetings {$var1}, We have received your request for onboarding at NKB Divine Vedic Sciences platform. We will get back to you soon."

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name).replace("{$var2}", otp)
    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
    # print("var1:", var1)
    print("message_template:", message_template)
    print("message:", message)

    # Prepare the payload  
    payload = {
        "from": sender_id,
        "to": user_id,
        "data": {
            "var1": name,
            "var2": otp
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
        "template_id": "195542032"
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



# def customer_login_otp(request):
#     error_message = ""
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_name = GurujiUsers.objects.filter(whatsapp_no = user_id)
#         for i in user_name:
#             i.first_name
#             i.last_name
#             name = i.first_name + " " + i.last_name
#     	# print('llllll',name)

#         # Check if user_id is an email
#         if '@' in user_id:
#             try:
#                 user = GurujiUsers.objects.get(email_id=user_id)
#                 print('llllll',user)
#             except GurujiUsers.DoesNotExist:
#                 user = None
#         else:
#             try:
#                 user = GurujiUsers.objects.get(whatsapp_no=user_id)
#             except GurujiUsers.DoesNotExist:
#                 user = None

#         if user is not None and user.is_customer:
#             # Generate OTP and store it in the session  
#             otp = get_random_string(length=6, allowed_chars='0123456789')
#             request.session['login_otp'] = otp   
#             print('otp',otp)
#             request.session['login_user_id'] = user_id

#             # Send the OTP to the user's email
#             subject = 'Login OTP'
#             message = f"Dear user,\n\nYour OTP for login is: {otp}\n\nPlease enter this OTP to log in to your account.\n\nThank you!"
#             message = render_to_string('login/otp_email.html', {'otp': otp})
#             print('aparna',message)
#             send_mail(subject, message, 'your-email@example.com', [user.email_id], fail_silently=False)

#             otp_login_sms([user_id],name,otp)


#             # Redirect to OTP verification page
#             return redirect('/otp-verification/')
#         else:
#             error_message = 'Invalid Phone Number'

#     return render(request, 'login/customer_otp_login.html', {'error_message': error_message})


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string

def customer_login_otp(request):
    error_message = ""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_name = GurujiUsers.objects.filter(email_id=user_id).first()
        name = user_name.first_name + " " + user_name.last_name if user_name else ""

        # Check if user_id is an email
        if '@' in user_id:
            try:
                user = GurujiUsers.objects.get(email_id=user_id)
            except GurujiUsers.DoesNotExist:
                user = None
        else:
            try:
                user = GurujiUsers.objects.get(whatsapp_no=user_id)
            except GurujiUsers.DoesNotExist:
                user = None

        if user_name is None:
            # User is not registered, set an error message
            error_message = "User is not registered. Please sign up first."


        elif user is not None and user.is_customer:
            # Generate OTP and store it in the session
            otp = get_random_string(length=6, allowed_chars='0123456789')
            request.session['login_otp'] = otp
            request.session['login_user_id'] = user_id

            # Send the OTP to the user's email
            subject = 'Login OTP'
            message = f"Dear {name},\n\nYour OTP for login is: {otp}\n\nPlease enter this OTP to log in to your account.\n\nThank you!"

            send_mail(subject,message, 'your-email@example.com', [user.email_id], fail_silently=False)

            return redirect('/otp_verification_before/')

        else:
            error_message = 'Invalid Email Id'

    return render(request, 'login/customer_otp_login.html', {'error_message': error_message})



from django.contrib.auth import logout
from django.http import JsonResponse

def logout_customer(request):
    if request.user.is_authenticated:
        if request.user.is_astrologer:
            pass
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})





def logout_astrologer(request): 
        # if request.user.is_customer:
        #     pass
        logout(request)
        return HttpResponseRedirect('/astrologer-login/') 
        


import secrets
import string   
def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

import secrets
import string   
def generate_random_password11(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))




from django.views.decorators.csrf import csrf_exempt


def forgotsuccess(request):
        user_id = request.POST.get('user_id')
        print('1111111111111111111111',user_id)
        if request.user.is_authenticated and request.user.is_admin:
            return redirect('/admin-login/')
        elif request.user.is_authenticated and request.user.is_astrologer:
            return redirect('/astrologer-login/')
        elif request.user.is_authenticated and request.user.is_user:
            return redirect('/customer-login/')

        return render(request, 'login/forgotpass.html')


from django.contrib.auth.hashers import check_password
import re


# def changepass(request):
#     print(request.user.email_id)
#     error_message = ''
#     message = ''
#     print(request.user.email_id)
#     data = GurujiUsers.objects.get(email_id=request.user.email_id)
#     print('data', data)
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         password = request.POST.get('password')
#         new_pass1 = request.POST.get('new_pass1')
#         new_pass2 = request.POST.get('new_pass2')

#         if new_pass1 and new_pass2:
#             if new_pass1 != new_pass2:
#                 error_message = 'Passwords do not match.'
#             elif len(new_pass1) < 8:
#                 error_message = 'Password must be at least 8 characters long.'
#             elif len(new_pass1) > 100:
#                 error_message = 'Password cannot exceed 100 characters.'    
#             elif not re.match(r'^(?=.*[a-zA-Z])(?=.*[@!#$])(?=.*[0-9])[a-zA-Z0-9@!#$]{8,}$', new_pass1):
#               error_message = 'Password must contain lowercase and uppercase letters (a to z or A to Z), numbers (0 to 9), and at least one of the symbols @, !, #, or $.'
#             else:
#                 user = GurujiUsers.objects.get(user_id=request.user.user_id)
#                 check_password(password, user.password)
#                 user.password = make_password(new_pass1)
#                 user.save()
#                 message = 'Password updated successfully.'
#                 if request.user.is_customer:
#                     return redirect('/customer-login/')
#                 if request.user.is_admin:
#                     return redirect('/admin-login/')
#                 if request.user.is_astrologer:
#                     return redirect('/astrologer-login/')
#     return render(request, 'login/changepass.html', {'error_message': error_message, 'message': message})

from django.contrib.auth.forms import PasswordChangeForm
@login_required
@never_cache
def changepass(request):
    error_message = ''
    message = ''
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/customer-login/')
    else:
        fm = PasswordChangeForm(user=request.user)    
    return render(request, 'login/changepass.html', {'form':fm,'error_message': error_message, 'message': message})






# def changepass(request):
#     error_message = ''
#     message = ''

#     if request.method == 'POST':
#         #  form = PasswordChangeForm(request.POST)
#         #     if form.is_valid():
#             user_id = request.user.user_id
#             password = request.POST.get('password')
#             new_pass1 = request.POST.get('new_pass1')
#             new_pass2 = request.POST.get('new_pass2')
#             print("mmm",user_id,password,new_pass1)

#             # Validate passwords and check old password
#             if new_pass1 != new_pass2:
#                 error_message = 'Passwords do not match.'
#             elif len(new_pass1) < 8:
#                 error_message = 'Password must be at least 8 characters long.'
#             elif len(new_pass1) > 100:
#                 error_message = 'Password cannot exceed 100 characters.'
#             elif not re.match(r'^(?=.*[a-zA-Z])(?=.*[@!#$])(?=.*[0-9])[a-zA-Z0-9@!#$]{8,}$', new_pass1):
#                 error_message = 'Password must contain lowercase and uppercase letters, numbers, and at least one of the symbols @, !, #, or $.'
#             else:
#                 user = GurujiUsers.objects.get(user_id=user_id)
#                 if not check_password(password, user.password):
#                     error_message = 'Your old password is incorrect.'
#                 else:
#                     user.password = make_password(new_pass1)
#                     user.save()
#                     message = 'Password updated successfully.'
#                     if user.is_customer:
#                         return redirect('/customer-login/')
#                     if user.is_admin:
#                         return redirect('/admin-login/')
#                     if user.is_astrologer:
#                         return redirect('/astrologer-login/')
#     else:
#         form = PasswordChangeForm(initial={'user_id': request.user.user_id})

#     return render(request, 'login/changepass.html', { 'error_message': error_message, 'message': message})






def plan(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        plan_name_1 = request.POST.get('plan_name_1')
        admin_plan_1_d = request.POST.get('admin_plan_1_d')    
        amount_plan = request.POST.get('amount_plan')
        plan_data = admin_setting_plan(
            plan_name_1=plan_name_1,
            admin_plan_1_d=admin_plan_1_d,
            amount_plan = amount_plan
        )
        plan_data.save()
    data= admin_setting_plan.objects.all()
    return render (request, 'login/plan.html',{'data':data})






import random
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import razorpay
import pytz
import datetime
from datetime import datetime  # Import only 'datetime' class from the 'datetime' module
import pytz
import random
import razorpay






def send_sms_package_silver(recipient_numbers,name,var2):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Hello {$var1}, Thank you for selecting the {$var2} package. You can now ask your question to our expert astrologers. Regards NKB Divine Vedic Sciences"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name).replace("{$var2}", var2)

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": recipient_numbers,
        "data": {
            "var1": name,
            "var2":var2,
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
        "template_id": "568600729"
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







def send_sms_package_gold(recipient_numbers,name,var2):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Dear {$var1}, Congratulations on selecting the {$var2} package. You have 30 days to avail of all the features. Enjoy your astrology journey. Regards NKB Divine"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name).replace("{$var2}", var2)

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": recipient_numbers,
        "data": {
            "var1": name,
            "var2":var2,
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
        "template_id": "471214560"
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











def send_sms_package_platinum(recipient_numbers,name,var2):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Dear {$var1}, Congratulations on selecting the {$var2} package. You have 30 days to avail of all the features. Enjoy your astrology journey. Regards NKB Divine"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", name).replace("{$var2}", var2)

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": recipient_numbers,
        "data": {
            "var1": name,
            "var2":var2,
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
        "template_id": "471214560"
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







# oriinal

# @csrf_exempt
# def comment_view(request):

#     recipient_numbers=request.user.whatsapp_no
#     name= request.user.first_name
    
#     # print('data',recipient_numbers)
#     # print('name',name)
#     # print('ddddddddddddddd',request.user.first_name)



#     current_datetime_utc = datetime.now(pytz.utc)
#     # Convert the datetime to the Indian time zone
#     timezone = pytz.timezone('Asia/Kolkata')
#     current_datetime = current_datetime_utc.astimezone(timezone)
#     current_date = current_datetime.date()
#     # current_time = current_datetime.time()
#     current_time = current_datetime.time().strftime('%H:%M:%S')
#     formatted_date = current_date.strftime('%d-%m-%Y')
#     # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
#     date_obj = datetime.strptime(formatted_date, '%d-%m-%Y')
#     # Get the month in alphabetic format
#     month_alphabetic = date_obj.strftime('%B')
#     # print(month_alphabetic)
#     invoice_number = random.randint(10000, 99999)
#     # print("Random Invoice Number:", invoice_number)
#     plan = admin_setting_plan.objects.get(plan_name_1='Personalized Guidance')
#     amount = int(plan.amount_plan)
#     gst = (amount * 9)/100
#     total_amount =int(amount + (gst*2))
#     currency = 'INR'
#     client = razorpay.Client(auth=("rzp_test_Ey7h721E1o2LY1", "AwU7kngK8eCZK9Ztqd02brOy"))
#     payment = client.order.create({'amount': total_amount * 100, 'currency': 'INR', 'payment_capture': '1'})
#     razorpay_order_id = payment['id']
#     razorpay_payment_id = payment['receipt']
#     balance = Wallet.objects.filter(email_id = request.user.email_id)
#     transaction_id = generate_random_transaction_id()
#     e_list = []
#     for i in balance:
#         e_list.append(i.recharge_amount)
#     cust_wallet = 0
#     for j in e_list:
#         if j: 
#             cust_wallet = int(j)+ int(cust_wallet)
#     remaining = cust_wallet - int(total_amount)


#     if request.method == 'POST':
#         if cust_wallet >= total_amount:
#             done = Plan_Purchase(
#             invoice_number = invoice_number,
#             plan_order_id=razorpay_order_id,
            
#             name = f'{request.user.first_name} {request.user.last_name}',
#             cust_id=request.user.user_id,
#             cust_email_id=request.user.email_id,
#             cust_whatsapp_no=request.user.whatsapp_no,
#             cgst = gst,
#             sgst = gst,
#             total_amount = total_amount,
#             questions_count = plan.admin_plan_1_d,
#             plan_purchase_time = current_time,
#             plan_name=plan.plan_name_1,
#             plan_amount=plan.amount_plan,
#             plan_purchase_date = formatted_date,
#             purchase_time = current_datetime,
#             plan_month=month_alphabetic,
#             )   
#             done.save()
#             wallet = Wallet(
#                 cust_id = request.user.user_id,
#                 name = f'{request.user.first_name} {request.user.last_name}',
#                 email_id=request.user.email_id,
#                 whatsapp_no=request.user.whatsapp_no,
#                 recharge_time = current_time,
#                 recharge_date= formatted_date,
#                 debit_amount = total_amount,
#                 wallet_month = month_alphabetic, 
#                 transaction_id = transaction_id,
#             )
#             wallet.save()
        
        	

#         plan_name = "Personalized Guidance"
#         customer=request.user.email_id 
#         comment=Comment.objects.filter(plan_name=plan_name,user=customer,order_id = '')
#         # print('comment',comment)
#         for i in comment:
#             if i.comment1:
#                 print('ddddddddddddddd',i)
#                 i.order_id = invoice_number
#                 i.customer_to_admin_time=current_time
#                 i.plan_purchase_date=formatted_date
#                 i.plan_month = month_alphabetic
#                 i.send_admin = True
#                 i.save()
#         return redirect('/dash_customer1/')
#     # print('dddddddddddd',razorpay_order_id,razorpay_payment_id,total_amount,amount )
#     # admin_name = "Admin"
#     # customer_id = "{{request.user.first_name}} {{request.user.last_name}}"
#     # message = f"Dear {admin_name},\n\n"
#     # message += f"You have received a new Ask a Question from {request.user.first_name} {request.user.last_name}  . Login to see details.\n\n"
#     # message += "Best Regards,\nTeam Jyotish Junction"
#     # send_mail(
#     #     'New Question Asked by Jyotish Junction Customer',
#     #     message,
#     #     'jyotishjunction11@gmail.com',  
#     #     ['jyotishjunction11@gmail.com'],  
#     #     fail_silently=False,
#     # )

#     # user_message = f"Dear  {request.user.first_name} {request.user.last_name},\n\n"
#     # user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
#     # user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
#     # user_message += "Warm Regards,\nTeam Jyotish Junction"
#     # send_mail( 
#     #     'Question has been received by us',
#     #     user_message,
#     #     'jyotishjunction11@gmail.com',   
#     #     [request.user.email_id],  
#     #     fail_silently=False,
#     # )

#     # send_sms_package_silver([recipient_numbers],name,'Personalized Guidance')


    

    


#     context = {
#         'razorpay_order_id': razorpay_order_id,
#         'razorpay_merchant_key': 'rzp_test_Ey7h721E1o2LY1',
#         'razorpay_amount': amount,
#         'gst':gst, 
#         'currency': currency,
#         'plan':plan, 
#         'total_amount':int(total_amount), 
#         'current_date':current_date,
#         'current_time':current_time,
#         'cust_wallet':cust_wallet,
#         'remaining':remaining,
#     }
#     return render(request, 'login/index.html', context=context)

# live
# @csrf_exempt
# def comment_view(request):

#     recipient_numbers=request.user.whatsapp_no
#     name= request.user.first_name
    
#     # print('data',recipient_numbers)
#     # print('name',name)
#     # print('ddddddddddddddd',request.user.first_name)



#     current_datetime_utc = datetime.now(pytz.utc)
#     # Convert the datetime to the Indian time zone
#     timezone = pytz.timezone('Asia/Kolkata')
#     current_datetime = current_datetime_utc.astimezone(timezone)
#     current_date = current_datetime.date()
#     # current_time = current_datetime.time()
#     current_time = current_datetime.time().strftime('%H:%M:%S')
#     formatted_date = current_date.strftime('%d-%m-%Y')
#     # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
#     date_obj = datetime.strptime(formatted_date, '%d-%m-%Y')
#     # Get the month in alphabetic format
#     month_alphabetic = date_obj.strftime('%B')
#     # print(month_alphabetic)
#     invoice_number = random.randint(10000, 99999)
#     # print("Random Invoice Number:", invoice_number)
#     plan = admin_setting_plan.objects.get(plan_name_1='Personalized Guidance')
#     amount = int(plan.amount_plan)
#     gst = (amount * 9)/100
#     total_amount =int(amount + (gst*2))
#     currency = 'INR'
#     client = razorpay.Client(auth=("rzp_test_Ey7h721E1o2LY1", "AwU7kngK8eCZK9Ztqd02brOy"))
#     payment = client.order.create({'amount': total_amount * 100, 'currency': 'INR', 'payment_capture': '1'})
#     razorpay_order_id = payment['id']
#     razorpay_payment_id = payment['receipt']
#     balance = Wallet.objects.filter(email_id = request.user.email_id)
#     transaction_id = generate_random_transaction_id()
#     e_list = []
#     for i in balance:
#         e_list.append(i.recharge_amount)
#     cust_wallet = 0
#     for j in e_list:
#         if j: 
#             cust_wallet = int(j)+ int(cust_wallet)
#     remaining = cust_wallet - int(total_amount)


#     if request.method == 'POST':
#         if cust_wallet > total_amount:
#             done = Plan_Purchase(
#             invoice_number = invoice_number,
#             plan_order_id=razorpay_order_id,
            
#             name = f'{request.user.first_name} {request.user.last_name}',
#             cust_id=request.user.user_id,
#             cust_email_id=request.user.email_id,
#             cust_whatsapp_no=request.user.whatsapp_no,
#             cgst = gst,
#             sgst = gst,
#             total_amount = total_amount,
#             questions_count = plan.admin_plan_1_d,
#             plan_purchase_time = current_time,
#             plan_name=plan.plan_name_1,
#             plan_amount=plan.amount_plan,
#             plan_purchase_date = formatted_date,
#             purchase_time = current_datetime,
#             plan_month=month_alphabetic,
#             )   
#             done.save()
#             wallet = Wallet(
#                 cust_id = request.user.user_id,
#                 name = f'{request.user.first_name} {request.user.last_name}',
#                 email_id=request.user.email_id,
#                 whatsapp_no=request.user.whatsapp_no,
#                 recharge_time = current_time,
#                 recharge_date= formatted_date,
#                 debit_amount = total_amount,
#                 wallet_month = month_alphabetic, 
#                 transaction_id = transaction_id,
#             )
#             wallet.save()
        
        	

#         plan_name = "Personalized Guidance"
#         customer=request.user.email_id 
#         comment=Comment.objects.filter(plan_name=plan_name,user=customer,order_id = '')
#         # print('comment',comment)
#         for i in comment:
#             if i.comment1:
#                 print('ddddddddddddddd',i)
#                 i.order_id = invoice_number
#                 i.customer_to_admin_time=current_time
#                 i.plan_purchase_date=formatted_date
#                 i.plan_month = month_alphabetic
#                 i.send_admin = True
#                 i.save()
#         return redirect('/dash_customer1/')
#     # print('dddddddddddd',razorpay_order_id,razorpay_payment_id,total_amount,amount )
#     # admin_name = "Saurabh Tyagi"
#     # customer_id = "{{request.user.first_name}} {{request.user.last_name}}"
#     # message = f"Dear {admin_name},\n\n"
#     # message += f"You have received a new Ask a Question from {request.user.first_name} {request.user.last_name}  . Login to see details.\n\n"
#     # message += "Best Regards,\nTeam Jyotish Junction"
#     # send_mail(
#     #     'New Question Asked by Jyotish Junction Customer',
#     #     message,
#     #     'jyotishjunction11@gmail.com',  
#     #     ['pbambulkar9924@gmail.com'],  
#     #     fail_silently=False,
#     # )

#     # user_message = f"Dear  {request.user.first_name} {request.user.last_name},\n\n"
#     # user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
#     # user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
#     # user_message += "Warm Regards,\nTeam Jyotish Junction"
#     # send_mail( 
#     #     'Question has been received by us',
#     #     user_message,
#     #     'jyotishjunction11@gmail.com',   
#     #     [request.user.email_id],  
#     #     fail_silently=False,
#     # )

#     # send_sms_package_silver([recipient_numbers],name,'Personalized Guidance')


    

    


#     context = {
#         'razorpay_order_id': razorpay_order_id,
#         'razorpay_merchant_key': 'rzp_test_Ey7h721E1o2LY1',
#         'razorpay_amount': amount,
#         'gst':gst, 
#         'currency': currency,
#         'plan':plan, 
#         'total_amount':int(total_amount), 
#         'current_date':current_date,
#         'current_time':current_time,
#         'cust_wallet':cust_wallet,
#         'remaining':remaining,
#     }
#     return render(request, 'login/index.html', context=context)   


@csrf_exempt



def comment_view(request):
    plan_count = Plan_Purchase.objects.filter(cust_email_id=request.user.email_id).count()

    recipient_numbers = request.user.whatsapp_no
    name = request.user.first_name

    current_datetime_utc = datetime.now(pytz.utc)
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    formatted_date = current_date.strftime('%d-%m-%Y')
    month_alphabetic = current_date.strftime('%B')
    invoice_number = random.randint(10000, 99999)

    try:
        plan = admin_setting_plan.objects.get(plan_name_1='Personalized Guidance')
    except admin_setting_plan.DoesNotExist:
        plan = None

    currency = 'INR'
    balance = Wallet.objects.filter(email_id=request.user.email_id)
    transaction_id = generate_random_transaction_id()

    if plan_count == 0 and plan:
        if hasattr(plan, 'amount_plan') and hasattr(plan, 'admin_plan_1_d'):
            amount = int(plan.amount_plan)
            gst = (amount * 9) / 100
            total_amount = int(amount + (gst * 2))
            questions_count = plan.admin_plan_1_d
        else:
            amount = 0
            gst = 0
            total_amount = 0
            questions_count = 0
    else:
        total_amount = 0
        amount = 0
        gst = 0
        questions_count = 0

    e_list = [i.recharge_amount for i in balance if i.recharge_amount]
    cust_wallet = sum(map(int, e_list))
    remaining = cust_wallet - int(total_amount)

    if request.method == 'POST':
        if cust_wallet > total_amount and plan_count != 0 and plan:
            done = Plan_Purchase(
                invoice_number=invoice_number,
                name=f'{request.user.first_name} {request.user.last_name}',
                cust_id=request.user.user_id,
                cust_email_id=request.user.email_id,
                cust_whatsapp_no=request.user.whatsapp_no,
                cgst=gst,
                sgst=gst,
                total_amount=total_amount,
                questions_count=questions_count,
                plan_purchase_time=current_time,
                plan_name=plan.plan_name_1 if hasattr(plan, 'plan_name_1') else 'Personalized Guidance',
                plan_amount=plan.amount_plan,
                plan_purchase_date=formatted_date,
                purchase_time=current_datetime,
                plan_month=month_alphabetic,
            )
            done.save()
        else:
            done = Plan_Purchase(
                invoice_number=invoice_number,
                name=f'{request.user.first_name} {request.user.last_name}',
                cust_id=request.user.user_id,
                cust_email_id=request.user.email_id,
                cust_whatsapp_no=request.user.whatsapp_no,
                cgst=gst,
                sgst=gst,
                total_amount=total_amount,
                questions_count=questions_count,
                plan_purchase_time=current_time,
                plan_name='Personalized Guidance',
                plan_amount=0,  # Set plan_amount to 0
                plan_purchase_date=formatted_date,
                purchase_time=current_datetime,
                plan_month=month_alphabetic,
            )
            done.save()

        wallet = Wallet(
            cust_id=request.user.user_id,
            name=f'{request.user.first_name} {request.user.last_name}',
            email_id=request.user.email_id,
            whatsapp_no=request.user.whatsapp_no,
            recharge_time=current_time,
            recharge_date=formatted_date,
            debit_amount=total_amount,
            wallet_month=month_alphabetic,
            transaction_id=transaction_id,
        )
        wallet.save()

        plan_name = "Personalized Guidance"
        customer = request.user.email_id
        comment = Comment.objects.filter(plan_name=plan_name, user=customer, order_id='')
        for i in comment:
            if i.comment1:
                i.order_id = invoice_number
                i.customer_to_admin_time = current_time
                i.plan_purchase_date = formatted_date
                i.plan_month = month_alphabetic
                i.send_admin = True
                i.save()
        return redirect('/dash_customer1/')

    context = {
        'gst': gst,
        'currency': currency,
        'plan': plan,
        'total_amount': int(total_amount),
        'current_date': current_date,
        'current_time': current_time,
        'cust_wallet': cust_wallet,
        'remaining': remaining,
    }

    if plan_count != 0:
        context['total_amount'] = int(total_amount)
    else:
        context['total_amount'] = 0

    return render(request, 'login/index.html', context=context)


    # else:
    #     recipient_numbers=request.user.whatsapp_no
    #     name= request.user.first_name
        
    #     # print('data',recipient_numbers)
    #     # print('name',name)
    #     # print('ddddddddddddddd',request.user.first_name)



    #     current_datetime_utc = datetime.now(pytz.utc)
    #     # Convert the datetime to the Indian time zone
    #     timezone = pytz.timezone('Asia/Kolkata')
    #     current_datetime = current_datetime_utc.astimezone(timezone)
    #     current_date = current_datetime.date()
    #     # current_time = current_datetime.time()
    #     current_time = current_datetime.time().strftime('%H:%M:%S')
    #     formatted_date = current_date.strftime('%d-%m-%Y')
    #     # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
    #     date_obj = datetime.strptime(formatted_date, '%d-%m-%Y')
    #     # Get the month in alphabetic format
    #     month_alphabetic = date_obj.strftime('%B')
    #     # print(month_alphabetic)
    #     invoice_number = random.randint(10000, 99999)
    #     # print("Random Invoice Number:", invoice_number)
    #     plan = admin_setting_plan_dollar.objects.get(plan_name_1='Personalized Guidance')
    #     amount = int(plan.amount_plan)
    #     gst = (amount * 9)/100
    #     total_amount =int(amount + (gst*2))
    #     currency = 'USD'
    #     client = razorpay.Client(auth=("rzp_test_Ey7h721E1o2LY1", "AwU7kngK8eCZK9Ztqd02brOy"))
    #     payment = client.order.create({'amount': total_amount * 100, 'currency': 'INR', 'payment_capture': '1'})
    #     razorpay_order_id = payment['id']
    #     razorpay_payment_id = payment['receipt']
    #     balance = Wallet.objects.filter(email_id = request.user.email_id)
    #     transaction_id = generate_random_transaction_id()
    #     e_list = []
    #     for i in balance:
    #         e_list.append(i.recharge_amount)
    #     cust_wallet = 0
    #     for j in e_list:
    #         if j: 
    #             cust_wallet = int(j)+ int(cust_wallet)
    #     remaining = cust_wallet - int(total_amount)


    #     if request.method == 'POST':
    #         if cust_wallet > total_amount:
    #             done = Plan_Purchase(
    #             invoice_number = invoice_number,
    #             plan_order_id=razorpay_order_id,
                
    #             name = f'{request.user.first_name} {request.user.last_name}',
    #             cust_id=request.user.user_id,
    #             cust_email_id=request.user.email_id,
    #             cust_whatsapp_no=request.user.whatsapp_no,
    #             cgst = gst,
    #             sgst = gst,
    #             total_amount = total_amount,
    #             questions_count = plan.admin_plan_1_d,
    #             plan_purchase_time = current_time,
    #             plan_name=plan.plan_name_1,
    #             plan_amount=plan.amount_plan,
    #             plan_purchase_date = formatted_date,
    #             purchase_time = current_datetime,
    #             plan_month=month_alphabetic,
    #             )   
    #             done.save()
    #             wallet = Wallet(
    #                 cust_id = request.user.user_id,
    #                 name = f'{request.user.first_name} {request.user.last_name}',
    #                 email_id=request.user.email_id,
    #                 whatsapp_no=request.user.whatsapp_no,
    #                 recharge_time = current_time,
    #                 recharge_date= formatted_date,
    #                 debit_amount = total_amount,
    #                 wallet_month = month_alphabetic, 
    #                 transaction_id = transaction_id,
    #             )
    #             wallet.save()
            
                

    #         plan_name = "Personalized Guidance"
    #         customer=request.user.email_id 
    #         comment=Comment.objects.filter(plan_name=plan_name,user=customer,order_id = '')
    #         # print('comment',comment)
    #         for i in comment:
    #             if i.comment1:
    #                 print('ddddddddddddddd',i)
    #                 i.order_id = invoice_number
    #                 i.customer_to_admin_time=current_time
    #                 i.plan_purchase_date=formatted_date
    #                 i.plan_month = month_alphabetic
    #                 i.send_admin = True
    #                 i.save()
    #         return redirect('/dash_customer1/')
        
    #     context = {
    #         'razorpay_order_id': razorpay_order_id,
    #         'razorpay_merchant_key': 'rzp_test_Ey7h721E1o2LY1',
    #         'razorpay_amount': amount,
    #         'gst':gst, 
    #         'currency': currency,
    #         'plan':plan, 
    #         'total_amount':int(total_amount), 
    #         'current_date':current_date,
    #         'current_time':current_time,
    #         'cust_wallet':cust_wallet,
    #         'remaining':remaining,
    #     }
    #     return render(request, 'login/index4.html', context=context) 
    
  

import pytz   
import random
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import razorpay
import pytz
import datetime
from datetime import datetime  # Import only 'datetime' class from the 'datetime' module
import pytz
import random
import razorpay




@csrf_exempt
def comment_view_gold(request):
    recipient_numbers=request.user.whatsapp_no
    name = request.user.first_name

    # current_datetime_utc = datetime.datetime.now(pytz.utc)

    # # Convert the datetime to the Indian time zone
    # timezone = pytz.timezone('Asia/Kolkata')
    # current_datetime = current_datetime_utc.astimezone(timezone)

    # # Extract date and time components
    # current_date = current_datetime.date()
    # current_time = current_datetime.time().strftime('%H:%M:%S')
    # formatted_date = current_date.strftime('%d-%m-%Y')
    # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')




    current_datetime_utc = datetime.now(pytz.utc)

    # Convert the datetime to the Indian time zone
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    # current_time = current_datetime.time()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    formatted_date = current_date.strftime('%Y-%m-%d')
    # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
    date_obj = datetime.strptime(formatted_date, '%Y-%m-%d')

    # Get the month in alphabetic format
    month_alphabetic = date_obj.strftime('%B')
    invoice_number = random.randint(10000, 99999)
    print("Random Invoice Number:", invoice_number)
    # new_date = current_date + relativedelta(months=1)
    plan = admin_setting_plan.objects.get(plan_name_1='Celestial Guidance')
    amount = float(plan.amount_plan)  # Assuming plan.amount_plan is already an integer
    gst = (amount * 9)/100
    total_amount =float(amount + (gst*2))
    currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_Ey7h721E1o2LY1", "AwU7kngK8eCZK9Ztqd02brOy"))
    payment = client.order.create({'amount': total_amount * 100, 'currency': 'INR', 'payment_capture': '1'})
    razorpay_order_id = payment['id']
    razorpay_payment_id = payment['receipt']
    balance = Wallet.objects.filter(email_id = request.user.email_id)
    transaction_id = generate_random_transaction_id()
    e_list = []
    for i in balance:
        e_list.append(i.recharge_amount)
    cust_wallet = 0
    for j in e_list:
        if j: 
            cust_wallet = float(j)+ float(cust_wallet)
    remaining = cust_wallet - float(total_amount)
    if request.method == 'POST':
        if cust_wallet >=  total_amount:
        
            done = Plan_Purchase(
            plan_order_id=razorpay_order_id,
            invoice_number = invoice_number,
            
            name = f'{request.user.first_name} {request.user.last_name}',
            cgst = gst,
            sgst = gst,
            total_amount = total_amount,
            plan_purchase_time = current_time,
            questions_count = plan.admin_plan_1_d,
            cust_id=request.user.user_id,
            cust_email_id=request.user.email_id,
            cust_whatsapp_no=request.user.whatsapp_no,
            plan_name=plan.plan_name_1,
            plan_amount=plan.amount_plan,
            purchase_date = formatted_date,
            purchase_time = current_datetime,
            plan_month=month_alphabetic,
            # plan_expiry_date = new_date,

            )   
            done.save()
            wallet = Wallet(
                cust_id = request.user.user_id,
                name = f'{request.user.first_name} {request.user.last_name}',
                email_id=request.user.email_id,
                whatsapp_no=request.user.whatsapp_no,
                recharge_time = current_time,
                plan_recharge_date= formatted_date,  
                debit_amount = total_amount,
                wallet_month = month_alphabetic, 
                transaction_id = transaction_id,
            )
            wallet.save()
        
        # return redirect('/customer-payments/')
        plan_name = "Celestial Guidance"
        customer=request.user.email_id 
        comment=Comment.objects.filter(plan_name=plan_name,user=customer,order_id = '')
        print('comment',comment)
        for i in comment:
            if i.comment1:
                print('ddddddddddddddd',i)
                i.send_admin=True
                i.order_id = invoice_number
                i.plan_month = month_alphabetic
                i.purchase_date=formatted_date
                i.save()
        # admin_name = "Admin"   
        # message = f"Dear {admin_name},\n\n"
        # message += f"You have received a new Ask a Question from  . Login to see details.\n\n"
        # message += "Best Regards,\nTeam Jyotish Junction"
        # send_mail(
        #     'New Question Asked by Jyotish Junction Customer',
        #     message,
        #     'jyotishjunction11@gmail.com',  
        #     ['jyotishjunction11@gmail.com'], 
        #     fail_silently=False,
        # )
        # user_message = f"Dear  {request.user.first_name} {request.user.last_name},\n\n"
        # user_message += f"We sincerely appreciate your confidence in Jyotish Junction will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
        # user_message += "Warm Regards,\nTeam Jyotish Junction"
        # send_mail( 
        #     'Question has been received by us',
        #     user_message,
        #     'jyotishjunction11@gmail.com',  # Replace with your email address
        #     [request.user.email_id],  # User email address
        #     fail_silently=False,
        # )

        # send_sms_package_gold([recipient_numbers],name,"Celestial Guidance")
        return redirect('/dash_customer1/')
    
    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': 'rzp_test_Ey7h721E1o2LY1',
        'razorpay_amount': amount,
        'gst':gst, 
        'currency': currency,
        'plan':plan, 
        'total_amount':float(total_amount), 
        'current_date':current_date,
        'current_time':current_time,
        'cust_wallet':cust_wallet,
        'remaining':remaining,
    }
    return render(request, 'login/index2.html', context=context)






@csrf_exempt 
def comment_view_platinum(request):
    recipient_numbers=request.user.whatsapp_no
    name = request.user.first_name
    # current_datetime_utc = datetime.datetime.now(pytz.utc) 

    # # Convert the datetime to the Indian time zone
    # timezone = pytz.timezone('Asia/Kolkata')
    # current_datetime = current_datetime_utc.astimezone(timezone)


    
    # current_date = current_datetime.date()
    # current_time = current_datetime.time().strftime('%H:%M:%S')
    # formatted_date = current_date.strftime('%d-%m-%Y')
    # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')


    current_datetime_utc = datetime.now(pytz.utc)

    # Convert the datetime to the Indian time zone
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    # current_time = current_datetime.time()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    formatted_date = current_date.strftime('%Y-%m-%d')
    # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
    date_obj = datetime.strptime(formatted_date, '%Y-%m-%d')

    # Get the month in alphabetic format
    month_alphabetic = date_obj.strftime('%B')
    invoice_number = random.randint(10000, 99999)
    print("Random Invoice Number:", invoice_number)
    # new_date = current_date + relativedelta(months=1)
    plan = admin_setting_plan.objects.get(plan_name_1='Divine Revelations')
    amount = float(plan.amount_plan) 
    gst = (amount * 9)/100
    total_amount =float(amount + (gst*2))
    currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_Ey7h721E1o2LY1", "AwU7kngK8eCZK9Ztqd02brOy"))
    payment = client.order.create({'amount': total_amount * 100, 'currency': 'INR', 'payment_capture': '1'})
    razorpay_order_id = payment['id']
    razorpay_payment_id = payment['receipt']
    balance = Wallet.objects.filter(email_id = request.user.email_id)
    transaction_id = generate_random_transaction_id()
    e_list = []
    for i in balance:
        e_list.append(i.recharge_amount)
    cust_wallet = 0
    for j in e_list:
        if j: 
            cust_wallet = float(j)+ float(cust_wallet)
    remaining = cust_wallet - float(total_amount)
    if request.method == 'POST':
        if cust_wallet >= total_amount:
        
            done = Plan_Purchase(
            plan_order_id=razorpay_order_id,
            invoice_number = invoice_number,
            
            name = f'{request.user.first_name} {request.user.last_name}',
            cgst = gst,
            sgst = gst,
            total_amount = total_amount,
            plan_purchase_time = current_time,
            questions_count = plan.admin_plan_1_d,
            cust_id=request.user.user_id,
            cust_email_id=request.user.email_id,
            cust_whatsapp_no=request.user.whatsapp_no,
            plan_name=plan.plan_name_1,
            plan_amount=plan.amount_plan,
            purchase_date = formatted_date,
            purchase_time = current_datetime,
            plan_month=month_alphabetic,
           
            )   
            done.save()
            wallet = Wallet(
                cust_id = request.user.user_id,
                name = f'{request.user.first_name} {request.user.last_name}',
                email_id=request.user.email_id,
                whatsapp_no=request.user.whatsapp_no,
                recharge_time = current_time,
                plan_recharge_date= formatted_date,
                debit_amount = total_amount,
                wallet_month = month_alphabetic,
                transaction_id = transaction_id, 
            )
            wallet.save()
       
        # return redirect('/customer-payments/')
        plan_name = "Divine Revelations"
        customer=request.user.email_id 
        comment=Comment.objects.filter(plan_name=plan_name,user=customer,order_id="")
        print('comment',comment)
        for i in comment:
            if i.comment1:
                print('ddddddddddddddd',i)
                i.send_admin=True
                i.order_id = invoice_number
                i.plan_month = month_alphabetic
                i.purchase_date=formatted_date
                i.save()
        # admin_name = "Admin"  # Replace with the admin's name
        #   # Replace with the customer's ID

        # message = f"Dear {admin_name},\n\n"
        # message += f"You have received a new Ask a Question from  . Login to see details.\n\n"
        # message += "Best Regards,\nTeam Jyotish Junction"

        # send_mail(
        #     'New Question Asked by Jyotish Junction Customer',
        #     message,
        #     'jyotishjunction11@gmail.com',  # Replace with your email address
        #     ['jyotishjunction11@gmail.com'],  # Admin email address
        #     fail_silently=False,
        # )

        # user_message = f"Dear  {request.user.first_name} {request.user.last_name},\n\n"
        # user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
        # user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
        # user_message += "Warm Regards,\nTeam Jyotish Junction"


        # send_mail( 
        #     'Question has been received by us',
        #     user_message,
        #     'jyotishjunction11@gmail.com',  # Replace with your email address
        #     [request.user.email_id],  # User email address
        #     fail_silently=False,
        # )

        # # send_sms_package_platinum([recipient_numbers])
        # send_sms_package_platinum([recipient_numbers],name,"Divine Revelations")
        return redirect('/dash_customer1/')
    
    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_merchant_key': 'rzp_test_Ey7h721E1o2LY1',
        'razorpay_amount': amount,
        'gst':gst, 
        'currency': currency,
        'plan':plan, 
        'total_amount':float(total_amount), 
        'current_date':current_date,
        'current_time':current_time,
        'cust_wallet':cust_wallet,
        'remaining':remaining,
    }
    return render(request, 'login/index3.html', context)




def dash_customer1(request):
    plan = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).order_by('-plan_purchase_time','-plan_purchase_date')
    
    plan1 = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).last()

    customer = GurujiUsers.objects.filter(is_customer=True)   
    comment = Comment.objects.filter(user = request.user.email_id)
    print('hhhhhhhhhhhhhhh',comment)
   
    ddd = []
    cust_set = set()
    for i in comment:
        value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user)
        cust_set.add(value)
    cust_data = list(cust_set)
    
    # Debugging: Print plan_name values
    for p in plan:
        for j in cust_data:
            if j[1] == p.invoice_number:
                final_data = Comment.objects.filter(order_id = p.invoice_number).last()
                ddd.append(final_data)
    print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr',len(plan),len(cust_data),len(ddd))   
    cust_set2 = set()
    for i in plan:
        for j in comment:
                if i.invoice_number == j.order_id :
                    op = Comment.objects.filter(Q(order_id=i.invoice_number) & Q(qapprove=False)).count()   
                    print('eeeeeeeeeeee',op)
                    if j.plan_name =='Celestial Guidance' and op <= 2001 :
                        value = (j.object_id,j.order_id,j.plan_name,j.plan_amount,j.plan_purchase_date,j.user,op)
                    elif j.plan_name == "Divine Revelations" and op <= 6000:
                        value = (j.object_id,j.order_id,j.plan_name,j.plan_amount,j.plan_purchase_date,j.user,op)
                    elif j.plan_name == "Personalized Guidance" and op <= 0:
                        value = (j.object_id,j.order_id,j.plan_name,j.plan_amount,j.plan_purchase_date,j.user,op)
                    cust_set2.add(value)
    cust_data2 = list(cust_set2)

    
 
    # Assuming you want to get the entry with primary key 1
    comment = Comment.objects.filter(user=request.user.email_id)

    # Get the current time in UTC
    current_datetime_utc = datetime.now(pytz.utc)

    # Convert the current UTC time to the 'Asia/Kolkata' timezone
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)

    # Extract the date and time components
    current_date = current_datetime.date()
    current_time = current_datetime.time().strftime('%H:%M:%S')

    # Print the customer_to_admin_time for each entry in the 'comment' queryset
    # for p in comment:
    #     print(p.customer_to_admin_time)

    # # Convert customer_to_admin_time from string to time format
    # for p in comment:
    #     customer_to_admin_time_str = p.customer_to_admin_time  # Assuming p.customer_to_admin_time is a string representing the time
    #     time_format = "%H:%M:%S"  # Adjust the format according to the actual format of customer_to_admin_time (time part only)

    #     try:
    #         customer_to_admin_time = datetime.strptime(customer_to_admin_time_str, time_format).time()
    #         print(type(customer_to_admin_time))
    #     except ValueError:
    #     	pass
            # print(f"Error: Unable to convert {customer_to_admin_time_str} to time format.")


    
    commentgf = Comment.objects.filter(user = request.user).last()
    
    recipient_numbers=request.user.whatsapp_no
    # print('ssssssssss',commentgf)
    # print('ddddddddddddddd',request.user,request.user.first_name,request.user.last_name,)

    

    recipient_numbers=request.user.whatsapp_no
    name = f'{request.user.first_name} {request.user.last_name}'
    print('recipient_numbers',recipient_numbers)
    print('name',name)

    # if plan1.plan_name == "Celestial Guidance":
    #     send_sms_package_gold([recipient_numbers],name,"Celestial Guidance")
    # elif plan1.plan_name == "Personalized Guidance":
    #     send_sms_package_silver([recipient_numbers],name,"Personalized Guidance")
    # elif plan1.plan_name == "Divine Revelations":
    #     send_sms_package_platinum([recipient_numbers],name,"Divine Revelations")

    admin_name = "Admin"   
    message = f"Dear {admin_name},\n\n"
    message += f"You have received a new Ask a Question from {name} . Login to see details.\n\n"
    message += "Best Regards,\nTeam Jyotish Junction"
    send_mail(
        'New Question Asked by Jyotish Junction Customer',
        message,
        'jyotishjunction11@gmail.com',  
        ['jyotishjunction11@gmail.com'], 
        fail_silently=False,
    )
    user_message = f"Dear  {request.user.first_name} {request.user.last_name},\n\n"
    user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
    user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
    user_message += "Warm Regards,\nTeam Jyotish Junction"
    send_mail( 
        'Question has been received by us',
        user_message,
        'jyotishjunction11@gmail.com',  # Replace with your email address
        [request.user.email_id],  # User email address
        fail_silently=False,
    )
    print('ssssssssss',commentgf)
    print('ddddddddddddddd',request.user,request.user.first_name,request.user.last_name,)

    

    

    context = {
        'plan': plan,
        'customer': customer,
        'plan':plan,
        'cust_data':cust_data,   
        'cust_data2':cust_data2,
        'ddd':ddd,
    }
    return redirect('/dash_customer/')



def popup(request):
    return render(request,'login/popup.html')

# def dash_customer1(request):
#     plan = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).order_by('-plan_purchase_time','-plan_purchase_date')
#     plan1 = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).last()
#     print('aaaaaaaaaaaaaaaaaaaaaaapppppppppppppppppppppppppppp',plan1.plan_name)
      
#     customer = GurujiUsers.objects.filter(is_customer=True)   
#     comment = Comment.objects.filter(user = request.user.email_id)
#     print('hhhhhhhhhhhhhhh',comment)
   
#     ddd = []
#     cust_set = set()
#     for i in comment:
#         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user)
#         cust_set.add(value)
#     cust_data = list(cust_set)
    
#     # Debugging: Print plan_name values
#     for p in plan:
#         for j in cust_data:
#             if j[1] == p.invoice_number:
#                 final_data = Comment.objects.filter(order_id = p.invoice_number).first()
#                 ddd.append(final_data)
#     print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr',len(plan),len(cust_data),len(ddd))

    

#     # Assuming you want to get the entry with primary key 1
#     comment = Comment.objects.filter(user=request.user.email_id)

#     # Get the current time in UTC
#     current_datetime_utc = datetime.now(pytz.utc)

#     # Convert the current UTC time to the 'Asia/Kolkata' timezone
#     timezone = pytz.timezone('Asia/Kolkata')
#     current_datetime = current_datetime_utc.astimezone(timezone)

#     # Extract the date and time components
#     current_date = current_datetime.date()
#     current_time = current_datetime.time().strftime('%H:%M:%S')

#     # Print the customer_to_admin_time for each entry in the 'comment' queryset
#     # for p in comment:
#     #     print(p.customer_to_admin_time)

#     # # Convert customer_to_admin_time from string to time format
#     # for p in comment:
#     #     customer_to_admin_time_str = p.customer_to_admin_time  # Assuming p.customer_to_admin_time is a string representing the time
#     #     time_format = "%H:%M:%S"  # Adjust the format according to the actual format of customer_to_admin_time (time part only)

#     #     try:
#     #         customer_to_admin_time = datetime.strptime(customer_to_admin_time_str, time_format).time()
#     #         print(type(customer_to_admin_time))
#     #     except ValueError:
#     #     	pass
#             # print(f"Error: Unable to convert {customer_to_admin_time_str} to time format.")


#     commentgf = Comment.objects.filter(user = request.user).last()
    
#     recipient_numbers=request.user.whatsapp_no
#     # print('ssssssssss',commentgf)
#     # print('ddddddddddddddd',request.user,request.user.first_name,request.user.last_name,)

    

#     recipient_numbers=request.user.whatsapp_no
#     name = f'{request.user.first_name} {request.user.last_name}'
#     print('recipient_numbers',recipient_numbers)
#     print('name',name)
#     if plan1.plan_name == "Celestial Guidance":
#         send_sms_package_gold([recipient_numbers],name,"Celestial Guidance")
#     elif plan1.plan_name == "Personalized Guidance":
#         send_sms_package_silver([recipient_numbers],name,"Personalized Guidance")
#     elif plan1.plan_name == "Divine Revelations":
#         send_sms_package_platinum([recipient_numbers],name,"Divine Revelations")

#     admin_name = "Admin"   
#     message = f"Dear {admin_name},\n\n"
#     message += f"You have received a new Ask a Question from  . Login to see details.\n\n"
#     message += "Best Regards,\nTeam Jyotish Junction"
#     send_mail(
#         'New Question Asked by Jyotish Junction Customer',
#         message,
#         'jyotishjunction11@gmail.com',  
#         ['jyotishjunction11@gmail.com'], 
#         fail_silently=False,
#     )
#     user_message = f"Dear  {request.user.first_name} {request.user.last_name},\n\n"
#     user_message += f"We sincerely appreciate your confidence in Jyotish Junction as your chosen platform for seeking guidance. We acknowledge the significance of your inquiry and want to assure you that our proficient team of Astro Gurus will thoroughly analyze your birth charts and provide you with a meticulously considered response within 24 hours.\n\n"
#     user_message += "We kindly request you to rate the provided answer, as it will enable us to consistently deliver high-quality responses to all our valued seekers.\n\n"
#     user_message += "Warm Regards,\nTeam Jyotish Junction"
#     send_mail( 
#         'Question has been received by us',
#         user_message,
#         'jyotishjunction11@gmail.com',  # Replace with your email address
#         [request.user.email_id],  # User email address
#         fail_silently=False,
#     )



#     context = {
#         'plan': plan,
#         'customer': customer,
#         'plan':plan,
#         'cust_data':cust_data,   
#         'ddd':ddd,
#     }

#     return redirect('/after_login_cus/')


@csrf_exempt
def success(request):
    print(request.user)
    a=''
    plan_data = Plan_Purchase(cust_id = request.user.user_id , cust_email_id = request.user.email_id , cust_whatsapp_no = request.user.whatsapp_no)
    plan_data.save()
    plan = Plan_Purchase.objects.last()
    # if request.method == 'POST':
    #     a= request.POST
    #     print('ahhhhhhhhhhhh',a,a['razorpay_payment_id'])
    # plan.payment_id = a['razorpay_payment_id']
    # plan.save()  
    return render (request, 'success.html')





def comment(request):
    print('qqqqqqqqqqqqqqqqqq',request.user)
    # data1 = admin_setting_plan.objects.get(id=id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment1')
        print('jjjjjjj',comment_text)
        if comment_text != '':
            print('wwwwwwwwwwwwwww',comment_text)
            new_obj = Comment(comment1=comment_text, object_id = request.user.id, user = request.user.email_id)
            new_obj.save()
            # Redirect to the success page or specify the URL
            return redirect('/select_plan/')
    data = Comment.objects.all()
    data2 = GurujiUsers.objects.filter(is_customer = True)
    print(data2)
    return render(request, 'login/comment.html', {'comment_box_visible': True, 'data': data, 'data2':data2})




def generate_random_plan(length=6):
    alphabet = string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def astro_info(request):
    astrologers = AstrologerUser.objects.all()
    # Filtering based on country
    country_filter = request.GET.get('country')
    if country_filter:
        astrologers = astrologers.filter(aus_country=country_filter)
    # Get list of all countries
    countries = [country.name for country in pycountry.countries]
    context = {'astrologers': astrologers, 'countries': countries}
    return render(request, 'astrologer/astro_info.html', context)


from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import razorpay
import pytz
import datetime
from datetime import datetime  # Import only 'datetime' class from the 'datetime' module
import pytz
import random
import razorpay,stripe

def generate_order_id():
    # Generating a random 9-digit number
    random_digits = ''.join(random.choices(string.digits, k=9))
    
    # Concatenating the prefix "guru" with the random digits
    order_id = "order" + random_digits
    return order_id

stripe.api_key = 'sk_test_51NYjoESIMsjPxpEA8sWFXC0qE325msqgAZeUT5oV0t58RFIKbfv48Pvi2KiuWs0LnkeOqRXX68BMNloASUF2krMA00DLqw2csQ'




def send_sms_wallet(recipient_numbers,name,amount):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"

    var1 = name # Replace this with the actual value you want to pass
    var2 = amount


    message_template = "Dear {$var1}, Recharge successful {$var2} added to your wallet. Happy consulting. Regards NKB Divine Vedic Sciences"
    
    message = message_template.replace("{$var1}", name).replace("{$var2}", str(amount))
    # var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    

    # Replace {$ var1} with the actual value
    message = "Thank you for registering as an astrologer."

    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
   
    print("message:", message)

    # Prepare the payload
    payload = {
        "from": sender_id,
        "to": recipient_numbers,
        "data": {
            "var1": name,
            "var2": amount
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
        "template_id": "161458124"
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



from django.http import JsonResponse, HttpResponseRedirect


from django.conf import settings
from django.http import JsonResponse
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
import stripe
import requests
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY



stripe.api_key = settings.STRIPE_SECRET_KEY

def success_view(request):
    transaction_id = request.session.get('transaction_id')
    muser_id = request.session.get('muser_id')
    amount =request.session.get('amount')
    recharge_date = request.session.get('recharge_date')
    recharge_time = request.session.get('recharge_time')
    wallet_month =request.session.get('wallet_month')
    name = request.session.get('name')
    email_id = request.session.get('email_id')
    whatsapp_no =request.session.get('whatsapp_no')
    done = Wallet(
            order_id=generate_order_id(),
            payment_id = transaction_id, 
            recharge_amount = amount*2,
            recharge_date = recharge_date,
            recharge_time = recharge_time,
            wallet_month= wallet_month,
            name = name,
            cust_id=muser_id,
            email_id=email_id,
            whatsapp_no=whatsapp_no,
            transaction_id=transaction_id,
            )
    done.save()
    context = {
            'transaction_id' : transaction_id,
            'muser_id' : muser_id,
            'amount' :amount*2,
            'recharge_date' : recharge_date,
            'recharge_time' : recharge_time,
            'wallet_month' : wallet_month,
            'name' : name,
            'email_id' : email_id,
            'whatsapp_no' : whatsapp_no, 
           
        }

    return render(request, "payment_success.html",context)


def cancel_view(request):
    return render(request, "cancel.html")



def product_landing_page_view(request,paisa):
    current_datetime_utc = datetime.now(pytz.utc)

    # Convert the datetime to the Indian time zone
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    # current_time = current_datetime.time()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    formatted_date = current_date.strftime('%d-%m-%Y')
    # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
    date_obj = datetime.strptime(formatted_date, '%d-%m-%Y')

    # Get the month in alphabetic format
    amount = int(paisa) 
    month_alphabetic = date_obj.strftime('%B')
    invoice_number = random.randint(10000, 99999)
    transaction_id = generate_random_transaction_id()
    request.session['transaction_id'] = transaction_id
    request.session['muser_id'] = request.user.user_id
    request.session['amount'] = amount
    request.session['recharge_date'] = formatted_date
    request.session['recharge_time'] = current_time
    request.session['wallet_month'] = month_alphabetic
    request.session['name'] = f'{request.user.first_name} {request.user.last_name}'
    request.session['email_id'] = request.user.email_id
    request.session['whatsapp_no'] = request.user.whatsapp_no
    context = {
        "product": paisa,
        'name':f"{request.user.first_name} {request.user.last_name}",
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
    }
    return render(request, "landing.html", context) 

def create_checkout_session_view(request,paisa):
    YOUR_DOMAIN = "https://gurujispeaks.com/"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': paisa * 100,
                    'product_data': {
                        'name': f"{request.user.first_name} {request.user.last_name}",
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/',
        cancel_url=YOUR_DOMAIN + '/cancel/',
    )
    return JsonResponse({
        'id': checkout_session.id
    })

























# def home_page_view(request,paisa):
#     amount = paisa
#     user = f"{request.user.first_name} {request.user.last_name}"
#     email_id = request.user.email_id

#     request.session["amount"] = amount
#     request.session["user"] = user
#     request.session["email_id"] = email_id

#     context = {
#         'key': settings.STRIPE_PUBLISHABLE_KEY,
#         'amount':amount,
#         'user':user,
#         'email_id':email_id,
#     }
#     return render(request, "stripe-home.html", context)


# def charge_view(request):
#     if request.method == 'POST':
#         payment_method_id = request.POST.get('payment_method_id')
#         customer_nickname = request.POST.get('customer_nickname')
#         customer_email = request.POST.get('customer_email')
#         amount = request.session.get("amount")
#         try:
#             customer = stripe.Customer.create( 
#                 email=customer_email,
#                 description=f"Customer for {customer_nickname}",
#             )
#             payment_intent = stripe.PaymentIntent.create(
#                 amount=amount*100,
#                 currency='usd',
#                 description='Payment Gateway', 
#                 payment_method_types=['card'],
#                 payment_method=payment_method_id,
#                 customer=customer.id,
#             )
#             payment_intent.confirm()
#             payment_intent_status = payment_intent.confirm()
#             stripe_js_url = payment_intent_status['next_action']['use_stripe_sdk']['stripe_js']
#             response = requests.get(stripe_js_url)
#             print('payment', payment_intent)
#             print('stripe_js_url', stripe_js_url)
#             request.session["url"]=stripe_js_url







#             # Make an HTTP GET request to the stripe_js_url
#             if response.status_code == 200:
#                 context = {
#                     'status': 'success',
#                     'response_text': response.text,
#                     'stripe_js_url': stripe_js_url,   
#                 }
#                 return JsonResponse(context)
#             else:
#                 context = {
#                     'status': 'error',
#                     'message': 'Failed to make HTTP request',
#                     'stripe_js_url': stripe_js_url,
#                 }
#                 return JsonResponse(context)
#         except stripe.error.StripeError as e:  
#             context = {
#                 'status': 'error',
#                 'message': str(e),
#             }
#             return JsonResponse(context)
#     return render(request, "stripe-charge.html")

# def success_view(request):
#     url_type=request.session.get('url')
#     return render(request, 'success.html',{"url_type":url_type})







import json
import hashlib
import requests
from django.http import JsonResponse


def passs(request): 
    return render(request,'login/pass.html')



def ram(request):
    return redirect('/check-status/')


def check_status(request):
    plan_id = request.session.get('plan_id')
    transaction_id = request.session.get('transaction_id')
    muser_id = request.session.get('muser_id')
    amount =request.session.get('amount')
    plan_recharge_date = request.session.get('plan_recharge_date')
    recharge_time = request.session.get('recharge_time')
    wallet_month =request.session.get('wallet_month')
    name = request.session.get('name')
    email_id = request.session.get('email_id')
    whatsapp_no =request.session.get('whatsapp_no')
    merchant_id="M1V0CXVZ7AGF"
    saltKey = "5034b537-b639-498e-bb0f-927c119a3485"
    saltIndex = "1"
    # encode_string = f"/pg/v1/status/{merchant_id}/{transaction_id}" + saltKey
    encode_string = f"/pg/v1/status/M1V0CXVZ7AGF/{transaction_id}" + "5034b537-b639-498e-bb0f-927c119a3485"
    xVerify = hashlib.sha256(encode_string.encode()).hexdigest()
    xVerify = xVerify + "###" + saltIndex

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-VERIFY": xVerify,
        "X-MERCHANT-ID": merchant_id,
    }

    url = f"https://api.phonepe.com/apis/hermes/pg/v1/status/M1V0CXVZ7AGF/{transaction_id}"
    response = requests.get(url, headers=headers)

    data = json.loads(response.text)

    # Extracting the "success" value
    success = data.get("success")

    print(success)


    if success: 

        response_data = response.json()
        
        
        done = Wallet(
            order_id=generate_order_id(),
            payment_id = transaction_id, 
            recharge_amount = float(amount) * 1.5,
            plan_recharge_date = plan_recharge_date,
            recharge_time = recharge_time,
            wallet_month= wallet_month,
            name = name,
            cust_id=muser_id,
            email_id=email_id,
            whatsapp_no=whatsapp_no,
            transaction_id=transaction_id,
            )
        done.save()
        aa=GurujiUsers.objects.filter(email_id=email_id)
        for i in aa:
            first_name1 = i.first_name
            last_name1 = i. last_name
            whatsapp_no = i.whatsapp_no

        name = name
        recipient_numbers=whatsapp_no
        print('ddddddddd',name,whatsapp_no)

        # send_sms_wallet([recipient_numbers],name,amount)
        plan_id = request.session.get('plan_id')
        plan_data = Comment.objects.filter(plan_id=plan_id, object_id = muser_id, order_id = "")
        for j in plan_data:
            if j.plan_name == "Personalized Guidance": 
                plan_name = j.plan_name
                del request.session["plan_id"]
                context={'plan_name':plan_name}
                # return redirect('/ask_question_silver/')
                return render(request,'login/pass.html',context)

            elif j.plan_name == "Divine Revelations":
                del request.session["plan_id"]
                plan_name = j.plan_name
                context={'plan_name':plan_name}
                # return redirect('/ask_question_platinum/')
                return render(request,'login/pass.html',context)
            elif j.plan_name == "Celestial Guidance":
                del request.session["plan_id"]   
                plan_name = j.plan_name
                context={'plan_name':plan_name}
                # return redirect('/ask_question_gold/')
                return render(request,'login/pass.html',context)
            else:
                # return redirect('/customer-wallet/')
                plan_name = ''
                context={'plan_name':plan_name}
                return render(request,'login/pass.html',context)

        
        context = {
            
            'plan_name':None,
        }
        return render(request,'login/pass.html',context)

    else:
        plan_id = request.session.get('plan_id')
        context={'plan_id':plan_id}
        return render(request,"phonepe_fail.html",context)
    


# @csrf_exempt
def customer_recharge(request,paisa):
    data = admin_setting_plan.objects.all()
    plan = Plan_Purchase.objects.all()
    plan_data = Plan_Purchase.objects.filter(payment_id='')

    # Add the 'geolocation_url' context variable to be used in the template

    current_datetime_utc = datetime.now(pytz.utc)

    # Convert the datetime to the Indian time zone
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    # current_time = current_datetime.time()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    formatted_date = current_date.strftime('%Y-%m-%d')
    # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
    date_obj = datetime.strptime(formatted_date, '%Y-%m-%d')

    # Get the month in alphabetic format
    month_alphabetic = date_obj.strftime('%B')
    invoice_number = random.randint(10000, 99999)
    amount = float(paisa)  # Default amount if not provided or if request method is not "POST"
    #amount = int(amount)  # Convert the amount to an integer
    currency = 'INR'
    transaction_id = generate_random_transaction_id()
    
    request.session['transaction_id'] = transaction_id
    request.session['muser_id'] = request.user.user_id
    request.session['amount'] = amount
    request.session['plan_recharge_date'] = formatted_date
    request.session['recharge_time'] = current_time
    request.session['wallet_month'] = month_alphabetic
    request.session['name'] = f'{request.user.first_name} {request.user.last_name}'
    request.session['email_id'] = request.user.email_id
    request.session['whatsapp_no'] = request.user.whatsapp_no

    

    
    
    saltKey = "5034b537-b639-498e-bb0f-927c119a3485"
    saltIndex = "1"
    request_body = json.dumps({
            "merchantId": "M1V0CXVZ7AGF",
            "merchantTransactionId": transaction_id,
            "merchantUserId": request.user.user_id,
            "amount": paisa * 100,
            "redirectUrl": "https://www.gurujispeaks.com/ram/",
            "redirectMode": "POST",
            "callbackUrl": "https://www.gurujispeaks.com/",
            "mobileNumber": request.user.user_id,
            "paymentInstrument": {
                "type": "PAY_PAGE"
            } 
    })

    
    
    
    

    requestPayLoad = request_body.encode()
    
    requestPayLoad = base64.b64encode(requestPayLoad,altchars=None)
    print('decode;;;;;;;',request_body)
    

    requestPayLoad = requestPayLoad.decode()
    encodeString = requestPayLoad + "/pg/v1/pay" + saltKey
    xVerify = hashlib.sha256(encodeString.encode()).hexdigest()
    xVerify = xVerify + "###" + saltIndex


    print("request:",request_body,"\n\n Encode:",requestPayLoad,"\n\n xVerify:",xVerify)
    request_json = json.loads(request_body)

    # Extract the value of "merchantTransactionId"
    merchant_transaction_id = request_json["merchantTransactionId"]
    print('merchant_transaction_id',merchant_transaction_id)
    payload = {"request":requestPayLoad} 
    print('payload22222222222222',payload)
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-VERIFY": xVerify,
    }

    url = "https://api.phonepe.com/apis/hermes/pg/v1/pay"
    response = requests.post(url, json=payload, headers=headers)
    


    # print(response.text)

    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',response.text)
    print("URL:",url)


    if response.status_code == 200:
        response_data = response.json()   
        print('response_data["success"]',response_data["success"])
        if "success" in response_data and response_data["success"]:   
            # done = Wallet(
            #     order_id=generate_order_id(),
            #     payment_id = transaction_id, 
            #     recharge_amount = amount*2,
            #     recharge_date = formatted_date,
            #     recharge_time = current_time,
            #     wallet_month= month_alphabetic,
            #     name = f'{request.user.first_name} {request.user.last_name}',
            #     cust_id=request.user.user_id,
            #     email_id=request.user.email_id,
            #     whatsapp_no=request.user.whatsapp_no,
            #     transaction_id=transaction_id,
            #     )
            # done.save()
            
            redirect_info = response_data["data"]["instrumentResponse"]["redirectInfo"]
            redirect_url = redirect_info.get("url", "Redirect URL not provided")
            return render(request, 'payment_form.html', {'success': True, 'result': redirect_url})
        else:
            error_message = response_data.get("message", "Unknown error occurred")
            if error_message == "Unknown error occurred":
                print("PhonePe API response:", response_data)
    else:
        print("PhonePe API request failed with status code:", response.status_code)
        print("Response content:", response.text)
    return render(request, 'payment_form.html')

    # else:
    #     current_datetime_utc = datetime.now(pytz.utc)

    #     # Convert the datetime to the Indian time zone
    #     timezone = pytz.timezone('Asia/Kolkata')
    #     current_datetime = current_datetime_utc.astimezone(timezone)
    #     current_date = current_datetime.date()
    #     # current_time = current_datetime.time()
    #     current_time = current_datetime.time().strftime('%H:%M:%S')
    #     formatted_date = current_date.strftime('%d-%m-%Y')
    #     # date_obj = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')
    #     date_obj = datetime.strptime(formatted_date, '%d-%m-%Y')

    #     # Get the month in alphabetic format
    #     month_alphabetic = date_obj.strftime('%B')
    #     invoice_number = random.randint(10000, 99999)
    #     amount = int(paisa)  # Default amount if not provided or if request method is not "POST"
    #     #amount = int(amount)  # Convert the amount to an integer
    #     currency = 'USD'
        
    #     transaction_id = generate_random_transaction_id()

    #     url = reverse('stripe-pay',args=[amount])
    #     return redirect(url)

        
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        # Payment successful, save the necessary details to your database
        # Similar to the code you have in your current view for Razorpay
        return redirect('/dash_customer/')
    else:
        # Handle payment execution failure
        return render(request, 'payment_failure.html')
    
def payment_success(request):
    return render(request, 'payment_success.html')


def payment_cancel(request):
    return render(request, 'payment_cancel.html')






from django import template
from django.db.models import Q

def customer_to_admin(request):
    data1 = GurujiUsers.objects.filter(is_astrologer=True)
    

    
    customer = GurujiUsers.objects.filter(is_customer=True)
    comment_data = {}  
    for j in customer:
        comment_data[j.email_id] = Comment.objects.filter(user=j.email_id).values_list('comment1', flat=True)
        print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', comment_data[j.email_id])
        



    customer_data = GurujiUsers.objects.filter(is_customer=True, email_id = j.email_id)
    if request.method == 'POST':
        selected_astrologer_id = request.POST.get('astro_email_id')
        print('selected_astrologer_id', selected_astrologer_id)
        request.session['selected_astrologer_id'] = selected_astrologer_id
        print('selected_astrologer_id', selected_astrologer_id)
    print('comment_data[j.email_id]',comment_data)
        
    context = {
        'customer': customer,
        'comment_data': comment_data,
        'data1':data1,
    }

    return render(request, 'login/customer_to_admin.html', context)



from django.core.mail import send_mail

def adcustomer_to_admin(request, id):
    data = Comment.objects.all()
    data1 = GurujiUsers.objects.all()
    data2 = GurujiUsers.objects.get(id=id)

    print('zzzzzzzzzzzzzzzzzzzzzzzzz', data2.email_id)
    comment = Comment.objects.filter(user=data2.email_id)
    print('bbbbbbbbbbbbbbbbbbb', comment, len(comment))
    selected_astrologer_id = request.POST.get('astro_email_id')
    print('selected_astrologer_id', selected_astrologer_id)
    for i in comment:
        i.astro_email_id = selected_astrologer_id
        i.save()

    if selected_astrologer_id is not None:
        data2.astro_email_id = selected_astrologer_id
        data2.save()

        # Send email to the selected astrologer
        astrologer = GurujiUsers.objects.get(email_id=selected_astrologer_id)
        print('kkkkkkkkkkk',astrologer)
        subject = 'New customer comment'
        message = 'You have a new question try to reply that question .'
        sender_email = 'jyotishjunction11@gmail.com'
        recipient_list = [astrologer.email_id]
        send_mail(subject, message, sender_email, recipient_list)

    return redirect('/customer_to_admin/')


def ad_to_astro(request):  
    comments = Comment.objects.all()
    astrologer_users = GurujiUsers.objects.filter(is_astrologer=True)
    for i in comments:
        for j in astrologer_users:
            if i.astro_email_id == j.email_id:
                print("Match found:", i.astro_email_id)
    return render (request,'login/ad_to_astro.html')   

@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def astro_reply(request):
    data1=Comment.objects.all()   
    astrologer=GurujiUsers.objects.filter(is_astrologer=True)   
    customer=GurujiUsers.objects.filter(is_customer=True)
    data= request.user.email_id   
    comment= Comment.objects.filter(astro_email_id=request.user.email_id)
    print(comment)       
    for i in comment:   
        print(i.comment1,'             ',i.comment2)
    return render (request,'login/astro_reply.html',{'comment':comment,'data1':data1,'astrologer':astrologer,'customer':customer})




@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def editastro_reply(request, id):
    # current_datetime_utc = datetime.datetime.now(pytz.utc)
    # timezone = pytz.timezone('Asia/Kolkata')
    # current_datetime = current_datetime_utc.astimezone(timezone)
    # current_date = current_datetime.date()
    # current_time = current_datetime.time().strftime('%H:%M:%S')

    current_datetime_utc = datetime.now(pytz.utc)

    # Convert the datetime to the Indian time zone
    timezone = pytz.timezone('Asia/Kolkata')
    current_datetime = current_datetime_utc.astimezone(timezone)
    current_date = current_datetime.date()
    # current_time = current_datetime.time()
    current_time = current_datetime.time().strftime('%H:%M:%S')
    



    plan =Plan_Purchase.objects.get(id = id)
    user = GurujiUsers.objects.get(email_id = request.user.email_id)
    user_data = GurujiUsers.objects.get(email_id = plan.cust_email_id)
    data = Comment.objects.filter(user = plan.cust_email_id, astro_email_id = request.user.email_id,plan_name = plan.plan_name, plan_amount = plan.plan_amount, order_id = plan.invoice_number)
    for j in data:
        print(j.comment1, j.comment2) 
    if request.method == 'POST':
        for comment in data:
            comment2_key = f'comment2_{comment.id}'  
            comment2 = request.POST.get(comment2_key)
            comment.comment2 = comment2
            comment.astrloger_to_admin_time = current_time
            comment.save()
        admin_name = GurujiUsers.objects.get(is_superuser = True, is_admin = True)
        customer_id = f"{plan.name}"  # Replace with the customer's ID
        subject = 'Customer Question has been answered by our Astrologer'
        message = f"Dear {admin_name.first_name} {admin_name.last_name},\n\n"
        message += f"Our Astro Guru has submitted their answer for {plan.name}. Login to see details.\n\n"
        message += "Best Regards,\nTeam Jyotish Junction"
        
        send_mail(
            subject,
            message,
            'jyotishjunction11@gmail.com',  # Replace with your email address
            ['jyotishjunction11@gmail.com'],  # Admin email address
            fail_silently=False,
        )
        return redirect('/dash_astro/')
    data4 = Customer_profile.objects.filter(cust_id =plan.cust_id)
    user_profile = GurujiUsers.objects.get(email_id = plan.cust_email_id)   
    print(data4,len(data4))
    return render(request, 'login/editastro_reply.html', {'user_pro':f'{user_profile.first_name} {user_profile.last_name}','data4':data4,'user_profile':user_profile,'data': data,'plan':plan,'user':user,'user_data':user_data,})


def astro_reply_admin(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')  
        print('email_id', email_id)
        comments = Comment.objects.filter(user=email_id)
        print('comments',comments)
        
        for comment in comments:
            comment.qapprove = True
            comment.save()
        return redirect('/astro_reply_admin/')  # Redirect to the same page after updating the fields
    
    data1 = Comment.objects.all()
    data2 = GurujiUsers.objects.filter(is_astrologer=True)
    data3 = GurujiUsers.objects.filter(is_customer=True)
    comment = Comment.objects.all()         
    print(comment)
    for i in comment:
        print(i.comment1)
    
    return render(request, 'login/astro_reply_admin.html', {'comment': comment, 'data1': data1, 'data2': data2, 'data3': data3})


from .models import Rating,Plan_Purchase,Comment

def customer_view_answer(request, id): 
    plan = Plan_Purchase.objects.get(id=id)
    guruji_user = GurujiUsers.objects.get(email_id=request.user.email_id)
    data = Comment.objects.filter(user=plan.cust_email_id, plan_name=plan.plan_name, order_id=plan.invoice_number)
    user = request.user
    
    if guruji_user.review_comments1 and guruji_user.review_star1:
    
        error_message = 'Data already saved!'
        messages.error(request, error_message)
        return render(request, 'login/customer-view-answer.html', {'user': user, 'data': data, 'guruji_user': guruji_user})

    if request.method == 'POST':
        review_comments1 = request.POST.get('review_comments1')
        review_star1 = request.POST.get('review_star1')
        

        guruji_user.review_comments1 = review_comments1
        guruji_user.review_star1 = review_star1

        guruji_user.save()
        messages.success(request, 'Data saved successfully!')
    
    context = {
        'user': user,
        'data': data,
        'guruji_user':guruji_user
    }
    
    return render(request, 'login/customer-view-answer.html', context)


 


def dash_admin(request):
    return render(request,'login/dash_admin.html')    

@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def dash_astro(request):   
    data1=Comment.objects.all()
    astrologer=GurujiUsers.objects.filter(is_astrologer=True)   
    customer=GurujiUsers.objects.filter(is_customer=True)
    data3=Plan_Purchase.objects.all()
    data= request.user.email_id 
    # print('111111111111111',data,type(data))
    data2 = GurujiUsers.objects.get(email_id = request.user.email_id)  


    data3=Plan_Purchase.objects.all()
    comment= Comment.objects.filter(astro_email_id=request.user.email_id)
    cust_set = set()
    cust_set2 = set()
    for i in comment:
        cust_data = (i.cust_name,i.plan_name,i.plan_purchase_date,i.order_id,i.astro_email_id,i.user,i.plan_amount)  
        d=list(cust_data)
        print('llllllllllllll',len(d))
        if cust_data not in cust_set:
            cust_set.add(cust_data)     
    filtered_cust_set = [item for item in cust_set if item[2] is not None]

    sorted_cust_set = sorted(filtered_cust_set, key=lambda x: x[2],reverse=True)
    data_list = []
    for k in cust_set:
        ddd = Comment.objects.filter(cust_name = k[0],plan_name = k[1],plan_purchase_date = k[2],order_id = k[3],astro_email_id = k[4],user = k[5],plan_amount=k[6]).last()
        data_list.append(ddd)
    print('22222222222222222',data_list,len(data_list))
    print('33333333333333333',cust_set,len(cust_set))

  
   

    # for i in comment:   
    #     print(i.comment1,'             ',i.comment2)
    return render (request,'login/dash_astro.html',{'sorted_cust_set':sorted_cust_set,'data_list':data_list,'data':data,'cust_set':cust_set,'data1':data1,'astrologer':astrologer,'customer':customer,'data2':data2,'data3':data3})






def view_data(request):  
    data1 = Comment.objects.all()
    context={'data1':data1}
    return render(request,'view_data.html',context)  


   



def view_astroquestions(request, user):
    data = Comment.objects.filter(user=user)
    print('dadsddfffgg',data)
    for i in data:
        if i.user == user:
            print('ddddddddddddddddddddd',i.user == user)
            print('aparna',i.user,user)
    data1 = Comment.objects.all()
    context={'data1':data1, 'data':data, 'user':user}
    return render(request, 'astrologer/view_asrtoanswers.html',context)






def astro_admin_approved(request):
    astro = GurujiUsers.objects.filter(is_astrologer=True)
    print('astro',astro)

    context={
        'astro':astro,
    }
    return render(request,'login/astro_admin_approved.html',context)


from django.db import IntegrityError\


def admin_approval_astro(request):
    astro = GurujiUsers.objects.filter(is_astrologer=False)
    print('astro',astro)

    context={
        'astro':astro,
    }
    return render(request,'login/admin_approval_astro.html',context)





def ask_ques_login(request):
    error_message = ""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        print(user_id,password)

        # Check if user_id is an email or a mobile number
        if '@' in user_id:  # If '@' is present, consider it an email
            try:
                user = GurujiUsers.objects.get(email_id=user_id)
                print('lllllll',user)
            except GurujiUsers.DoesNotExist:
                user = None
        else:  # Otherwise, consider it a mobile number
            try:
                user = GurujiUsers.objects.get(whatsapp_no=user_id)
            except GurujiUsers.DoesNotExist:
                user = None
        # Authenticate user   
        if user is not None:
            user = authenticate(request, username=user.user_id, password=password)
        if user is not None and user.is_customer:
            login(request, user)
            return redirect('/ask_question_silver/')
        else:
            error_message = 'Invalid user ID, email, or password'

    return render(request, 'setting/ask_ques_login.html', {'error_message': error_message})

 
# def ask_ques_signup(request):
#     if request.method == "POST":
#         user_id = generate_random_password11()
#         whatsapp_no = request.POST.get('whatsapp_no')        
#         email_id = request.POST.get('email_id')  
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         password_no = request.POST.get('password')
#         password = make_password(request.POST['password'])
#         conform_password = make_password(request.POST['confirm_password'])
#         country= request.POST.get('country')
#         gender = request.POST.get('gender')
#         dob = request.POST.get('dob')   
#         pincode = request.POST.get('pincode')
#         city = request.POST.get('city') 
#         state = request.POST.get('state')
#         birth_time = request.POST.get('birth_time')
#         birth_place = request.POST.get('birth_place')


#         if GurujiUsers.objects.filter(email_id=email_id).exists():
#             return redirect('/error_email/')

#         # Check for duplicate whatsapp_no
#         if GurujiUsers.objects.filter(whatsapp_no=whatsapp_no).exists():
#             return redirect('/error_mobile/')

#         user = GurujiUsers(user_id = user_id,whatsapp_no = whatsapp_no, email_id = email_id, first_name = first_name, last_name = last_name,country=country,gender=gender,dob=dob,pincode=pincode,city=city,state=state,birth_time=birth_time,birth_place=birth_place, password = password ,is_staff=True,is_active = True,is_customer=True )
#         user.save()
        
#         message = f"Dear  {first_name} {last_name},\n\n" \
#             f"Welcome to Jyotish Junction, your trusted online astrology consultancy platform. We are delighted to have you join our community, where we believe in the true power of astrology to bring profound insights and transformative experiences.\n\n" \
#             f"At Jyotish Junction, we prioritize accuracy and personalized guidance. Our seasoned astrologers take the time to meticulously analyze your horoscope, providing you with accurate predictions and effective solutions tailored to your unique life path\n\n" \
#             f"Say goodbye to generic readings! Our platform is dedicated to offering personalized predictions on love, career, finances, and more. With our reliable guidance, you can make informed decisions and unlock a future full of success\n\n" \
#             f"Experience the real power of astrology with us. Our dedicated astrologers will help you navigate your life's journey, uncover hidden treasures, and guide you towards a future filled with purpose and fulfillment.\n\n" \
#             f"Join us at Jyotish Junction and embrace the celestial whispers that hold the key to your destiny. We are committed to providing you with the in-depth insights you deserve.\n\n" \
#             f"Get ready to embark on a transformative journey with us. True wisdom takes time, but the rewards are lifelong. \n\n" \
#             f"Welcome to Jyotish Junction, where the magic of astrology awaits! \n\n" \
#             f"Best Regards,\n" \
#             f"The Team at Jyotish Junction"

#         send_mail(
#             'Welcome to Jyotish Junction - Embrace Celestial Whispers for a Fulfilling Future!',
#             message,
#             'zappkodesolutions@gmail.com',
#             [email_id],
#             fail_silently=False,
#         )

#         return redirect('/ask_ques_otp/')
    
        
#     return render(request, 'setting/ask_ques_signup.html')




def ask_ques_signup(request):
    email_ids = GurujiUsers.objects.values_list('email_id', flat=True)
    email_ids_list = list(email_ids)  
    phone_numbers = GurujiUsers.objects.values_list('whatsapp_no', flat=True)
    phone_numbers_list = list(phone_numbers)
    print(phone_numbers_list,email_ids_list)
    for email_id in email_ids:
        exist_email_id =email_id
    
    if request.method == "POST":
        user_id = generate_random_password11()
        whatsapp_no = request.POST.get('whatsapp_no')      
        email_id = request.POST.get('email_id')  
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')
        password_no = request.POST.get('password')
        password = make_password(request.POST['password'])
        conform_password = make_password(request.POST['confirm_password'])
        if GurujiUsers.objects.filter(email_id=email_id).exists():
            return redirect('/error_email/')

        

        # Check for duplicate whatsapp_no
        if GurujiUsers.objects.filter(whatsapp_no=whatsapp_no).exists():
            return redirect('/error_mobile/')
        
        

        user = GurujiUsers(user_id = user_id,whatsapp_no = whatsapp_no, email_id = email_id, first_name = first_name, last_name = last_name, password = password ,is_staff=True,is_active = True,is_customer=True )
        user.save()

        name = first_name + " " + last_name

        
        recipient_numbers = [whatsapp_no]  # Use the user's WhatsApp number
        # send_sms_customer_signup(recipient_numbers,name)
        # Save the job_id in the user's model instance
        
   

        subject = 'Welcome to Jyotish Junction'
        
        message = f"Dear  {first_name} {last_name},\n\n" \
            f"Welcome to Jyotish Junction, your trusted online astrology consultancy platform. We are delighted to have you join our community, where we believe in the true power of astrology to bring profound insights and transformative experiences.\n\n" \
            f"At Jyotish Junction, we prioritize accuracy and personalized guidance. Our seasoned astrologers take the time to meticulously analyze your horoscope, providing you with accurate predictions and effective solutions tailored to your unique life path\n\n" \
            f"Say goodbye to generic readings! Our platform is dedicated to offering personalized predictions on love, career, finances, and more. With our reliable guidance, you can make informed decisions and unlock a future full of success\n\n" \
            f"Experience the real power of astrology with us. Our dedicated astrologers will help you navigate your life's journey, uncover hidden treasures, and guide you towards a future filled with purpose and fulfillment.\n\n" \
            f"Join us at Jyotish Junction and embrace the celestial whispers that hold the key to your destiny. We are committed to providing you with the in-depth insights you deserve.\n\n" \
            f"Get ready to embark on a transformative journey with us. True wisdom takes time, but the rewards are lifelong. \n\n" \
            f"Welcome to Jyotish Junction, where the magic of astrology awaits! \n\n" \
            f"Best Regards,\n" \
            f"The Team at Jyotish Junction"
        
        from_email = settings.CAR_FROM_EMAIL
        recipient_list = [email_id]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD, connection=None)

        return redirect('/ask_ques_otp/')
    
        
    return render(request, 'setting/ask_ques_signup.html',{'email_ids_list':email_ids_list,'phone_numbers_list': phone_numbers_list})  






def otp_verification_before(request):
    error_message = ""
    if request.method == 'POST':
        otp = request.POST.get('otp')
        # Retrieve the OTP from the session
        stored_otp = request.session.get('login_otp')
        print(stored_otp)
        if otp == stored_otp:
            # OTP verification successful
            del request.session['login_otp']  # Remove the OTP from the session
            user_id = request.session.get('login_user_id') 
            user = GurujiUsers.objects.get(email_id=user_id)
            # user.backend = 'django.contrib.auth.backends.ModelBackend'  
            login(request, user)
            # Perform additional logic or login the user as needed
            return redirect('/ask_question_silver/')  # Redirect to the dashboard or desired page after successful login
        error_message = 'Invalid OTP'
    elif request.method == 'GET' and 'resend_otp' in request.GET:
        new_otp = str(random.randint(100000, 999999))  # Generate a new OTP
        print('new_otp',new_otp)
        user_id = request.session.get('login_user_id')
        user = GurujiUsers.objects.get(email_id=user_id)
        request.session['login_otp'] = new_otp  # Store the new OTP in the session
        otp = new_otp
        name = f"{user.first_name} {user.last_name}"
        # otp_login_sms([user_id],name,otp)
    return render(request, 'login/otp_verification_before.html', {'error_message': error_message})






def error_email(request):
    return render(request,'login/error_mail.html')


def error_mobile(request):
    return render(request,'login/error_mobile.html')


def send_sms_customer_signup(recipient_numbers,name):
    # EnableX credentials
    app_id = "64b4bd31112b540fbd054d49"
    app_key = "Wa4eAuUy5yhyEe5yyeRaueteguXa8y5ayeey"

    # SMS details
    sender_id = "NKBDVN"
    var1 = name # Replace this with the actual value you want to pass
    # Template message with {$ var1} placeholder
    message_template = "Hello {$var1}, Welcome your registration is successful. Start your astrological journey now. Regards NKB Divine Divine Vedic Sciences"

    # Replace {$ var1} with the actual value
    message = message_template.replace("{$var1}", var1)
    # message = "Thank you for registering as an astrologer."
    # API endpoint
    url = "https://api.enablex.io/sms/v1/messages/"

   
    print("var1:", var1)
    print("message_template:", message_template)
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
        "template_id": "531785614"
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


def customer_signup123(request):
    email_ids = GurujiUsers.objects.values_list('email_id', flat=True)
    email_ids_list = list(email_ids)
    # phone_numbers = GurujiUsers.objects.values_list('whatsapp_no', flat=True)
    # phone_numbers_list = list(phone_numbers)
    # print(phone_numbers_list,email_ids_list)
    for email_id in email_ids:
        exist_email_id =email_id
    
    if request.method == "POST":
        user_id = generate_random_password11()
        # whatsapp_no = request.POST.get('whatsapp_no')      
        email_id = request.POST.get('email_id')  
        # first_name = request.POST.get('first_name')  
        # last_name = request.POST.get('last_name')
        # password_no = request.POST.get('password')
        # password = make_password(request.POST['password'])
        # conform_password = make_password(request.POST['confirm_password'])
        if GurujiUsers.objects.filter(email_id=email_id).exists():
            return redirect('/error_email/')

        user = GurujiUsers(user_id = user_id, email_id = email_id,is_staff=True,is_active = True,is_customer=True )
        user.save()
        return redirect('/customer-login-otp/')
    
    return render(request, 'login/customer_signup.html',{'email_ids_list':email_ids_list})  



def customer_signup(request):
    email_ids = GurujiUsers.objects.values_list('email_id', flat=True)
    email_ids_list = list(email_ids)
    phone_numbers = GurujiUsers.objects.values_list('whatsapp_no', flat=True)
    phone_numbers_list = list(phone_numbers)
    print(phone_numbers_list,email_ids_list)
    for email_id in email_ids:
        exist_email_id =email_id
    
    if request.method == "POST":
        user_id = generate_random_password11()
        whatsapp_no = request.POST.get('whatsapp_no')      
        email_id = request.POST.get('email_id')  
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')
        password_no = request.POST.get('password')
        password = make_password(request.POST['password'])
        conform_password = make_password(request.POST['confirm_password'])
        if GurujiUsers.objects.filter(email_id=email_id).exists():
            return redirect('/error_email/')

        

        # Check for duplicate whatsapp_no
        if GurujiUsers.objects.filter(whatsapp_no=whatsapp_no).exists():
            return redirect('/error_mobile/')
        
        

        user = GurujiUsers(user_id = user_id,whatsapp_no = whatsapp_no, email_id = email_id, first_name = first_name, last_name = last_name, password = password ,is_staff=True,is_active = True,is_customer=True )
        user.save()

        name = first_name + " " + last_name

        
        recipient_numbers = [whatsapp_no]  # Use the user's WhatsApp number
        # send_sms_customer_signup(recipient_numbers,name)
        # Save the job_id in the user's model instance
        
   

        subject = 'Welcome to Jyotish Junction'
        
        message = f"Dear  {first_name} {last_name},\n\n" \
            f"Welcome to Jyotish Junction, your trusted online astrology consultancy platform. We are delighted to have you join our community, where we believe in the true power of astrology to bring profound insights and transformative experiences.\n\n" \
            f"At Jyotish Junction we prioritize accuracy and personalized guidance. Our seasoned astrologers take the time to meticulously analyze your horoscope, providing you with accurate predictions and effective solutions tailored to your unique life path\n\n" \
            f"Say goodbye to generic readings! Our platform is dedicated to offering personalized predictions on love, career, finances, and more. With our reliable guidance, you can make informed decisions and unlock a future full of success\n\n" \
            f"Experience the real power of astrology with us. Our dedicated astrologers will help you navigate your life's journey, uncover hidden treasures, and guide you towards a future filled with purpose and fulfillment.\n\n" \
            f"Join us at Jyotish Junction and embrace the celestial whispers that hold the key to your destiny. We are committed to providing you with the in-depth insights you deserve.\n\n" \
            f"Get ready to embark on a transformative journey with us. True wisdom takes time, but the rewards are lifelong. \n\n" \
            f"Welcome to Jyotish Junction, where the magic of astrology awaits! \n\n" \
            f"Best Regards,\n" \
            f"The Team at Jyotish Junction"
        
        from_email = settings.CAR_FROM_EMAIL
        recipient_list = [email_id]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD, connection=None)

        return redirect('/customer-login-otp/')
    
        
    return render(request, 'login/customer_signup.html',{'email_ids_list':email_ids_list,'phone_numbers_list': phone_numbers_list})  

def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email_id')
        email_exists = GurujiUsers.objects.filter(email_id=email).exists()
        return JsonResponse({'emailExists': email_exists})
    return JsonResponse({'error': 'Invalid request method'}, status=400)




def customer_login_view(request):
    error_message = ""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        print(user_id,password)

        # Check if user_id is an email or a mobile number
        if '@' in user_id:  # If '@' is present, consider it an email
            try:
                user = GurujiUsers.objects.get(email_id=user_id)
                print('lllllll',user)
            except GurujiUsers.DoesNotExist:
                user = None
        else:  # Otherwise, consider it a mobile number
            try:
                user = GurujiUsers.objects.get(whatsapp_no=user_id)
            except GurujiUsers.DoesNotExist:
                user = None

        # Authenticate user   
        if user is not None:
            user = authenticate(request, username=user.user_id, password=password)
        
        if user is not None and user.is_customer:
            login(request, user)
            return redirect('/after_login_cus/')
        else:
            error_message = 'Invalid Email Id, or password'

    return render(request, 'login/customer_login.html', {'error_message': error_message})



def whatsapp_qr(request):  
    
    user_phone = '+917400293601'  # User's phone number
    message = 'Hello,'  # Pre-filled message

    

    context = {
        'user_phone': user_phone,
        'message': message,
            }
    return render(request, 'whatsapp_qr.html', context)

import qrcode
from django.http import HttpResponse
from io import BytesIO

def generate_qr_code(request):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # qr.add_data('https://api.whatsapp.com/send?phone=%2B917400293601&text=Hello%2C')
    qr.add_data('https://api.whatsapp.com/send?phone=%2B917249103310&text=Hello%2C')
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Serve image
    buffer = BytesIO()
    img.save(buffer)
    return HttpResponse(buffer.getvalue(), content_type="image/png")



#old working 
# def otp_verification_view(request):
#     error_message = ""
#     if request.method == 'POST':
#         otp = request.POST.get('otp')
     
#         # Retrieve the OTP from the session
#         stored_otp = request.session.get('login_otp')

#         if otp == stored_otp:
#             # OTP verification successful
#             del request.session['login_otp']  # Remove the OTP from the session
#             user_id = request.session.get('login_user_id')
#             user = GurujiUsers.objects.get(whatsapp_no=user_id)
#             # user.backend = 'django.contrib.auth.backends.ModelBackend'
#             login(request, user)
#             # Perform additional logic or login the user as needed
#             return redirect('/after_login_cus/')  # Redirect to the dashboard or desired page after successful login

#         error_message = 'Invalid OTP'

#     return render(request, 'login/otp_verification.html', {'error_message': error_message})   

from django.http import JsonResponse
import random

# original

# def otp_verification_view(request):
#     error_message = ""
#     if request.method == 'POST':
#         otp = request.POST.get('otp')
#         # Retrieve the OTP from the session
#         stored_otp = request.session.get('login_otp')
#         print(stored_otp)
#         if otp == stored_otp:
#             # OTP verification successful
#             del request.session['login_otp']  # Remove the OTP from the session
#             user_id = request.session.get('login_user_id') 
#             user = GurujiUsers.objects.get(whatsapp_no=user_id)
#             # user.backend = 'django.contrib.auth.backends.ModelBackend'  
#             login(request, user)
#             # Perform additional logic or login the user as needed
#             return redirect('/after_login_cus/')  # Redirect to the dashboard or desired page after successful login
#         error_message = 'Invalid OTP'
#     elif request.method == 'GET' and 'resend_otp' in request.GET:
#         new_otp = str(random.randint(100000, 999999))  # Generate a new OTP
#         print('new_otp',new_otp)
#         user_id = request.session.get('login_user_id')
#         user = GurujiUsers.objects.get(whatsapp_no=user_id)
#         request.session['login_otp'] = new_otp  # Store the new OTP in the session
#         otp = new_otp
#         name = f"{user.first_name} {user.last_name}"
#         otp_login_sms([user_id],name,otp)
#     return render(request, 'login/otp_verification.html', {'error_message': error_message})



def otp_verification_view(request):
    error_message = ""
    if request.method == 'POST':
        otp = request.POST.get('otp')
        # Retrieve the OTP from the session
        stored_otp = request.session.get('login_otp')
        print(stored_otp)
        if otp == stored_otp:
            # OTP verification successful
            del request.session['login_otp']  # Remove the OTP from the session
            user_id = request.session.get('login_user_id') 
            user = GurujiUsers.objects.get(email_id=user_id)
            # user.backend = 'django.contrib.auth.backends.ModelBackend'  
            login(request, user)
            # Perform additional logic or login the user as needed
            return redirect('/after_login_cus/')  # Redirect to the dashboard or desired page after successful login
        error_message = 'Invalid OTP'
    elif request.method == 'GET' and 'resend_otp' in request.GET:
        new_otp = str(random.randint(100000, 999999))  # Generate a new OTP
        print('new_otp',new_otp)
        user_id = request.session.get('login_user_id')
        user = GurujiUsers.objects.get(whatsapp_no=user_id)
        request.session['login_otp'] = new_otp  # Store the new OTP in the session
        otp = new_otp
        name = f"{user.first_name} {user.last_name}"
        otp_login_sms([user_id],name,otp)
    return render(request, 'login/otp_verification.html', {'error_message': error_message})




def send_otp_sms(user_mobile, new_otp):
    # Implement the logic to send an OTP SMS to the provided mobile number
    # You can use third-party SMS APIs or services to achieve this
    	pass



from datetime import datetime
import pytz



# def dash_customer(request):
#     plan = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).order_by('-plan_purchase_time','-plan_purchase_date')
#     plan1 = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id )
    
#     customer = GurujiUsers.objects.filter(is_customer=True)   
#     comment = Comment.objects.filter(user = request.user.email_id)
#     print('hhhhhhhhhhhhhhh',comment)
   
#     ddd = []
#     cust_set = set()
#     for i in comment:
#         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user)     
#         cust_set.add(value)
#     cust_data = list(cust_set)
    
#     # Debugging: Print plan_name values
#     for p in plan:
#         for j in cust_data:
#             if j[1] == p.invoice_number:
#                 final_data = Comment.objects.filter(order_id = p.invoice_number).last()
#                 ddd.append(final_data)
#     print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr',len(plan),len(cust_data),len(ddd))   
#     cust_set2 = set()
#     for i in plan:
#         for j in comment:
#                 if i.invoice_number == j.order_id :
#                     op = Comment.objects.filter(Q(order_id=i.invoice_number) & Q(qapprove=False)).count()   
#                     print('eeeeeeeeeeee',op)
#                     if j.plan_name =='Celestial Guidance' and op <= 2001 :
#                         value = (j.object_id,j.order_id,j.plan_name,j.plan_amount,j.plan_purchase_date,j.user,op)
#                     elif j.plan_name == "Divine Revelations" and op <= 6000:
#                         value = (j.object_id,j.order_id,j.plan_name,j.plan_amount,j.plan_purchase_date,j.user,op)
#                     elif j.plan_name == "Personalized Guidance" and op <= 500:
#                         value = (j.object_id,j.order_id,j.plan_name,j.plan_amount,j.plan_purchase_date,j.user,op)
#                     cust_set2.add(value)
#     cust_data2 = list(cust_set2)

    
 
#     # Assuming you want to get the entry with primary key 1
#     comment = Comment.objects.filter(user=request.user.email_id)

#     # Get the current time in UTC
#     current_datetime_utc = datetime.now(pytz.utc)

#     # Convert the current UTC time to the 'Asia/Kolkata' timezone
#     timezone = pytz.timezone('Asia/Kolkata')
#     current_datetime = current_datetime_utc.astimezone(timezone)

#     # Extract the date and time components
#     current_date = current_datetime.date()
#     current_time = current_datetime.time().strftime('%H:%M:%S')

#     # Print the customer_to_admin_time for each entry in the 'comment' queryset
#     # for p in comment:
#     #     print(p.customer_to_admin_time)

#     # # Convert customer_to_admin_time from string to time format
#     # for p in comment:
#     #     customer_to_admin_time_str = p.customer_to_admin_time  # Assuming p.customer_to_admin_time is a string representing the time
#     #     time_format = "%H:%M:%S"  # Adjust the format according to the actual format of customer_to_admin_time (time part only)

#     #     try:
#     #         customer_to_admin_time = datetime.strptime(customer_to_admin_time_str, time_format).time()
#     #         print(type(customer_to_admin_time))
#     #     except ValueError:
#     #     	pass
#             # print(f"Error: Unable to convert {customer_to_admin_time_str} to time format.")


#     commentgf = Comment.objects.filter(user = request.user).last()
#     recipient_numbers=request.user.whatsapp_no
#     plan6 = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id )
#     # print('ssssssssss',commentgf)
#     # print('ddddddddddddddd',request.user,request.user.first_name,request.user.last_name,)

    

    

#     context = {
#         'plan': plan,
#         'customer': customer,
#         'plan6':plan6,
#         'cust_data':cust_data,   
#         'cust_data2':cust_data2,
#         'ddd':ddd,
#     }
#     return render(request,'login/dash_customer.html',context)


# rk


# def dash_customer(request):
#     plan = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).order_by('-plan_purchase_time','-plan_purchase_date')
#     customer = GurujiUsers.objects.filter(is_customer=True)   
#     comment = Comment.objects.filter(user = request.user.email_id)
#     print('hhhhhhhhhhhhhhh',comment)
#     cust_set = set()
#     for p in plan: 
#         for i in comment:
#             if p.invoice_number == i.order_id :
#                 if Comment.objects.filter(Q(order_id=p.invoice_number) & ~Q(qapprove=True)).count():
#                     op = Comment.objects.filter(Q(order_id=p.invoice_number) & ~Q(qapprove=True)).count()
#                     if i.plan_name =='Celestial Guidance' and op <= 5 :
#                         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
#                         cust_set.add(value)
#                     elif i.plan_name == "Divine Revelations" and op <= 10:
#                         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
#                         cust_set.add(value)
#                     elif i.plan_name == "Personalized Guidance" and op <= 1:
#                         value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
#                         cust_set.add(value)
#     cust_data = list(cust_set) 
#     print('cust_data',cust_data,len(cust_data)) 
#     ddd = []
#     for p in plan:
#         for j in cust_data:
#             if j[1] == p.invoice_number:
#                 final_data = Comment.objects.filter(order_id = p.invoice_number).first()
#                 ddd.append(final_data)
 

#     context = {
#         'plan': plan,
#         'customer': customer,
#         'plan':plan,
#         'cust_data':cust_data,   
#         'ddd':ddd,
#     }
#     return render(request,'login/dash_customer.html',context)





def dash_customer(request):
    plan = Plan_Purchase.objects.filter(cust_email_id = request.user.email_id ).order_by('-purchase_date')
    for i in plan:
     print("2222222",i.plan_name)
    customer = GurujiUsers.objects.filter(is_customer=True)   
    comment = Comment.objects.filter(user = request.user.email_id)

    cust_set = set()   
    for p in plan: 
        for i in comment:
            if p.invoice_number == i.order_id :
                if Comment.objects.filter(order_id=p.invoice_number).count():
                    op = Comment.objects.filter(order_id=p.invoice_number).count()
                    if i.plan_name =='Celestial Guidance' and op <= 5:
                        value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
                        rrr = Comment.objects.filter(order_id=value[1]).last()
                        if value[6] == 5 and rrr.qapprove:
                            pass 
                        else:
                            cust_set.add(value)
                    elif i.plan_name == "Divine Revelations" and op <= 10:
                        value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
                        rrr = Comment.objects.filter(order_id=value[1]).last()
                        if value[6] == 10 and rrr.qapprove:
                            pass 
                        else:
                            cust_set.add(value)
                    elif i.plan_name == "Personalized Guidance" and op <= 1:
                        value = (i.object_id,i.order_id,i.plan_name,i.plan_amount,i.plan_purchase_date,i.user,op)
                        print("33333333",value)
                        rrr = Comment.objects.filter(order_id=value[1]).last()
                        if value[6] == 1 and rrr.qapprove:
                            pass 
                        else:
                            cust_set.add(value)
    cust_data = list(cust_set) 
    print('cust_data',cust_data,len(cust_data))  
    ddd = []
    for p in plan:
        for j in cust_data:
            if j[1] == p.invoice_number:
                final_data = Comment.objects.filter(order_id = p.invoice_number).first()
                ddd.append(final_data)
 
    print('cust_data',plan,len(plan))
    print('cust_data',cust_data,len(cust_data))
    print('cust_data',ddd,len(ddd))
    context = {
        'plan': plan,
        'customer': customer,
        'plan':plan,
        'cust_data':cust_data,   
        'ddd':ddd,
    }
    return render(request,'login/dash_customer.html',context)
   

import pycountry

@login_required
@never_cache
def UserEditView(request):
    print('111111111111111111111',request.user.email_id)
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    rrr=data.country
    print('data',data)
    if request.method == 'POST':
        # data.first_name =request.POST.get('first_name')
        # data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        # data.whatsapp_no = request.POST.get('whatsapp_no')
        # data.gender = request.POST.get('gender')
        # data.pincode = request.POST.get('pincode')
        # data.city = request.POST.get('city')
        # data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        # data.age = request.POST.get('age')        
        # country_code = request.POST.get('country')
        # try:
        #     country = pycountry.countries.get(alpha_2=country_code)
        #     if country:
        #         country_full_name = country.name
        # except:
        #     pass
        # data.country = country_full_name
        image = request.FILES.get('cust_img')
        if image:
            # Save the new profile picture to the user's profile
            data.image = image
            data.save()
            sweetify.success(request, "Profile updated successfully.", timer=3000)
        else:
            return messages.info(request,"Image file is required.")
        data.save()

    user = GurujiUsers.objects.get(email_id=request.user.email_id)
    
        
    context = {
    'data':data,
    'rrr':rrr,
    }
           
    return render(request,'login/customer-profile.html',context)     

  

def update_silver(request):
    # print('111111111111111111111',request.user.email_id)
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    rrr=data.country
    print('data',data)
    if request.method == 'POST':
        # data.first_name =request.POST.get('first_name')
        # data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        # data.whatsapp_no = request.POST.get('whatsapp_no')
        # data.gender = request.POST.get('gender')
        # data.pincode = request.POST.get('pincode')
        # data.city = request.POST.get('city')
        # data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        # data.age = request.POST.get('age')        
        # country_code = request.POST.get('country')
        # try:
        #     country = pycountry.countries.get(alpha_2=country_code)
        #     if country:
        #         country_full_name = country.name
        # except:
        #     pass  
        # data.country = country_full_name
        data.save()
        return redirect ('/ask_question_silver/')

       
    context = {
    'data':data,
    'rrr':rrr,
    }
           
    return render(request,'login/update_profile_silver.html',context)
    
    


def update_gold(request):
    print('111111111111111111111',request.user.email_id)
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    rrr=data.country
    print('data',data)
    if request.method == 'POST':
        # data.first_name =request.POST.get('first_name')
        # data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        data.whatsapp_no = request.POST.get('whatsapp_no')
        data.gender = request.POST.get('gender')
        data.pincode = request.POST.get('pincode')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        data.age = request.POST.get('age')        
        country_code = request.POST.get('country')
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_full_name = country.name
        except:
            pass
        data.country = country_full_name
        data.save()
        return redirect('/ask_question_gold/')
    context = {
    'data':data,
    'rrr':rrr,
    }
           
    return render(request,'login/update_profile_gold.html',context)




def update_platinum(request):
    print('111111111111111111111',request.user.email_id)
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    rrr=data.country
    print('data',data)
    if request.method == 'POST':
        # data.first_name =request.POST.get('first_name')
        # data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        data.whatsapp_no = request.POST.get('whatsapp_no')
        data.gender = request.POST.get('gender')
        data.pincode = request.POST.get('pincode')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        data.age = request.POST.get('age')        
        country_code = request.POST.get('country')
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_full_name = country.name
        except:
            pass
        data.country = country_full_name
        data.save()
        return redirect('/ask_question_platinum/')
    context = {
    'data':data,
    'rrr':rrr,
    }
           
    return render(request,'login/update_profile_platinum.html',context)






def update_silver_dash(request):
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    rrr=data.country
    
    if request.method == 'POST':
        # data.first_name =request.POST.get('first_name')
        # data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        data.whatsapp_no = request.POST.get('whatsapp_no')
        data.gender = request.POST.get('gender')
        data.pincode = request.POST.get('pincode')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        data.age = request.POST.get('age')        
        country_code = request.POST.get('country')
        id = request.session.get("id")
        print()
        print('111111111111111111111',id)
        print()
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_full_name = country.name
        except:
            pass
        data.country = country_full_name
        data.save()

        return redirect('/ask_q_silver/{}'.format(id))
    context = {
    'data':data,
    'rrr':rrr,
    }
           
    return render(request,'login/update_profile_silver.html',context)


    # context = {
    # 'data':data,   
    # 'rrr':rrr,
    # }
           
    # return render(request,'login/customer-profile.html',context)



def update_gold_dash(request):
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    rrr=data.country
    
    if request.method == 'POST':
        # data.first_name =request.POST.get('first_name')
        # data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        data.whatsapp_no = request.POST.get('whatsapp_no')
        data.gender = request.POST.get('gender')
        data.pincode = request.POST.get('pincode')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        data.age = request.POST.get('age')        
        country_code = request.POST.get('country')
        id = request.session.get("id")
        print()
        print('111111111111111111111',id)
        print()
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_full_name = country.name
        except:
            pass
        data.country = country_full_name
        data.save()

        return redirect('/ask_q_gold/{}'.format(id))
    context = {
    'data':data,
    'rrr':rrr,
    }
           
    return render(request,'login/update_profile_gold.html',context)


    # context = {
    # 'data':data,   
    # 'rrr':rrr,
    # }
           
    # return render(request,'login/customer-profile.html',context)

# -----------------------------------------------------


def update_platinum_dash(request):
    data = GurujiUsers.objects.get(email_id = request.user.email_id)
    rrr=data.country
    
    if request.method == 'POST':
        # data.first_name =request.POST.get('first_name')
        # data.last_name =request.POST.get('last_name')
        data.dob = request.POST.get('dob')   
        data.whatsapp_no = request.POST.get('whatsapp_no')
        data.gender = request.POST.get('gender')
        data.pincode = request.POST.get('pincode')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.birth_time = request.POST.get('birth_time')
        data.email_id = request.POST.get('email_id')
        data.birth_place = request.POST.get('birth_place') 
        data.age = request.POST.get('age')        
        country_code = request.POST.get('country')
        id = request.session.get("id")
        
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if country:
                country_full_name = country.name
        except:
            pass
        data.country = country_full_name
        data.save()

        return redirect('/ask_q_platinum/{}'.format(id))
    context = {
    'data':data,
    'rrr':rrr,
    }
           
    return render(request,'login/update_profile_platinum.html',context)


 


from django.urls import reverse


def view_plan(request):
    print('rrrrrrrrrrrrrrrrrrrrr', request.user)
    data = admin_setting_plan.objects.all()
    plan = Plan_Purchase.objects.all()
    plan_data = Plan_Purchase.objects.filter(payment_id='')
    authenticated_user = request.user


    # Add the 'geolocation_url' context variable to be used in the template
    # geolocation_url = reverse('get_geolocation_data')


    # client_ip = request.META.get('REMOTE_ADDR', '')
    # print('client_ip',client_ip)

    # try:
    #     # Use a geolocation API to get the approximate location based on the client's IP address
    #     response = requests.get(f'https://ipinfo.io/{client_ip}/json', timeout=5)
    #     data = response.json()
    #     location = data.get('city', '') + ', ' + data.get('region', '') + ', ' + data.get('country', '')
    #     print('Location:', location)
    #     print('Country:', data.get('country'))
    # except Exception as e:
    #     location = 'Error: Unable to fetch location'
    #     print('Error while fetching location:', str(e))

    
    # response = requests.get(f'https://ipinfo.io/{client_ip}/json', timeout=5)

    # try:
    #         data = response.json()
    #         location = data.get('city', '') + ', ' + data.get('region', '') + ', ' + data.get('country', '')
    #         print('fdsdfg',data.get('country'))

           
    # except ValueError:
    #         location = 'Error: Unable to fetch location'
    #         print('Error while fetching location')

    context={
        # 'ip_address': client_ip ,
        # 'location': location,
        # 'geolocation_url': geolocation_url,
        'plan': plan,
        'data': data,
        'rrr':data,
        'authenticated_user': authenticated_user,
        # 'response':response,
        # 'location':location,

    }   


    # if data.get('country', '') != 'IN':
    return render(request, 'login/view_plan.html',context)
    # else:     
    #     return render(request, 'login/view_plan_dollar.html',context)
    




from django.http import JsonResponse
import requests
import json


import requests

def get_geolocation_data(request):
    # Get the client's IP address from the request object
    client_ip = request.META.get('REMOTE_ADDR', '')
    print('client_ip',client_ip)

    try:
        # Use a geolocation API to get the approximate location based on the client's IP address
        response = requests.get(f'https://ipinfo.io/{client_ip}/json', timeout=5)
        data = response.json()
        location = data.get('city', '') + ', ' + data.get('region', '') + ', ' + data.get('country', '')
        print('Location:', location)
        print('Country:', data.get('country'))
    except Exception as e:
        location = 'Error: Unable to fetch location'
        print('Error while fetching location:', str(e))

    return render(request, 'login/view_plan_dollar.html', {'ip_address': client_ip, 'location': location})



# original
# def astro_my_customers(request):
#     data1 = GurujiUsers.objects.get(email_id=request.user.email_id)
#     data = Comment.objects.filter(astro_email_id=data1.email_id)
#     print('lllll', data1)
#     print('22222', data)

#     customers = []
#     for comment in data:
#         if comment.astro_email_id == data1.email_id:
#             try:
#                 matching_user = GurujiUsers.objects.get(email_id=comment.user)
#                 customer = {
#                     'first_name': matching_user.first_name,
#                     'last_name': matching_user.last_name,
#                     'birth_place': matching_user.birth_place,
#                     'birth_time': matching_user.birth_time,
#                 }
#                 customers.append(customer)
#             except GurujiUsers.DoesNotExist:
#                 pass

#     return render(request, 'login/astro_my_customer.html', {'customers': customers})

# error unound
# def astro_my_customers(request):
#     data1 = GurujiUsers.objects.get(email_id=request.user.email_id)
#     data = Comment.objects.filter(astro_email_id=data1.email_id)
#     print('data1',data1)
#     print('data',data)
    
#     # Create a set to store unique customer email IDs
#     unique_customers = set()

#     customers = []
#     for comment in data:
#         if comment.user != data1.email_id:  # Avoid adding the astrologer to the list
#             if comment.user not in unique_customers:  # Check if the customer is unique
#                 unique_customers.add(comment.user)  
#                 print('klklkk',comment.user)
#                 count = len(unique_customers)

#                 try:
#                     matching_user = GurujiUsers.objects.get(email_id=comment.user)
#                     customer = {    
#                         'first_name': matching_user.first_name,
#                         'last_name': matching_user.last_name,
#                         'birth_place': matching_user.birth_place,
#                         'birth_time': matching_user.birth_time,
#                     }
#                     customers.append(customer)
#                 except GurujiUsers.DoesNotExist:
#                     pass

#     return render(request, 'login/astro_my_customer.html', {'customers': customers,'count':count})


# def ask_ques_otp(request):
#     error_message = ""
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_name = GurujiUsers.objects.filter(whatsapp_no = user_id)
#         for i in user_name:
#             i.first_name
#             i.last_name
#             name = i.first_name + " " + i.last_name
#     	# print('llllll',name)

#         # Check if user_id is an email
#         if '@' in user_id:
#             try:
#                 user = GurujiUsers.objects.get(email_id=user_id)
#                 print('llllll',user)
#             except GurujiUsers.DoesNotExist:
#                 user = None
#         else:   
#             try:
#                 user = GurujiUsers.objects.get(whatsapp_no=user_id)
#             except GurujiUsers.DoesNotExist:
#                 user = None

#         if user is not None and user.is_customer:
#             # Generate OTP and store it in the session
#             otp = get_random_string(length=6, allowed_chars='0123456789')
#             request.session['login_otp'] = otp
#             print('otp',otp)
#             request.session['login_user_id'] = user_id

#             # Send the OTP to the user's email
#             subject = 'Login OTP'
#             message = f"Dear user,\n\nYour OTP for login is: {otp}\n\nPlease enter this OTP to log in to your account.\n\nThank you!"
#             message = render_to_string('login/otp_email.html', {'otp': otp})
#             print('aparna',message)
#             send_mail(subject, message, 'your-email@example.com', [user.email_id], fail_silently=False)

#             # otp_login_sms([user_id],name,otp)


#             # Redirect to OTP verification page
#             return redirect('/otp_verification_before/')
#         else:
#             error_message = 'Invalid Phone Number'

#     return render(request, 'login/customer_otp_before.html', {'error_message': error_message})      



from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def ask_ques_otp(request):
    error_message = ""
    if request.method == 'POST':
        # user_id = request.POST.get('user_id')
        # user_name = ""
        # name = user_name.first_name + " " + user_name.last_name if user_name else ""
        user_id = request.POST.get('user_id')
        user_name = GurujiUsers.objects.filter(email_id=user_id).first()
        name = user_name.first_name + " " + user_name.last_name if user_name else ""


        # Check if user_id is an email or phone number
        if '@' in user_id:
            try:
                user = GurujiUsers.objects.get(email_id=user_id)
                user_name = f"{user.first_name} {user.last_name}"
            except GurujiUsers.DoesNotExist:
                user = None
        else:
            try:
                user = GurujiUsers.objects.get(whatsapp_no=user_id)
                user_name = f"{user.first_name} {user.last_name}"
            except GurujiUsers.DoesNotExist:
                user = None

        if user_name is None:
            # User is not registered, set an error message
            error_message = "User is not registered. Please sign up first."


        elif user is not None and user.is_customer:
            # Generate OTP and store it in the session
            otp = get_random_string(length=6, allowed_chars='0123456789')
            request.session['login_otp'] = otp
            request.session['login_user_id'] = user_id

            # Render the email content with user's name and OTP
            # email_content = render_to_string('login/otp_email.html', {'user_name': user_name, 'otp': otp})

            # Send the OTP to the user's email
            subject = 'Login OTP'
            message = f"Dear {name},\n\nYour OTP for login is: {otp}\n\nPlease enter this OTP to log in to your account.\n\nThank you!"

            send_mail(subject,message, 'your-email@example.com', [user.email_id], fail_silently=False)

            # Redirect to OTP verification page
            return redirect('/otp_verification_before/')

        else:
            error_message = 'Invalid Email Id'

    return render(request, 'login/customer_otp_before.html', {'error_message': error_message})






@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def astro_my_customers(request):
    data1 = GurujiUsers.objects.get(email_id=request.user.email_id)
    data = Comment.objects.filter(astro_email_id=data1.email_id)
    print('data1',data1)
    print('data',data)
    
    # Create a set to store unique customer email IDs
    unique_customers = set()

    customers = []
    for comment in data:
        if comment.user != data1.email_id:  # Avoid adding the astrologer to the list
            if comment.user not in unique_customers:  # Check if the customer is unique
                unique_customers.add(comment.user)  
                print('klklkk',comment.user)
                try:
                    matching_user = GurujiUsers.objects.get(email_id=comment.user)
                    customer = {    
                        'first_name': matching_user.first_name,
                        'last_name': matching_user.last_name,
                        'birth_place': matching_user.birth_place,
                        'birth_time': matching_user.birth_time,
                    }
                    customers.append(customer)
                except GurujiUsers.DoesNotExist:
                    pass
    unique_customer_count = len(unique_customers)

    return render(request, 'login/astro_my_customer.html', {'customers': customers,'unique_customer_count':unique_customer_count})



def customer_bill(request):
     data1=Plan_Purchase.objects.filter(cust_email_id=request.user.email_id)
     context={
         "data1":data1
     }
     return render (request,'login/customer_bill.html',context)  


def bill(request,id):
     data=Plan_Purchase.objects.get(id=id)
     print("dfghj",data,data.name)
     context={
         "data":data
     }
     return render (request,'login/customer_billview.html',context)  


@login_required(login_url=settings.ASTROLOGER_LOGIN_URL)
@never_cache
def astrologer_payment(request):
    data3=Plan_Purchase.objects.all()
    data4=GurujiUsers.objects.all()
    comment= Comment.objects.filter(astro_email_id=request.user.email_id)
    cust_set = set()
    for i in comment:
        cust_data = (i.order_id,i.cust_name,i.plan_name,i.plan_purchase_date,i.astro_email_id,i.user,i.plan_amount,i.astro_commision)
        
        if cust_data not in cust_set:
            print('cust_data',cust_data)
            cust_set.add(cust_data)
    # sorted_cust_set = sorted(cust_set, key=lambda x: x[3], reverse=True)

    

   

    total_commision1 = 0
    for j in cust_set:
        total_commision1 += j[7]


    data2 = len(list(cust_set)) 
    data = list(cust_set)
    total_commision = 0
    for k in data:
        commision = GurujiUsers.objects.filter(email_id = k[4])
        for j in commision:
                print('111111111111111',j.commision)  
                # total_commision += (float(k[6])*j.commision)/100
        print(total_commision)
        print(commision)


    print('total_customer',data2)
    return render (request,'login/astrologer_payment.html',{'cust_set':cust_set,'data3':data3,'data2':data2,'commision':commision})   


from django.db.models import Count

def monthly(request):
    # Get unique values of plan_month and their counts
    unique_months = Comment.objects.values('plan_month').annotate(month_count=Count('plan_month')).distinct()
    
    return render(request, 'login/month.html', {'unique_months': unique_months})


def monthly_commission(request, plan_month):
    data = Comment.objects.filter(plan_month=plan_month,astro_email_id=request.user.email_id)
    cust_set = set()
    for i in data:
        cust_data = (i.order_id,i.cust_name,i.plan_name,i.plan_purchase_date,i.astro_email_id,i.user,i.plan_amount,i.astro_commision)
        
        if cust_data not in cust_set:
            print('cust_data',cust_data)
            cust_set.add(cust_data)
    # sorted_cust_set = sorted(cust_set, key=lambda x: x[3], reverse=True)

    data2 = len(list(cust_set)) 
    data_list = list(cust_set)
    commision = 0
    total_commision = 0
    for k in data_list:
        commision = GurujiUsers.objects.filter(email_id = k[4])
        for j in commision:
                print('111111111111111',j.commision)  
                total_commision += j.commision
                # total_commision += (float(k[6])*j.commision)/100
        print(commision)


    print('total_customer',data2)

    # total_commission = sum(i.astro_commision for i in data)
    for i in data:
        print('aaaaa',i.plan_id,i.order_id)
    context={'data':data,'commision':commision,'total_commision':total_commision}
    return render(request, 'login/monthly_commission.html', context)


def kundli(request):
     return render(request,'login/kundli.html')

# def horoscope(request):
#     return render(request,'login/horoscope.html')


# def papasamaya_view(request):
#     # Replace 'YOUR_API_KEY' with your actual API key
#     api_key = 'c293c846-c50f-5ec6-9f80-1eaa0576dff3'
#     if request.method == 'POST':
#         # data.first_name =request.POST.get('first_name')
#         # data.last_name =request.POST.get('last_name')
#         name = request.POST.get('name') 
#         email = request.POST.get('email')
#         mobile_no = request.POST.get('mobile_no')
#         # category = request.POST.get('category')
#         # name = request.POST.get('name')
#         # name = request.POST.get('name')  
#         # whatsapp_no = request.POST.get('whatsapp_no')

#     # Get the parameters from the request 
#     name=request
#     dob = request.GET.get('dob')
#     tob = request.GET.get('tob')
#     lat = request.GET.get('lat')
#     lon = request.GET.get('lon')
#     tz = request.GET.get('tz')
#     lang = request.GET.get('lang','en')
#     subcategory= request.GET.get('subcategory')

#     # Define the API URL
#     api_url = f"https://api.vedicastroapi.com/v3-json/horoscope/{subcategory}?api_key={api_key}&dob={dob}&tob={tob}&lat={lat}&lon={lon}&tz={tz}&lang={lang}"

#     try:
#         # Make a GET request to the API
#         response = requests.get(api_url)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Parse the JSON response
#             data = response.json()
            
#             # You can process the data as needed

#             # Return the data as a JSON response
#             return JsonResponse(data)
#         else:
#             # Handle the case where the API request failed
#             return JsonResponse({'error': 'Failed to retrieve data from the API'}, status=500)
#     except Exception as e:
#         # Handle any exceptions that may occur during the request
#         return JsonResponse({'error': str(e)}, status=500)
    
# def panchang(request):
#     return render(request,'login/panchang.html')

# def panchang_view1(request):
#     try:
#         # Extract parameters from the request
#         date = request.GET.get('date')
#         subcategory= request.GET.get('subcategory')
        
#         lat = request.GET.get('lat')
#         lon = request.GET.get('lon')
#         tz = request.GET.get('tz')
#         print('lllll',tz)
#         time = request.GET.get('time')
        

#         lang = request.GET.get('lang', 'en')
#         api_key = 'c293c846-c50f-5ec6-9f80-1eaa0576dff3'  # Replace with your actual API key

#         # Check if all required parameters are provided
#         if date and time and lat and lon and tz and lang:
#             # Construct the API URL with the extracted parameters
#             url = f"https://api.vedicastroapi.com/v3-json/panchang/{subcategory}?api_key={api_key}&date={date}&tz={tz}&lat={lat}&lon={lon}&time={time}&lang={lang}"
#             response = requests.get(url)

#                         # Check if the request was successful (status code 200)
#             if response.status_code == 200:
#                 data = response.json()
#                 return JsonResponse(data, safe=False)
#             else:
#                 return JsonResponse({'error': 'Failed to fetch data from the API.'}, status=500)
#         else:
#             return JsonResponse({'error': 'Missing one or more parameters.'}, status=400)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)


# def api_panchang_form(request):
#     # timezones = [tz for tz in pytz.all_timezones]
#     return render(request, 'panchang_display.html')



import requests
from django.http import JsonResponse, HttpResponse

def papasamaya_view(request):
        dob = request.GET.get('dob', '25/10/2023')
        tob = request.GET.get('tob')  # Use the default date if "dob" is not provided
        lat = request.GET.get('lat','1')
        lon = request.GET.get('lon','1')
        tz = request.GET.get('tz',9)
        lang = request.GET.get('lang', 'en')
        subcategory = request.GET.get('subcategory')
        api_key = 'c293c846-c50f-5ec6-9f80-1eaa0576dff3'  # Replace with your actual API key

        # Check if all required parameters are provided
        if subcategory == 'planet-details':
           url = f'https://api.vedicastroapi.com/v3-json/horoscope/planet-details?dob={dob}&tob={tob}&lat={lat}&lon={lon}&tz={tz}&api_key={api_key}&lang={lang}'
        elif subcategory == 'ashtakvarga':
            url = f"https://api.vedicastroapi.com/v3-json/horoscope/ashtakvarga?api_key={api_key}&date={dob}&tob={tob}&tz={tz}&lat={lat}&lon={lon}&lang={lang}"
        elif subcategory == 'binnashtakvarga':
             url = f"https://api.vedicastroapi.com/v3-json/horoscope/binnashtakvarga?api_key={api_key}&date={dob}&tz={tz}&lat={lat}&lon={lon}&lang={lang}"
        elif subcategory == 'planet-report':
            url = f"https://api.vedicastroapi.com/v3-json/panchang/planet-report?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # elif subcategory == 'moon-phase':
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/moon-phase?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # # elif subcategory == 'choghadiya-muhurta':
            
        # #     url = f"https://api.vedicastroapi.com/v3-json/panchang/choghadiya-muhurta?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
        # elif subcategory == 'hora-muhurta':
            
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/hora-muhurta?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # elif subcategory == 'moonset':
            
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/moonset?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # elif subcategory == 'solarnoon':
            
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/solarnoon?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # elif subcategory == 'sunrise':
            
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/sunrise?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # elif subcategory == 'sunset':
            
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/sunrise?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # elif subcategory == 'retrogrades':
            
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/retrogrades?api_key={api_key}&date={dob}&tz={tz}&lang={lang}"
        # elif subcategory == 'moon-rise':
            
        #     url = f"https://api.vedicastroapi.com/v3-json/panchang/moonrise?api_key={api_key}&date={dob}&tz={tz}&lat={lat}&lon={lon}&lang={lang}"
        else:
            return JsonResponse({'error': 'Invalid subcategory'}, status=400)

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()["response"]
            context = {
                'data': data,
                'error': None,
            }
            return render(request, 'login/kundli_horoscop.html', context)
        
            
        
        else:
            return JsonResponse({'error': 'Failed to retrieve data'}, status=500)



from django.shortcuts import render
from django.utils import timezone
import pytz

def api_request_form(request):
    timezones = [tz for tz in pytz.all_timezones]
    return render(request, 'login/api_request_template.html',{'timezones': timezones})

def before_api_request_form(request):
    timezones = [tz for tz in pytz.all_timezones]
    return render(request, 'login/before_api_request_template.html',{'timezones': timezones})


from django.http import JsonResponse
import requests

def panchang(request):
    # api_key = 'c293c846-c50f-5ec6-9f80-1eaa0576dff3'
    # date = request.GET.get('date')
    # print('date',type(date))
    # tz = request.GET.get('tz')
    # lat = request.GET.get('lat','1')
    # lon = request.GET.get('lon','1')
    # time = request.GET.get('time', '05:20')
    # lang = request.GET.get('lang', 'en')
    # planet = request.GET.get('planet','Moon')
    # year = request.GET.get('year','2023')
    # subcategory = request.GET.get('subcategory', '')

    # if subcategory == 'panchang':
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/panchang?api_key={api_key}&date={date}&tz={tz}&lat={lat}&lon={lon}&time={time}&lang={lang}"
    # elif subcategory == 'monthly-panchang':
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/monthly-panchang?api_key={api_key}&date={date}&tz={tz}&lat={lat}&lon={lon}&time={time}&lang={lang}"
    # elif subcategory == 'sunset':
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/sunset?api_key={api_key}&date={date}&tz={tz}&lat={lat}&lon={lon}&time={time}&lang={lang}"
    # elif subcategory == 'moon-calendar':
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/moon-calendar?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # elif subcategory == 'moon-phase':
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/moon-phase?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # # elif subcategory == 'choghadiya-muhurta':
        
    # #     url = f"https://api.vedicastroapi.com/v3-json/panchang/choghadiya-muhurta?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # elif subcategory == 'hora-muhurta':
        
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/hora-muhurta?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # elif subcategory == 'moonset':
        
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/moonset?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # elif subcategory == 'solarnoon':
        
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/solarnoon?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # elif subcategory == 'sunrise':
        
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/sunrise?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # elif subcategory == 'sunset':
        
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/sunrise?api_key={api_key}&date={date}&tz={tz}&lang={lang}"
    # elif subcategory == 'retrogrades':
        
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/retrogrades?api_key={api_key}&date={date}&tz={tz}&lang={lang}&year={year}&planet={planet}"
    # elif subcategory == 'moonrise':
        
    #     url = f"https://api.vedicastroapi.com/v3-json/panchang/moonrise?api_key={api_key}&date={date}&tz={tz}&lat={lat}&lon={lon}&lang={lang}"
    # else:
    #     return JsonResponse({'error': 'Invalid subcategory'}, status=400)

    # response = requests.get(url)

    # if response.status_code == 200:
    #     data = response.json()["response"]
    #     context = {
    #         'data': data,
    #         'error': None,
    #     }
    #     return render(request, 'login/kundli1_panchang.html', context)
        
       
    # else:
    #     return JsonResponse({'error': 'Failed to retrieve data'}, status=500)

    return render(request, 'login/panchange_login.html')


def panchang_one(request):
    return render (request,'login/kundli_panchang.html')



def save_enquiry(request):
    if request.method == 'POST':
        contact_person = request.POST.get('contact_person')
        contact_phone = request.POST.get('contact_phone')
        contact_email = request.POST.get('contact_email')
        en = Contact(contact_person=contact_person,contact_phone=contact_phone,contact_email=contact_email)
        en.save()
        print(contact_person,contact_phone,contact_phone)
        messages.success(request, 'Data saved successfully.') 
        
    return render(request,'login/home.html')



# horoscope/views.py
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render



def aries_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=1"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request, 'zodiac/aries_daily.html', {'horoscope': horoscopes})

def before_aries_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=1"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request, 'zodiac/before_aries_daily.html', {'horoscope': horoscopes})

def taurus_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=2"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/taurus_daily.html",{'horoscope': horoscopes})

def before_taurus_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=2"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_taurus_daily.html",{'horoscope': horoscopes})


def gemini_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=3"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/gemini_daily.html",{'horoscope': horoscopes})

def before_gemini_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=3"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_gemini_daily.html",{'horoscope': horoscopes})

def cancer_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=4"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/cancer_daily.html",{'horoscope': horoscopes})

def before_cancer_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=4"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_cancer_daily.html",{'horoscope': horoscopes})


def leo_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=5"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/leo_daily.html",{'horoscope': horoscopes})

def before_leo_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=5"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_leo_daily.html",{'horoscope': horoscopes})

def virgo_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=6"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/virgo_daily.html",{'horoscope': horoscopes})

def before_virgo_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=6"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_virgo_daily.html",{'horoscope': horoscopes})
    
def libra_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=7"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/libra_daily.html",{'horoscope': horoscopes})

def before_libra_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=7"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_libra_daily.html",{'horoscope': horoscopes})


def scorpio_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=8"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/scorpio_daily.html",{'horoscope': horoscopes})

def before_scorpio_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=8"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_scorpio_daily.html",{'horoscope': horoscopes})


def sagittarius_daily(request):

    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=9"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/sagittarius_daily.html",{'horoscope': horoscopes})

def before_sagittarius_daily(request):

    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=9"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_sagittarius_daily.html",{'horoscope': horoscopes})

def capricorn_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=10"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/capricorn_daily.html",{'horoscope': horoscopes})

def before_capricorn_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=10"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_capricorn_daily.html",{'horoscope': horoscopes})

def aquarius_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=11"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/aquarius_daily.html",{'horoscope': horoscopes})

def before_aquarius_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=11"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_aquarius_daily.html",{'horoscope': horoscopes})

def pisces_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=12"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/pisces_daily.html",{'horoscope': horoscopes})

def before_pisces_daily(request):
    horoscopes = {}
    
    days = ['yesterday', 'today', 'tomorrow']
    for day in days:
        url = (
            f"https://www.horoscope.com/us/horoscopes/general/"
            f"horoscope-general-daily-{day}.aspx?sign=12"
        )
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        horoscope_text = soup.find("div", class_="main-horoscope").p.text
        horoscopes[day] = horoscope_text.split('-',1)[1].strip()

    return render(request,"zodiac/before_pisces_daily.html",{'horoscope': horoscopes})





def aries_monthly(request):
    return render(request,"zodiac/aries_monthly.html")

def taurus_monthly(request):
    return render(request,"zodiac/taurus_monthly.html")

def gemini_monthly(request):
    return render(request,"zodiac/gemini_monthly.html")

def cancer_monthly(request):
    return render(request,"zodiac/cancer_monthly.html")

def leo_monthly(request):
    return render(request,"zodiac/leo_monthly.html")

def virgo_monthly(request):
    return render(request,"zodiac/virgo_monthly.html")

def libra_monthly(request):
    return render(request,"zodiac/libra_monthly.html")

def scorpio_monthly(request):
    return render(request,"zodiac/scorpio_monthly.html")

def sagittarius_monthly(request):
    return render(request,"zodiac/sagittarius_monthly.html")

def capricorn_monthly(request):
    return render(request,"zodiac/capricorn_monthly.html")

def aquarius_monthly(request):
    return render(request,"zodiac/aquarius_monthly.html")

def pisces_monthly(request):
    return render(request,"zodiac/pisces_monthly.html")




def aries_weekly(request):
    return render(request,"zodiac/aries_weekly.html")

def taurus_weekly(request):
    return render(request,"zodiac/taurus_weekly.html")

def gemini_weekly(request):
    return render(request,"zodiac/gemini_weekly.html")

def cancer_weekly(request):
    return render(request,"zodiac/cancer_weekly.html")

def leo_weekly(request):
    return render(request,"zodiac/leo_weekly.html")

def virgo_weekly(request):
    return render(request,"zodiac/virgo_weekly.html")

def libra_weekly(request):
    return render(request,"zodiac/libra_weekly.html")

def scorpio_weekly(request):
    return render(request,"zodiac/scorpio_weekly.html")

def sagittarius_weekly(request):
    return render(request,"zodiac/sagittarius_weekly.html")

def capricorn_weekly(request):
    return render(request,"zodiac/capricorn_weekly.html")

def aquarius_weekly(request):
    return render(request,"zodiac/aquarius_weekly.html")

def pisces_weeekly(request):
    return render(request,"zodiac/pisces_weekly.html")


def love(request):
    return render(request,"login/love.html")

def career(request):
    return render(request,"login/career.html")

def luck(request):
    return render(request,"login/luck.html")

def love_login(request):
    return render(request,"login/love_login.html")

def career_login(request):
    return render(request,"login/career_login.html")

def luck_login(request):
    return render(request,"login/luck_login.html")


from django.shortcuts import render, redirect
from django.core.mail import send_mail
import random

def generate_random_otp():
    return ''.join(random.choices('0123456789', k=6))

# def send_email_otp(request):
#     if request.method == 'POST':
#             remail = request.POST.get('email')
#             otp = generate_random_otp()  # Call the function to generate OTP
#             print("Generated OTP:", otp)

#             subject = 'Registration Confirmation'
#             message = f'Hello,\n\nThank you for registering on our website.\nYour OTP is {otp}\nBest regards,\n Jyotish Juction'
#             from_email = settings.EMAIL_HOST_USER
#             print(from_email, remail, "From_email is:  and remail: ")  # Replace this with your desired 'from' email address
#             recipient_list = [remail]
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)

#         # Redirect to a success page (adjust the URL as needed)
#             return redirect('/cus_validate_otp/')

#     return render(request, 'register.html')



def send_email_otp(request):
    error_message = ""
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_name = GurujiUsers.objects.filter(email_id=user_id).first()
        name = user_name.first_name + " " + user_name.last_name if user_name else ""

        # Check if user_id is an email
        if '@' in user_id:
            try:
                user = GurujiUsers.objects.get(email_id=user_id)
            except GurujiUsers.DoesNotExist:
                user = None
        else:
            try:
                user = GurujiUsers.objects.get(whatsapp_no=user_id)
            except GurujiUsers.DoesNotExist:
                user = None

        if user is not None and user.is_customer:
            # Generate OTP and store it in the session
            otp = get_random_string(length=6, allowed_chars='0123456789')
            request.session['login_otp'] = otp
            request.session['login_user_id'] = user_id

            # Send the OTP to the user's email as plain text
            subject = 'Login OTP'
            message = f"Dear {name},\n\nYour OTP for login is: {otp}\n\nPlease enter this OTP to log in to your account.\n\nThank you!"
            send_mail(subject, message, 'your-email@example.com', [user.email_id], fail_silently=False)

            # otp_login_sms([user_id], name, otp)

            # Redirect to OTP verification page
            return redirect('/otp-verification/')
        else:
            error_message = 'Invalid Phone Number'

    return render(request, 'login/customer_otp_login.html', {'error_message': error_message})

def more_reviews(request):
    
    users_with_ratings = GurujiUsers.objects.exclude(Q(review_comments1='') | Q(review_star1=''))
    
    return render(request,'login/more_reviews.html',{'users':users_with_ratings})
 
def more_reviews_login(request):

    users_with_ratings = GurujiUsers.objects.exclude(Q(review_comments1='') | Q(review_star1=''))

    return render(request,'login/more_reviews_login.html',{'users':users_with_ratings})




from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from openai import OpenAI

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
import os
# openai_api_key = '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'
# openai.api_key = openai_api_key
client = OpenAI()
OpenAI.api_key = os.getenv('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')

def ask_openai(message):
    response = client.completions.create(
    model="text-davinci-003",  
    # model = "gpt-3.5-turbo",
    prompt=f"You are an helpful assistant.\nUser: {message}",
    temperature=0.9,
    max_tokens=150,
    stop=["\n"]
)

    answer = response.choices[0].text.strip()
    if "AI" in answer:
        answer = answer.replace("AI", "Jyotish Junction")
    return answer

def chatbot(request):
    chats = GurujiUsers.objects.filter(email_id=request.user.email_id)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        print('55555555555555555555555555',chat.response)
        return JsonResponse({'message': message, 'response': response})
        
    return render(request, 'login/chatbot.html', {'chats': chats})


# import openai 
# APIKEY = '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'
# openai.api_key = APIKEY
# assistant_run = True
# while assistant_run:
#     human = input("\n\nHuman: ")
#     chat_with_ai = human + "AI: "
#     response =  openai.Completion.create(
#         model = "text-davinci-003",
#         prompt = f"You are an AI Assistant.{chat_with_ai}",
#         temperature = 0.9,
#         max_tokens = 150,
#         stop = ["AI:","Human:"]
#     )
#     print(f"\n\nAI: {response.choices[0]['text']}")
