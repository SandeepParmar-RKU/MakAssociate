import django_filters
from .models import *

class BuyerFilter(django_filters.FilterSet):
    class Meta:
        model = Policy
        fields = {  
            'buyer' : ['exact'],
     
        }

class SellerFilter(django_filters.FilterSet):
    class Meta:
        model = Policy
        fields = {
            'seller': ['exact']
        }