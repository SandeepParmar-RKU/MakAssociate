from django import forms
from .models import *


class CaseForm(forms.ModelForm):

    class Meta:
       model = Case
       fields = ('cc_date','sourcelist','case_id','customer_name','customer_number','alt_number','companylist','vehicle_number','vehicle_type','payment_type','company_cash','case_mode','amount','pay_date','vehicle_from','location','status','company_kilometer','surveyorlist','inspection_type','surveyor_kilometer','surveyor_cash','cd_date','time','remarks')
       lables = {'cc_date':'CC Date','sourcelist':'Source','case_id':'Case id','customer_name':'Customer Name','customer_number':'Customer Number','alt_number':'Alt Number','companylist': 'Company Name','vehicle_number':'Vehicle Number','vehicle_type':'Vehicle Type','payment_type':'Payment Type','company_cash':'Company Cash','case_mode':'Case Mode','amount':'Amount',"pay_date":'Pay Date','vehicle_from':'Vehicle From','location':'Location', 'status':'Status', 'company_kilometer':'Company Kilometer','surveyorlist':'Surveyor Name','inspection_type':'Inspection Type','surveyor_kilometer':'Surveyor Kilometer','surveyor_cash':'Surveyor Cash','cd_date':'Cd date','time':'Time','remark':'Remarks'}

    def __init__(self,*args,**kwargs):
        super(CaseForm,self).__init__(*args, **kwargs)
      