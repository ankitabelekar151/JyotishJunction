from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    use_in_migrations =True
    def _create_user(self, user_id,email_id,whatsapp_no, password,**extra_fields):
        if not user_id:
            raise ValueError("user_id Must Be Provided")
        if not password:
            raise ValueError("Password Must Be Provided")    
 
        user = self.model(
            user_id = user_id,
            email_id= email_id,
            whatsapp_no= whatsapp_no, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using  = self.db)
        admin_user = AdminUser(ad_user_id=user_id,ad_email_id=email_id,ad_whatsapp_no= whatsapp_no,is_admin=True,is_staff=True,is_user=True,is_active=True)
        admin_user.save()
        return user
    
    def create_superuser(self, user_id,email_id,whatsapp_no,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_admin',True)
        return self._create_user(user_id,email_id,whatsapp_no,password,**extra_fields)    







class GurujiUsers(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=50,blank=True,null=True,unique=True) 
    user_id = models.CharField(max_length=50,blank=True,null=True,unique=True)
    first_name = models.CharField(max_length=240,blank=True,null=True)
    last_name = models.CharField(max_length=240,blank=True,null=True)
    name = models.CharField(max_length=240,blank=True,null=True)
    email_id = models.EmailField(max_length=240,unique = True,blank=True,null=True)
    whatsapp_no = models.CharField(max_length=240,unique = True,blank=True,null=True)
    commision = models.IntegerField(default = 0,blank=True,null=True)
    languages_known=models.CharField(max_length=240,blank=True,null=True)
    country = models.CharField(max_length=240,blank=True)
    dob=models.CharField(max_length=240,blank=True,null=True)  
    birth_time=models.CharField(max_length=240,blank=True,null=True)
    birth_place=models.CharField(max_length=240,blank=True,null=True)
    astro_approve_date=models.CharField(max_length=240,blank=True,null=True)
    astro_date = models.DateField(null=True)
    astro_approve_time=models.CharField(max_length=240,blank=True,null=True)
    address = models.CharField(max_length=240,blank=True)
    city = models.CharField(max_length=240,blank=True)
    state = models.CharField(max_length=240,blank=True)
    pincode = models.IntegerField(blank=True,null=True)
    about_me = models.CharField(max_length=240,blank=True)
    bank_name=models.CharField(max_length=240,blank=True,null=True)
    account_no = models.CharField(max_length=240,blank=True,null=True)
    ifsc_no = models.CharField(max_length=240,blank=True,null=True)
    aadhar_no =models.CharField(max_length=240,blank=True,null=True)
    pan_no = models.CharField(max_length=240,blank=True,null=True)
    age=models.CharField(max_length=240,blank=True,null=True)
    review_comments1= models.CharField(max_length=500,default='', null = True, blank= True)
    review_star1 = models.CharField(max_length=50,null = True, blank= True,default='')
    agora_user_id = models.CharField(max_length=50, blank=True, null=True, unique=True)




    
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    image1 = models.ImageField(upload_to='user_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='user_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='user_images/', blank=True, null=True)
    cust_img = models.ImageField(upload_to='user_images/', blank=True, null=True)

    is_gurujiuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_astrologer = models.BooleanField(default=False)
    pending_astrologer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_disable = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    gender = models.CharField(max_length=50,blank=True,null=True)
    experience = models.CharField(max_length=50,blank=True,null=True)
    expertise = models.CharField(max_length=240,blank=True,null=True)
    is_approved = models.BooleanField(default=False)
    


    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email_id', 'whatsapp_no']
    
    class Meta:
        verbose_name = 'GurujiUsers'
    def __str__(self):
        return self.email_id





class AdminUser(models.Model):
    ad_user_id = models.CharField(max_length=50,blank=True,null=True,unique=True)
    ad_first_name = models.CharField(max_length=240,blank=True,null=True)
    ad_last_name = models.CharField(max_length=240,blank=True,null=True)
    ad_email_id = models.EmailField(max_length=240,unique = True,blank=True,null=True)
    ad_whatsapp_no = models.CharField(max_length=240,unique = True,blank=True,null=True)
    ad_country = models.CharField(max_length=240,blank=True,null=True)
    ad_dob = models.CharField(max_length=240,blank=True,null=True)
    

    is_gurujiuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_astrologer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_disable = models.BooleanField(default=False)
    objects = CustomUserManager()

    


   
class AstrologerUser(models.Model):
    aus_user_id = models.CharField(max_length=50,blank=True,null=True,unique=True)
    aus_first_name = models.CharField(max_length=240,blank=True,null=True)
    aus_last_name = models.CharField(max_length=240,blank=True,null=True)
    aus_name = models.CharField(max_length=240,blank=True,null=True)
    aus_email_id = models.EmailField(max_length=240,blank=True,null=True,unique=True)
    aus_whatsapp_no = models.CharField(max_length=240,blank=True,null=True,unique=True)
    aus_country = models.CharField(max_length=240,blank=True,null=True)     
    aus_dob = models.CharField(max_length=240,blank=True,null=True)
    languages_known=models.CharField(max_length=240,blank=True,null=True)
    

    is_gurujiuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_astrologer = models.BooleanField(default=False)
    is_pending_astrologer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_disable = models.BooleanField(default=False)
    is_question = models.BooleanField(default=False)
    objects = CustomUserManager()
    
    gender = models.CharField(max_length=50,blank=True,null=True)
    experience = models.CharField(max_length=50,blank=True,null=True)
    expertise = models.CharField(max_length=240,blank=True,null=True)



class CustomerUser(models.Model):
    cus_user_id = models.CharField(max_length=50,blank=True,null=True,unique=True)
    cus_first_name = models.CharField(max_length=240,blank=True,null=True)
    cus_last_name = models.CharField(max_length=240,blank=True,null=True)
    cus_email_id = models.EmailField(max_length=240,unique = True,blank=True,null=True)
    cus_whatsapp_no = models.CharField(max_length=240,unique = True,blank=True,null=True)
    cus_country = models.CharField(max_length=240,blank=True,null=True)
    cus_dob = models.CharField(max_length=240,blank=True,null=True)
    cus_birth_time=models.CharField(max_length=240,blank=True,null=True)
    cus_birth_place=models.CharField(max_length=240,blank=True,null=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_astrologer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_disable = models.BooleanField(default=False)  
    objects = CustomUserManager()




class admin_setting_plan(models.Model):

    plan_name_1 = models.CharField(max_length=240,blank=True,null=True)
    admin_plan_1_d = models.CharField(max_length=500,blank=True,null=True)
    amount_plan = models.CharField(max_length=500,blank=True,null=True)
    admin_plan_approve = models.BooleanField(default=False)
    customer_plane_approve = models.BooleanField(default=False)
    cus_user_id = models.CharField(max_length=50,blank=True,null=True,unique=True)
    cus_first_name = models.CharField(max_length=240,blank=True,null=True)
    cus_last_name = models.CharField(max_length=240,blank=True,null=True)
    cus_email_id = models.EmailField(max_length=240,unique = True,blank=True,null=True)
    cus_whatsapp_no = models.CharField(max_length=240,unique = True,blank=True,null=True)
    cus_country = models.CharField(max_length=240,blank=True,null=True)
    cus_dob = models.CharField(max_length=240,blank=True,null=True)
    c_comment_1= models.CharField(max_length=500,blank=True,null=True)
    a_comment_1 = models.CharField(max_length=500,blank=True,null=True)
    silver = models.BooleanField(default=False)
    gold = models.BooleanField(default=False)
    diamond = models.BooleanField(default=False)

class admin_setting_plan_dollar(models.Model):

    plan_name_1 = models.CharField(max_length=240,blank=True,null=True)
    admin_plan_1_d = models.CharField(max_length=500,blank=True,null=True)
    amount_plan = models.CharField(max_length=500,blank=True,null=True)





class generalSetting(models.Model):
    user_id = models.CharField(max_length=100,default='', null=True)
    admin_setting_id = models.CharField(max_length=500, default='',null=True)
    business_category = models.CharField(max_length=500,default='',null=True)
    business_name = models.CharField(max_length=500,default='',null=True)
    business_code = models.CharField(max_length=500,default='',null=True)
    pin_code = models.CharField(max_length=500, default='')
    city = models.CharField(max_length=500, default='')
    area = models.CharField(max_length=500, default='')
    district = models.CharField(max_length=500, default='')
    state = models.CharField(max_length=500, default='')
    address = models.CharField(max_length=500, default='')
    landline_number = models.CharField(max_length=20, default='')
    alternate_mobile_number = models.CharField(max_length=20, default='')
    company_email = models.EmailField(blank= True, default='')
    alternate_email = models.EmailField(blank= True, default='')
    aadhaar = models.EmailField(blank= True, default='')
    pan_number = models.CharField(max_length=10, default='')
    gstin = models.CharField(max_length=100, default='')
    GSTIN_certificate = models.FileField(null=True, blank=True, upload_to='astro_GSTIN_certificate', default="")
    cin =  models.CharField(max_length=100, default='')
    CIN_certificate = models.FileField(null=True, blank=True, upload_to='astro_CIN_certificate', default="")
    business_logo = models.ImageField(null=True, blank=True, upload_to='astro_business_logo', default="")


    def __str__(self):
         return self.business_name + " (" + self.area + ")"




class MerchantProfile(models.Model):
    m_user = models.ForeignKey(GurujiUsers,related_name="merchant_record", null=True, on_delete=models.CASCADE)
    admin_setting_id = models.CharField(max_length=500, default='',null=True)
    business_name = models.CharField(max_length=500,default='',null=True)
    business_code = models.CharField(max_length=500,default='',null=True)
    pin_code = models.CharField(max_length=500, default='')
    city = models.CharField(max_length=500, default='')
    area = models.CharField(max_length=500, default='')
    district = models.CharField(max_length=500, default='')
    state = models.CharField(max_length=500, default='')
    address = models.CharField(max_length=500, default='')
    landline_number = models.CharField(max_length=20, default='')
    alternate_mobile_number = models.CharField(max_length=20, default='')
    company_email = models.EmailField(blank= True, default='')
    alternate_email = models.EmailField(blank= True, default='')
    aadhaar = models.EmailField(blank= True, default='')
    pan_number = models.CharField(max_length=10, default='')
    gstin = models.CharField(max_length=100, default='')
    GSTIN_certificate = models.FileField(null=True, blank=True, upload_to='astro_GSTIN_certificate', default="")
    cin =  models.CharField(max_length=100, default='')
    CIN_certificate = models.FileField(null=True, blank=True, upload_to='astro_CIN_certificate', default="")
    business_logo = models.ImageField(null=True, blank=True, upload_to='astro_business_logo', default="")


    def __str__(self):
         return self.business_name + " (" + self.area + ")"
    



class Plan_Purchase(models.Model):
    plan_id = models.CharField(max_length=200, default='', null=True)
    name = models.CharField(max_length=200, default='', null=True)
    invoice_number = models.CharField(max_length=200, default='', null=True)
    cust_id = models.CharField(max_length=200, default='', null=True)    
    cust_email_id = models.CharField(max_length=200, default='', null=True)
    cust_whatsapp_no = models.CharField(max_length=200, default='', null=True)
    plan_name = models.CharField(max_length=200, default='', null=True)   
    plan_amount = models.CharField(max_length=200, default='', null=True) 
    cgst = models.IntegerField(default=0)
    sgst = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    questions_count = models.IntegerField(default=0)
    plan_order_id = models.CharField(max_length=200, default='', null=True)
    payment_id = models.CharField(max_length=200, default='', null=True)   
    plan_purchase_date = models.CharField(max_length=200, default='', null=True)
    purchase_date = models.DateField(null=True)
    plan_purchase_time = models.CharField(max_length=200, default='', null=True)
    plan_expiry_date = models.CharField(max_length=200, default='', null=True)
    signature_id = models.CharField(max_length=1000,default='', null = True, blank= True)   
    purchase_time = models.CharField(max_length=50,default='', null = True, blank= True)
    plan_month = models.CharField(max_length=50,default='', null = True, blank= True)
    def __str__(self):
        return f'{self.plan_name}-{self.cust_email_id}'
    



class SelectedQuestion(models.Model):
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question         


class Comment(models.Model):
    plan_id = models.CharField(max_length=200, default='', null=True)
    object_id = models.CharField(max_length=100,default='', null=True)
    order_id = models.CharField(max_length=100,default='', null=True) 
    select_cust = models.CharField(max_length=100,default='', null=True)
    ques_type = models.CharField(max_length=100,default='', null=True)
    cust_name = models.CharField(max_length=100,default='', null=True)
    user = models.CharField(max_length=100,default='', null=True)
    astro_name = models.CharField(max_length=100,default='', null=True)
    astro_email_id=models.CharField(max_length=100,default='', null=True)
    astro_commision = models.IntegerField(default=0)
    plan_name = models.CharField(max_length=100,default='', null=True)
    plan_amount = models.CharField(max_length=100,default='', null=True)
    comment1=models.CharField(max_length=5000,default='',null=True)
    comment2=models.CharField(max_length=10000,default='',null=True)
    qapprove = models.BooleanField(default=False)
    send_admin = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200, default='', null=True)  
    purchase_date = models.DateField(null=True) 
    plan_purchase_date = models.CharField(max_length=200, default='', null=True)
    plan_expiry_date = models.CharField(max_length=200, default='', null=True)
    plan_month = models.CharField(max_length=50,default='', null = True, blank= True)
    customer_to_admin_time = models.CharField(max_length=50,default='', null = True, blank= True)
    admin_to_astrologer_time = models.CharField(max_length=50,default='', null = True, blank= True)
    astrloger_to_admin_time = models.CharField(max_length=50,default='', null = True, blank= True)
    admin_to_customer_time = models.CharField(max_length=50,default='', null = True, blank= True)


    def __str__(self):
        return f'{self.cust_name}-{self.astro_name}-{self.id}'
    


class Wallet(models.Model):
    plan_id = models.CharField(max_length=200, default='', null=True)
    cust_id = models.CharField(max_length=240,blank=True,null=True)
    name = models.CharField(max_length=240,blank=True,null=True)
    email_id = models.EmailField(max_length=240,blank=True,null=True)
    whatsapp_no = models.CharField(max_length=240,blank=True,null=True)
    recharge_amount = models.CharField(max_length=240,blank=True,null=True)
    debit_amount = models.CharField(max_length=240,blank=True,null=True)
    recharge_date = models.CharField(max_length=240,blank=True,null=True)
    plan_recharge_date = models.DateField(null=True)
    recharge_time = models.CharField(max_length=240,blank=True,null=True)
    order_id = models.CharField(max_length=240,blank=True,null=True) 
    payment_id = models.CharField(max_length=240,blank=True,null=True)
    wallet_month = models.CharField(max_length=100,default='', null=True)
    transaction_id = models.CharField(max_length=240,blank=True,null=True)
    def __str__(self):
        return f'{self.name}-{self.email_id}'


class Customer_profile(models.Model):
    cust_id = models.CharField(max_length=240,blank=True,null=True)
    fname = models.CharField(max_length=240,blank=True,null=True)
    pname = models.CharField(max_length=240,blank=True,null=True)
    dob = models.CharField(max_length=240,blank=True,null=True)
    gender = models.CharField(max_length=240,blank=True,null=True)
    birth_time = models.CharField(max_length=240,blank=True,null=True)
    birth_place = models.CharField(max_length=240,blank=True,null=True)
    city = models.CharField(max_length=240,blank=True,null=True)
    state = models.CharField(max_length=240,blank=True,null=True)
    country = models.CharField(max_length=240,blank=True,null=True)


    def __str__(self):
        return self.fname


class Contact(models.Model):
    contact_person = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=10)
    contact_email = models.EmailField()


class Rating(models.Model):
    rating1= models.CharField(max_length=240,blank=True,null=True)
    comments = models.CharField(max_length=240,blank=True,null=True)


#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

from django.conf import settings

class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}' 

from django.contrib.auth import get_user_model

User = get_user_model()
class ChatGptBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messageInput = models.TextField()
    bot_response = models.TextField()
    def __str__(self):
        return self.user.username