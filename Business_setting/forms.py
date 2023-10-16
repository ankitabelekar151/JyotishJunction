from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
GurujiUsers = settings.AUTH_USER_MODEL
from Business_setting.models import *
 
class generalSettingForm(forms.Form):
    business_name = forms.CharField(required=True)
    business_category = forms.CharField(required=False)
    pin_code = forms.CharField(required=False)
    city = forms.CharField(required=False) 
    area = forms.CharField(required=False)
    district = forms.CharField(required=False)
    state = forms.CharField(required=False)
    address = forms.CharField(required=False)
    landline_number = forms.CharField(required=False)
    alternate_mobile_number = forms.CharField(required=False)
    company_email = forms.CharField(max_length=100, required=False)
    alternate_email = forms.CharField(max_length=100, required=False)
    aadhaar = forms.CharField(required=False)
    pan_number = forms.CharField(required=False)
    gstin = forms.CharField(required=False)
    GSTIN_certificate = forms.FileField(required=False)
    #PAN_card = forms.FileField(required=True)
    cin = forms.CharField(required=False)
    CIN_certificate = forms.FileField(required=False)
    profile_image = forms.ImageField(required=False)
    business_logo = forms.ImageField(required=False)
    