from django.db import models

# Create your models here.
class Vendor(models.Model):
    managername = models.CharField(max_length=200)
    vendorname = models.CharField(max_length=200,db_index=True,unique=True)
    joiningdate = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200, db_index=True)
    vendorcontact = models.CharField(max_length=14,db_index=True)
    status = models.BooleanField(default=True)

class MilkCategory(models.Model):
    milkprice = models.FloatField(max_length=200,db_index= True)
    related_vendor = models.ForeignKey(Vendor,related_name='MilkCategory',on_delete=models.CASCADE,null=True)
 
class vendorledger(models.Model):
    related_vendor = models.ForeignKey(Vendor,related_name='vendorledger',on_delete=models.CASCADE,null = True)
    related_milkcategory=models.ForeignKey(MilkCategory,related_name='vendorledger',on_delete=models.CASCADE,null = True)
    date = models.CharField(max_length=20,db_index=True)
    price = models.FloatField(max_length=1000,db_index=True,default = 0.0)
    # total = models.FloatField(max__length = 100000,db_index=True,default=0.0)


class Profile(models.Model):
    user = models.CharField(max_length = 20,null= True,blank = False)
    user_type = models.CharField(max_length = 20,null= True,blank = False)
    contact_number = models.CharField(max_length=20,null=True,unique=True)
    joining_data = models.DateField(auto_now_add=False,null=True)
    address = models.CharField(max_length=15,null=True)


class CustomerMilkCategory(models.Model):
    milkprice = models.FloatField(max_length=20)
    # related_customer = models.ForeignKey(related_name = CustomerMilkCategory,on_delete=models.CASCADE,null=True)


class  Customerledger(models.Model):
    related_milk_category = models.ForeignKey(CustomerMilkCategory,
    related_name = "Customerledger",on_delete=models.CASCADE,null = True)
    related_customer = models.ForeignKey('Customerledger',on_delete=models.CASCADE,null= True)
    date = models.CharField(max_length=15,null=True)
    price = models.FloatField(max_length=1000,db_index=True,default=0.0)
    quantity = models.FloatField(max_length=100,db_index=True,default = 0.0)
    total = models.FloatField(max_length=10000,db_index=True,default=0.0)

