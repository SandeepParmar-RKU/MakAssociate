from django.urls import path,include
from . import views
from .forms import *

app_name = 'insurance'
urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    path('addseller/',views.SellerCreateView.as_view(), name='addseller'),
    path('addbuyer/',views.BuyerCreateView.as_view(), name='addbuyer'),
    # path('addpolicy/',views.PolicyCreateView, name='addpolicy'),
    # path('addpolicysave/',views.PolicySaveView, name='addpolicysave'),
    path('addpolicy/',views.PolicyCreateView.as_view(), name='addpolicy'),
    path('addcompany/',views.CompanyCreateView.as_view(), name='addcompany'),
    path('add/<int:id>',views.PolicyUpdateView.as_view(), name='updatepolicy'),
    # path('seller/<int:id>',views.PolicyUpdateViewseller.as_view(), name='updatepolicyseller'),
    path('buyers/',views.BuyerListView.as_view(), name='buyers'),
    path('sellers/',views.SellerListView.as_view(), name='sellers'),
    path('buyercollection/',views.BuyerCollectionCreateView.as_view(), name='buyercollectionform'),
    path('sellercollection/',views.SellerCollectionCreateView.as_view(), name='sellercollectionform'),
  
]