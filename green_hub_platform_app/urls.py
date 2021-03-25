from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
from .views import ProductViewSet, PackageViewSet, InvoiceViewSet

router.register(r'products', views.ProductViewSet,'farm-api')
router.register(r'packages', views.PackageViewSet,'maps-api')
router.register(r'invoices', views.InvoiceViewSet,'apisector')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'green_hub'
urlpatterns = [
    path('api/', include(router.urls)),
   
]