from django.urls import path, include
from Business_setting.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static 
from login import views
from admin_app.views import *

 
urlpatterns = [
    path('admin-login/', admin_login_view, name="admin-login"),
    path('view-profile/<int:id>/',view_profile,name = 'view-profile'),   
    path('admin-profile/', UserEditViewAdmin,name="admin-profile"),  
    path('dash_admin/',dashboard_admin,name='dash_admin'),
    path('astro_admin_approved/',astro_admin_approved, name="astro_admin_approved"),
    path('admin_approval_astro/',admin_approval_astro, name="admin_approval_astro"),   
    path('approve_astrologer/<int:user_id>/',approve_astrologer, name='approve_astrologer'),
    path('admin_revenue/', admin_revenue,name="admin_revenue"),
 
    path('customer_admin/',customer_admin, name="customer_admin"),  
    path('cust_pay_admin/',cust_pay_admin, name="cust_pay_admin"),
    path('admin-logout/', logout_admin,name="admin-logout"),
    path('changepass_admin/', changepass_admin,name="changepass_admin"),
    path('customer_disable/<int:id>/', customer_disable,name="customer_disable"),
    path('astro_disable/<int:id>/', astro_disable,name="astro_disable"),

    path('customer-profile/<int:id>/', UserEditView,name="customer-profile"),
    path('astro_profile/<slug:id>/', commisionastro,name="astro_profile"), 
    path('cus_to_ad_question/', cus_to_ad_question,name="cus_to_ad_question"),  

    path('astro_payment/<int:id>/', astro_payment,name="astro_payment"),
    path('cust_to_admin/',customer_to_admin,name='cust_to_admin'),
    path('admin_view_que/<int:id>/', admin_view_que,name="admin_view_que"),
    path('approved-question-admin/<int:user>/',approved_question_admin,name='approved-question-admin'),
    #path('astro_payment/', astro_payment,name="astro_payment"),
    path('monthly_admin/<str:astro_email_id>/', monthly_admin,name="monthly_admin"),
    path('monthly_commission_admin/<str:astro_email_id>/<str:plan_month>/', monthly_commission_admin,name="monthly_commission_admin"),





]