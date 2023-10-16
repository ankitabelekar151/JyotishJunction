"""guruspeaks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')  
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 

from django.contrib import admin
from django.urls import path,include     
from login import views    
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('ask_ques_login/',views.ask_ques_login,name="ask_ques_login"),
    path('ask_ques_signup/',views.ask_ques_signup,name="ask_ques_signup"), 
    path('customer-recharge/<int:paisa>/',views.customer_recharge,name="customer-recharge"),
    
    path('astrologer-registration/', views.astrologer_signup, name="astrologer-registration"), 
    path('ask_ques_otp/', views.ask_ques_otp, name="ask_ques_otp"),

    path('pass/', views.passs, name="pass"), 
    path('check-status/', views.check_status, name="check-status"),
    # path('stripeeeee-pay/<int:paisa>/', views.home_page_view, name='stripe-pay'), 
    # path('charge/', views.charge_view, name='charge'), 
    # path('success/',views.success_view,name="success"),
    path('ram/',views.ram,name="ram"),


    path('stripe-pay/<int:paisa>/', views.product_landing_page_view, name='stripe-pay'),
    path('create-checkout-session/<int:paisa>/', views.create_checkout_session_view, name='create-checkout-session'),
    path('cancel/', views.cancel_view, name='cancel'),
    path('success/', views.success_view, name='success'),

    
    path('customer-registration/',views.customer_signup,name="customer-registration"), 
    path('delete_customer/',views.delete_customer,name='delete_customer'),
    

    path('customer-login-otp/', views.customer_login_otp, name="customer-login-otp"),


    path('update_silver_dash/',views.update_silver_dash,name='update_silver_dash'),
    path('popup/', views.popup, name='popup'),

    path('update_gold_dash/',views.update_gold_dash,name='update_gold_dash'),

    path('update_platinum_dash/',views.update_platinum_dash,name='update_platinum_dash'),
    
    path('dash_customer1/',views.dash_customer1,name='dash_customer1'),
    
    path('verify_otp_view/',views.verify_otp_view,name='verify_otp_view'),
    # path('set_new_password_view',views.set_new_password_view,name='set_new_password_view'),
    path('set-new-password/', views.set_new_password_view, name='set-new-password'),



    path('initiate_payment/', views.initiate_phonepe_payment, name='initiate_payment'),


    path('astrologer_forgotpass/', views.astrologer_forgot_pass_view,name="astrologer_forgot-password"),
    path('astrologer_forgotsuccess/', views.astrologer_forgotsuccess,name="astrologer_forgotsuccess"),

    path('',views.home_view,name='home_view'),


    path('error_email/',views.error_email,name='error_email'),
    path('error_mobile/',views.error_mobile,name='error_mobile'),  
    
    path('order_histroy/',views.order_histroy,name='order_histroy'),
    path('otp_verification_before/', views.otp_verification_before, name='otp_verification_before'),



    path('plan_error_message/', views.plan_error_message, name="plan_error_message"),
    path('astrologer-login/', views.astrologer_login_view, name="astrologer-login"),
    path('customer-login/', views.customer_login_view, name="customer-login"),

    path('customer-wallet/',views.customer_wallet,name='customer-wallet'),

    path('customer_wallet/',views.particular_customer_wallet,name='customer_wallet'),

    path('customer-payments/',views.customer_payment,name='customer-payments'),


    path('update_silver/',views.update_silver,name='update_silver'),

    path('update_gold/',views.update_gold,name='update_gold'),
    path('update_platinum/',views.update_platinum,name='update_platinum'),

    



    path('get_geolocation_data/', views.get_geolocation_data, name='get_geolocation_data'),


    path('customer_support/', views.customer_support, name='customer_support'),





    path('otp-verification-astro/', views.otp_verification_view_astro, name='otp-verification-astro'),

    path('astro-login-otp/', views.astro_login_otp, name="astro-login-otp"),
    path('astrologer_payment/',views.astrologer_payment, name="astrologer_payment"),

    path('monthly_commission/<str:plan_month>/',views.monthly_commission,name='monthly_commission'), 
    path('monthly/', views.monthly, name='monthly'),


    
    path('ask_question_silver/',views.ask_question_silver,name='ask_question_silver'),
    path('ask_question_gold/',views.ask_question_gold,name='ask_question_gold'),
    path('ask_question_platinum/',views.ask_question_platinum,name='ask_question_platinum'),



    path('ask_q_silver/<int:id>/',views.ask_q_silver,name='ask_q_silver'),
    path('ask_q_gold/<int:id>/',views.ask_q_gold,name='ask_q_gold'),
    path('ask_q_platinum/<int:id>/',views.ask_q_platinum,name='ask_q_platinum'),

    
    path('ques_app_silver/<int:id>/',views.ques_app_silver,name='ques_app_silver'),
    path('ques_app_gold/<int:id>/',views.ques_app_gold,name='ques_app_gold'),
    path('ques_app_platinum/<int:id>/',views.ques_app_platinum,name='ques_app_platinum'),

    path('delete-question-silver/<int:id>/',views.delete_question_silver,name='delete-question-silver'),
    path('delete-question-gold/<int:id>/',views.delete_question_gold,name='delete-question-gold'),
    path('delete-question-platinum/<int:id>/',views.delete_question_platinum,name='delete-question-platinum'),
   
    path('delete-que-platinum/<int:id_value>/<int:plan_value>/',views.delete_que_platinum,name="delete-que-platinum"),
    path('delete-que-gold/<int:id_value>/<int:plan_value>/',views.delete_que_gold,name="delete-que-gold"),
    path('delete-que-silver/<int:id_value>/<int:plan_value>/',views.delete_que_silver,name="delete-que-silver"),
    
    path('customer-profile/', views.UserEditView,name="customer-profile"),
    path('astro_profile/', views.UserEditViewAstro,name="astro_profile"),
    # path('admin-profile/',views.admin_profile,name = 'admin-profile'),
    path('logout/', views.logout_customer,name="logout"),
    path('logout_astro/', views.logout_astrologer,name="logout_astro"),
    path('forgotpass/', views.forgot_pass_view,name="forgot-password"),
    path('changepass/', views.changepass,name="change-success"),
    path('forgotsuccess/', views.forgotsuccess,name="forgot-success"),
    path('success/',views.success,name='success'),

   
   
    path('ad_to_astro/',views.ad_to_astro,name='ad_to_astro'),
    path('astro_reply/',views.astro_reply,name='astro_reply'),
    path('astro_reply_admin/',views.astro_reply_admin,name='astro_reply_admin'),


    path('after_login_cus/',views.after_login_cus,name='after_login_cus'),

    path('whatsapp_qr/',views.whatsapp_qr,name='whatsapp_qr'),
    


    path('view_plan/',views.view_plan,name='view_plan'),
    path('comment_view/',views.comment_view,name='comment_view'),
    path('comment_view_gold/',views.comment_view_gold,name='comment_view_gold'),
    path('customer_to_admin/',views.customer_to_admin,name='customer_to_admin'),
    path('comment_view_platinum/',views.comment_view_platinum,name='comment_view_platinum'),
    path('adcustomer_to_admin/<int:id>/',views.adcustomer_to_admin,name='adcustomer_to_admin'),
   
    path('editastro_reply/<int:id>/',views.editastro_reply,name='editastro_reply'),
    path('customer-view-answer/<int:id>/',views.customer_view_answer,name='customer-view-answer'), 


    path('select_plan/',views.comment,name='select_plan'),
    path('home',views.plan,name='home'),
    path('astro_info/',views.astro_info,name='astro_info'),
    path("", include("Business_setting.urls")),
    path("", include("Supports_faq.urls")),
    path("", include("admin_app.urls")),
    path('ckeditor', include('ckeditor_uploader.urls')), 

    path('dash_customer/',views.dash_customer,name='dash_customer'),
    # path('dash_admin/',views.dash_admin,name='dash_admin'),
    path('dash_astro/',views.dash_astro,name='dash_astro'),
    path('view_astroquestions/<str:user>/',views.view_astroquestions,name='view_astroquestions'),
    path('view_data/',views.view_data,name='view_data'),
    path('astro_my_customers/',views.astro_my_customers,name='astro_my_customers'), 

    path('astrologer_changepass/', views.astrologer_changepass,name="astrologer-change-success"),
    path('customer_bill/',views.customer_bill,name='customer_bill'),
    path('bill/<int:id>/',views.bill,name='bill'),


    # path('enable_astrologer/<slug:id>/',views.enable_astrologer,name="enable_astrologer"),
    # path('astro_admin_approved/',views.astro_admin_approved, name="astro_admin_approved"),
    path('otp-verification/', views.otp_verification_view, name='otp_verification'),


    # path('astro_admin_approved/',views.astro_admin_approved, name="astro_admin_approved"),
    # path('approve_astrologer/<int:user_id>/', views.approve_astrologer, name='approve_astrologer'),
    # path('admin_approval_astro/',views.admin_approval_astro, name="admin_approval_astro"),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
    
    # path('fail_payment/', views.fail_payment, name='fail_payment'),
    # path('rrr/', views.rrr, name='rrr'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
