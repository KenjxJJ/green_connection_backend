from django.urls import path
from . import views 

urlpatterns = [
    path("api/products/", views.products_list),
    path("api/product/:id", views.product_detail)
]
