#APIS for this app will go here

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Package, Profile, Invoice
#This is the user serializer
class ProductSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = Product
        fields = '__all__'

    

#This is the user serializer
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
