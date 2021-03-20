from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models  import User
from decimal import Decimal
from django.core.validators import MinValueValidator

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
    product_image = models.ImageField(upload_to="images/", default="images/sample_product.jpg")
    product_price_in_dollars = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.CharField(max_length=400)
    quantity = models.PositiveIntegerField()
    serial_number = models.CharField(max_length=12, blank=True, null=True)
    batch_number = models.CharField(max_length=21, blank=True, null=True)
    rev_number = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return "Item No. {} - description by {}, quantity {}".format(self.item_number,self.description, self.quantity)
  
#  Package Info
#  How are the goods packeged for the customer

class Package(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    bill_reference = models.CharField(max_length=200, blank=True, null=True)
    invoice_reference = models.CharField(max_length=200,blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    weight = models.CharField(max_length=120, blank=True, null=True)
    country_of_origin = models.CharField(max_length=200) 
    is_a_dangerous_good = models.IntegerField(choices=SAFE_GOODS_CHOICES, default=0)
    date_of_arrival = models.DateTimeField()
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
    user = models.ForeignKey(Profile, on_delete=CASCADE)
    is_paid_or_cleared = models.BooleanField(default=False)

    def __str__(self):
        return "Invoice order on {}".format(self.date_of_order)


