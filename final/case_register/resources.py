from import_export import resources
from .models import *

class CaseResource(resources.ModelResource):
    class Meta:
        model = Case   
        fields = ('cc_date','sourcelist','case_id','customer_name','customer_number','alt_number','companylist','vehicle_number','vehicle_type','payment_type','company_cash','case_mode','amount','pay_date','vehicle_from','location','company_kilometer','surveyorlist__name','inspection_type','surveyor_kilometer','surveyor_cash','cd_date','time','remarks','status')
        export_order = ('cc_date','sourcelist','case_id','customer_name','customer_number','alt_number','companylist','vehicle_number','vehicle_type','payment_type','company_cash','case_mode','amount','pay_date','vehicle_from','location','company_kilometer','surveyorlist__name','inspection_type','surveyor_kilometer','surveyor_cash','cd_date','time','remarks','status')
 