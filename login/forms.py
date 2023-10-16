from django import forms
from login.models import GurujiUsers,AdminUser,AstrologerUser,CustomerUser
from django.contrib.auth.forms import UserChangeForm ,PasswordChangeForm
from django_countries.fields import CountryField
from django_countries import countries
from django_countries.widgets import CountrySelectWidget

from django import forms
#from .models import GurujiUsers

class UserData(forms.Form):
	class meta:
		model = GurujiUsers
		fields = '__all__'
                
                
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class FullCountrySelectWidget(CountrySelectWidget):
    def label_from_instance(self, country):
        return country.name

# class MyForm(forms.Form):
#     country = CountryField(blank_label='(Select country)').formfield(
#         widget=FullCountrySelectWidget(attrs={'class': 'form-control'})
#     )


class customerform(forms.ModelForm):
     
    class Meta:
        model = GurujiUsers
        fields = ['whatsapp_no','first_name', 'last_name','email_id','password'] 
        labels = {'whatsapp_no':'Mobile No'}
    def clean_country(self):
        country_code = self.cleaned_data.get('country')
        country_name = dict(countries)[country_code]
        return country_name





class Signupformcust(forms.ModelForm):
    country = CountryField(blank_label='(Select country)').formfield(widget=CountrySelectWidget(attrs={'class': 'form-control'}))
    class Meta:
        model = GurujiUsers
        fields = [ 'email_id','whatsapp_no','password']
    

 

class Signupform(forms.ModelForm):
    expertise = forms.MultipleChoiceField(
        choices=[
            ('astrology', 'Astrology'),
            ('psychic', 'Psychic'),
            ('healer', 'Healer'),
            ('numerology', 'Numerology'),
            ('tarot_reading', 'Tarot Reading'),
            ('face_reading', 'Face Reading'),
            ('palmistry', 'Palmistry'),
            ('vastu', 'Vastu'),
            ('feng_shui', 'Feng Shui'),
            ('puja_havan', 'Puja / Havan'),
            ('panchang_mahurat', 'Panchang / Mahurat')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )   
    
    languages_known = forms.MultipleChoiceField(
        choices=[
            ('english', 'English'),
            ('hindi', 'Hindi'),
            ('marathi', 'Marathi'),
            ('gujarati', 'Gujarati')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    country = CountryField(blank_label='(Select country)').formfield(widget=CountrySelectWidget(attrs={'class': 'form-control'}))
    
    class Meta:
        model = GurujiUsers
        fields = ['name','email_id','whatsapp_no','country','password','expertise', 'languages_known']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Save the selected choices as comma-separated strings
        user.expertise = ','.join(self.cleaned_data.get('expertise', []))
        user.languages_known = ','.join(self.cleaned_data.get('languages_known', []))
        
    # Convert the country code to the corresponding country name
        country_code = self.cleaned_data.get('country')
        country_name = dict(CountryField().get_choices())[country_code]
        user.country = country_name
    
        if commit:
            user.save()
        return user


# from django.core.validators import RegexValidator

# # Define the regular expression pattern for 24-hour time format
# time_format_validator = RegexValidator(
#     regex=r'^([01]\d|2[0-3]):([0-5]\d)$',
#     message='Enter a valid time in 24-hour format (hh:mm).'
# )

# class YourForm(forms.Form):
#     birth_time = forms.CharField(
#         max_length=5,
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label='Birth Time',
#         validators=[time_format_validator]
#     )

class EditProfileForm(UserChangeForm):  
    
    user_id = forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control' }),label='User ID')
    first_name = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='First Name')
   
    last_name = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Last Name')
    whatsapp_no= forms.CharField(disabled=False,max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Whatsapp No')
    dob= forms.CharField(disabled=False,max_length=240,widget=forms.TextInput(attrs={'class':'form-control','type': 'date'}),label='Date Of Birth')
    country = CountryField(blank_label='(Select country)').formfield(widget=CountrySelectWidget(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Address')
    pincode = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Pin Code')
    city = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='City')
    state = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='State')
    birth_time= forms.CharField(disabled=False,max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Birth Time')
    email_id = forms.EmailField(disabled=False,max_length=240,widget=forms.EmailInput(attrs={'class':'form-control'}),label='Email Id')
    birth_place = forms.CharField(disabled=False,max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Birth Place')
    #date_of_current_designation = forms.CharField(disabled=True,max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Date Of Current Designation')
    password =  forms.CharField(disabled=True,max_length=250,widget=forms.TextInput(attrs={'class':'form-control','type':'hidden'}),label='Password')


    class Meta:
        model = GurujiUsers
        fields = ('user_id','first_name','last_name','whatsapp_no','dob','country','address','pincode','city','state' ,'birth_time','password','email_id','birth_place')



class EditProfileFormAstro(UserChangeForm):  
    
    user_id = forms.CharField(disabled=True,widget=forms.TextInput(attrs={'class':'form-control' }),label='User ID')
    name = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Full Name')
   
    # last_name = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Last Name')
    whatsapp_no= forms.CharField(disabled=False,max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Whatsapp No')
    
    # dob= forms.CharField(disabled=False,max_length=240,widget=forms.TextInput(attrs={'class':'form-control','type': 'date'}),label='Date Of Birth')
    country = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Country')
    gender = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Gender')
    experience = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Experience')
    expertise = forms.MultipleChoiceField(
        choices=[
            ('astrology', 'Astrology'),
            ('psychic', 'Psychic'),
            ('healer', 'Healer'),
            ('numerology', 'Numerology'),
            ('tarot_reading', 'Tarot Reading'),
            ('face_reading', 'Face Reading'),
            ('palmistry', 'Palmistry'),
            ('vastu', 'Vastu'),
            ('feng_shui', 'Feng Shui'),
            ('puja_havan', 'Puja / Havan'),
            ('panchang_mahurat', 'Panchang / Mahurat')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )  

    languages_known = forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Languages Known')


    email_id = forms.EmailField(disabled=False,max_length=240,widget=forms.EmailInput(attrs={'class':'form-control'}),label='Email Id')
    about_me = forms.CharField(max_length=240,widget=forms.Textarea(attrs={'class':'form-control'}),label='About Me')
    # birth_place = forms.CharField(disabled=False,max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Birth Place')
    #date_of_current_designation = forms.CharField(disabled=True,max_length=240,widget=forms.TextInput(attrs={'class':'form-control'}),label='Date Of Current Designation')
    password =  forms.CharField(disabled=True,max_length=250,widget=forms.TextInput(attrs={'class':'form-control','type':'hidden'}),label='Password')


    class Meta:
        model = GurujiUsers
        fields = ('user_id','name','whatsapp_no','country','gender','experience','expertise','languages_known','password','email_id','about_me')        

class PasswordChangingForm(PasswordChangeForm):  
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password' }),label='Old Password', required=True)
    new_password1 = forms.CharField(max_length=240,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),label='New Password', required=True)
    new_password2 = forms.CharField(max_length=240,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),label='Confirm New Password', help_text='Must contain at least 8 characters and a special symbol.', required=True)

    class Meta:
        model = GurujiUsers
        fields = ('old_password','new_password1','new_password2') 

        
class UserChangePass(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput),
    new_pass1 = forms.CharField(max_length=240,widget=forms.PasswordInput, required=True),
    new_pass2 = forms.CharField(label='Password(again)',widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd=self.cleaned_data['new_pass1']
        valpwds=self.cleaned_data['new_pass2']

        if valpwd != valpwds:
            raise forms.ValidationError('password does not match') 

