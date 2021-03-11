from django.contrib import admin
from .models import Product, Profile, Package, Invoice


# Register your models here.

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Package)
admin.site.register(Invoice)