from django.contrib import admin

# Register your models here.
from login.models import AdminUser,AstrologerUser,CustomerUser,GurujiUsers,admin_setting_plan,admin_setting_plan_dollar,MerchantProfile,generalSetting,Comment,Plan_Purchase,Wallet,Customer_profile
admin.site.register(Plan_Purchase)
admin.site.register(GurujiUsers)
admin.site.register(AdminUser)
admin.site.register(AstrologerUser)
admin.site.register(CustomerUser)
admin.site.register(admin_setting_plan)
admin.site.register(admin_setting_plan_dollar)
admin.site.register(MerchantProfile)
admin.site.register(generalSetting)
admin.site.register(Comment)
admin.site.register(Wallet)
admin.site.register(Customer_profile)