from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, PackageSerializer, InvoiceSerializer, ProfileSerializer
from . models import Product, Package, Invoice, Profile


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    

    
    retrieve:
        retrieve a sigle Product by its id
    list:
        Return a list of all Product.
    create:
        Create a new Product.e.g
    {
    "id": 1,
    "item_number": "A001",
    "description": "testing",
    "quantity": 12,
    "serial_number": "A008",
    "batch_number": "B003",
    "rev_number": "C01"
    }
    delete:
        Delete a Product
    PUT:
        Update a Product.
    partial_update:
        Update a Product.
    """

    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticated]


class PackageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
   
    retrieve:
        retrieve a sigle Product by its id
    list:
        Return a list of all Product.
    create:
        Create a new Product.e.g
    {
    "id": 1,
    "bill_reference": "A003",
    "invoice_reference": "B005",
    "size": 12,
    "weight": "Thirty",
    "country_of_origin": "Uganda",
    "is_a_dangerous_good": 1,
    "date_of_arrival": "2021-03-18",
    "is_recieved": true
    }
    delete:
        Delete a Product
    PUT:
        Update a Product.
    partial_update:
        Update a Product.
    """

    queryset = Package.objects.all().order_by('-id')
    serializer_class = PackageSerializer
    #permission_classes = [permissions.IsAuthenticated]



class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    
    retrieve:
        retrieve a sigle Invoice by its id
    list:
        Return a list of all Invoices.
    create:
        Create a new Invoice.e.g
    {
    "id": 2,
    "date_of_order": "2021-03-25T13:44:13.137567Z",
    "is_paid_or_cleared": true,
    "product": 1,
    "package": 1,
    "user": 1
    }
    delete:
        Delete an Invoice
    PUT:
        Update an Invoice.
    partial_update:
        Update an Invoice.
    """

    queryset = Invoice.objects.all().order_by('-id')
    serializer_class = InvoiceSerializer
    #permission_classes = [permissions.IsAuthenticated]



class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

