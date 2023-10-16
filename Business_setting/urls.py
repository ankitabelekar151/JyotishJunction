
from django.urls import path, include
from Business_setting.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path("general-setting/", general_setting, name="general-setting"),
    path("privacy_policy/", privacy_policy, name="privacy_policy"),
    path("terms_of_service/", terms_of_service, name="terms_of_service"),
    path("Refund_Cancellation_Policy/", Refund_Cancellation_Policy, name="Refund_Cancellation_Policy"),
    path("intellactual_property/", intellactual_property, name="intellactual_property"),
    path("faqs/", faqs, name="faqs"),
    path("disclaimer/", disclaimer, name="disclaimer"), 
    
    path("astro_blog/", astro_blog, name="astro_blog"),
    path("astro_blog1/<int:id>/", astro_blog1, name="astro_blog1"),
    path("delete/<int:id>/", delete, name="delete"), 
    path("blogs/", blogs, name="blogs"),
    path("add_blogs/", add_blogs, name="add_blogs"),
    path("blogs_list/", blogs_list, name="blogs_list"),
    path("blogs_1/<int:id>/", blogs_1, name="blogs_1"),
    #path("blogs_1/", blogs_1, name="blogs_1"),
    path("blogs_2/", blogs_2, name="blogs_2"),
    path("blogs_3/", blogs_3, name="blogs_3"),
    path("blogs_4/", blogs_4, name="blogs_4"),
    path("blogs_5/", blogs_5, name="blogs_5"),
    path("blogs_6/", blogs_6, name="blogs_6"),
    path("customer_blogs/", customer_blogs, name="customer_blogs"),
    path("customer_blogs_1/<int:id>/", customer_blogs_1, name="customer_blogs_1"),
    path("before_login_blog/<int:id>/", before_login_blog, name="before_login_blog"),
    path("customer_blogs_right/<int:id>/", customer_blogs_right, name="customer_blogs_right"),
    
    path("customer_blogs_2/", customer_blogs_2, name="customer_blogs_2"),
    path("customer_blogs_3/", customer_blogs_3, name="customer_blogs_3"),
    path("customer_blogs_4/", customer_blogs_4, name="customer_blogs_4"),
    path("customer_blogs_5/", customer_blogs_5, name="customer_blogs_5"),
    path("customer_blogs_6/", customer_blogs_6, name="customer_blogs_6"),

    path("self-question/", self_question, name="self_question"),
    path("wealth-question/", wealth_question, name="wealth_question"),
    path("health-question/", health_question, name="health_question"),
    path("family-question/", family_question, name="family_question"),
    path("marriage-question/", marriage_question, name="marriage_question"),
    path("love-question/", love_question, name="love_question"),
    path("education-question/", education_question, name="education_question"),
    path("carrier-question/", carrier_question, name="carrier_question"),
    path("business-question/", business_question, name="business_question"),
    path("hardtime-question/", hardtime_question, name="hardtime_question"),
    path("puja-question/", puja_question, name="puja_question"),
    path("spirituality-question/", spirituality_question, name="spirituality_question"),



    
    path("after_self-question/", after_self_question, name="after_self_question"),
    path("after_wealth-question/", after_wealth_question, name="after_wealth_question"),
    path("after_health-question/", after_health_question, name="after_health_question"),
    path("after_family-question/", after_family_question, name="after_family_question"),
    path("after_marriage-question/", after_marriage_question, name="after_marriage_question"),
    path("after_love-question/", after_love_question, name="after_love_question"),
    path("after_education-question/", after_education_question, name="after_education_question"),
    path("after_carrier-question/", after_carrier_question, name="after_carrier_question"),
    path("after_business-question/", after_business_question, name="after_business_question"),
    path("after_hardtime-question/", after_hardtime_question, name="after_hardtime_question"),
    path("after_puja-question/", after_puja_question, name="after_puja_question"),
    path("after_spirituality-question/", after_spirituality_question, name="after_spirituality_question"),
    path("ask_a_question_inr/", ask_a_question_inr, name="ask_a_question_inr"),

    path("cust_refund/", cust_refund, name="cust_refund"),  
    path("cust_faq/", cust_faq, name="cust_faq"),
    path("cust_intel_property/", cust_intel_property, name="cust_intel_property"),
    path("cust_disclaimer/", cust_disclaimer, name="cust_disclaimer"),
    path("cust_privacy_policy/", cust_privacy_policy, name="cust_privacy_policy"),
    path("cust_tos/", cust_tos, name="cust_tos"),
    path("cust_refund/", cust_refund, name="cust_refund"),

    path("show_banner/", show_banner, name="show_banner"),
    path("add_banner/", add_banner, name="add_banner"),
    path("del_banner/<int:id>/", del_banner, name="del_banner"),

    

    
  

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)