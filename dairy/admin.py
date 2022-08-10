from django.contrib import admin
from .models import Customerledger, MilkCategory, Profile, Vendor, vendorledger,CustomerMilkCategory
# Register your models here.
class Vendor_Admin(admin.ModelAdmin):
    list_display = ['vendorname','managername','joiningdate', 'vendorcontact']

admin.site.register(Vendor, Vendor_Admin)

class MilkCategory_Admin(admin.ModelAdmin):
    list_display = ['milkprice','related_vendor']
    list_filter = [ 'milkprice']

admin.site.register(MilkCategory, MilkCategory_Admin)
admin.site.register(vendorledger)
admin.site.register(Profile)
admin.site.register(CustomerMilkCategory)
admin.site.register(Customerledger)