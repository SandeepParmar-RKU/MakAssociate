from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput


class BuyerForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
            super(BuyerForm,self).__init__(*args, **kwargs)
    class Meta:
        model = Buyer
        fields = {'buyer_name'}
        labels = {'buyer_name':'Buyer Name'}


class SellerForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
            super(SellerForm,self).__init__(*args, **kwargs)
    class Meta:
        model = Seller
        fields = {'seller_name'}
        labels = {'seller_name':'Seller Name'}

class CompanyForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
            super(CompanyForm,self).__init__(*args, **kwargs)

    class Meta:
        model = Company
        fields = {'company_name'}
        labels = {'company_name':'Company'}


class PolicyForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
            super(PolicyForm,self).__init__(*args, **kwargs)
    
    field_order = ['buyer','seller','issueDate','company','registrationNumber','vehicle','Type','expiryDate','premiumAmount','net','tp','od','buyerPayout','buyerPercantage','buyernet','buyermode','buyeramount','buyerdebit','buyerremark','sellerPayout','sellerPercantage','sellernet','sellermode','selleramount','sellerdebit','sellerremark']

    class Meta:
        model = Policy
        fields = {'buyer','seller','issueDate','company','registrationNumber','vehicle','Type','expiryDate','premiumAmount','net','tp','od','sellerPayout','sellerPercantage','sellernet','sellermode','selleramount','sellerdebit','sellerremark','buyerPayout','buyerPercantage','buyernet','buyermode','buyeramount','buyerdebit','buyerremark'}
        widgets = {
        'issueDate': DatePickerInput(options={
                "showClear": True   ,
                "showTodayButton": True,
            }), # default date-format %m/%d/%Y will be used
        'expiryDate': DatePickerInput(options={
                "showClear": True,
                "showTodayButton": True,
            }),
        }
        labels = {'buyer':'Buyer','seller':'Seller','issueDate':'Issue Date','company':'Company','registrationNumber':'Registration Number','vehicle':'Vehicle Type','Type':'Type','expiryDate':'Expiry Date','premiumAmount':'Premium Amount','net':'net','tp':'tp','od':'od','buyerPayout':'Payout','buyerPercantage':'Buyer Percantage','buyernet':'Recevebale','buyermode':'Buyer Mode','buyeramount':'Buyer Amount','buyerremark':'Remarks','buyerdebit':'Debit','sellerPayout':'Pay In','sellerPercantage':'Seller Percantage','sellernet':'Payable',"sellermode":'Seller Mode','selleramount':'Seller Amount','sellerdebit':'Credit','sellerremark':'Remarks'}
  

class SellerCollection(forms.ModelForm):
        def __init__(self,*args, **kwargs):
               
                super(SellerCollection,self).__init__(*args, **kwargs)


        field_order = ['seller','buyer','issueDate','company','sellermode','selleramount','sellerremark']

        class Meta:
                model = Policy
                fields = {'buyer','seller','issueDate','company','selleramount','sellermode','sellerremark'}
                widgets = {
                'issueDate': DatePickerInput(options={
                        "showClear": True   ,
                        "showTodayButton": True,
                }), # default date-format %m/%d/%Y will be used
                'expiryDate': DatePickerInput(options={
                        "showClear": True,
                        "showTodayButton": True,
                }),
                 }
                labels = {'buyer':'Buyer'}
         
class BuyerColletion(forms.ModelForm):
        def __init__(self,*args, **kwargs):
              
                super(BuyerColletion,self).__init__(*args, **kwargs)
               
                


        field_order = ['buyer','seller','issueDate','company','buyeramount','sellerrmode','buyerremark']

        class Meta:
                model = Policy
                fields = {'buyer','seller','issueDate','company','buyeramount','buyermode','buyerremark'}
                widgets = {
                'issueDate': DatePickerInput(options={
                        "showClear": True   ,
                        "showTodayButton": True,
                }), # default date-format %m/%d/%Y will be used
                'expiryDate': DatePickerInput(options={
                        "showClear": True,
                        "showTodayButton": True,
                }),
                }
                labels = {'buyer':'Buyer'}
        