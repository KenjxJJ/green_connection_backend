from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models  import User

# Create your models here.
SAFE_GOODS_CHOICES = (
    (0, "No"),
    (1, "Yes")
)

#  Created by the admin(GreenHub Manager)
ROLES = (
    (0, "Customer"),(1, "Supplier"),(2, "Loader" )
)

#  Product info
class Product(models.Model):
    item_number = models.CharField(max_length=11)
    description = models.CharField(max_length=400)
    quantity = models.IntegerField()
    serial_number = models.CharField(max_length=12, blank=True, null=True)
    batch_number = models.CharField(max_length=21, blank=True, null=True)
    rev_number = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return "Item No. {} - description by {}, quantity {}".format(self.item_number,self.description, self.quantity)
  
#  Package Info
#  How are the goods packeged for the customer

class Package(models.Model):
    bill_reference = models.CharField(max_length=200, blank=True, null=True)
    invoice_reference = models.CharField(max_length=200,blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=120, blank=True, null=True)
    country_of_origin = models.CharField(max_length=200) 
    is_a_dangerous_good = models.IntegerField(choices=SAFE_GOODS_CHOICES, default=0)
    date_of_arrival = models.DateField()
    is_recieved = models.BooleanField(default=False)

    def __str__(self):
        return  'Package info - Invoice Reference {}, Bill Ref.{},  Size {}'.format(self.invoice_reference, self.bill_reference, self.size)

# User profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE) 
    role = models.IntegerField(choices=ROLES, default=0)
    location = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} joined {}'.format(self.user, self.date_joined)

# Orders made by the customer
class Invoice(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    date_of_order = models.DateTimeField(auto_now_add=True)
    package = models.ForeignKey(Package,on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    is_paid_or_cleared = models.BooleanField(default=False)

    def __str__(self):
        return "Invoice order on {}".format(self.date_of_order)


