from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import *
class CaseResource(resources.ModelResource):
    surveyor_name = fields.Field(
    column_name='name',
    attribute='surveyorlist',
    widget=ForeignKeyWidget(Surveyorlist, 'name'))
    class Meta:
            model = Case
            import_id_fields = ('cc_date','sourcelist','case_id','customer_name','customer_number','alt_number','companylist','vehicle_number','vehicle_type','payment_type','company_cash','case_mode','amount','pay_date','vehicle_from','location','company_kilometer','surveyor_name','inspection_type','surveyor_kilometer','surveyor_cash','cd_date','time','remarks','status')
            export_order = ('cc_date','sourcelist','case_id','customer_name','customer_number','alt_number','companylist','vehicle_number','vehicle_type','payment_type','company_cash','case_mode','amount','pay_date','vehicle_from','location','status','company_kilometer','surveyor_name','inspection_type','surveyor_kilometer','surveyor_cash','cd_date','time','remarks')
            exclude = ('id',)
            skip_unchanged = True
            fields = ['cc_date','sourcelist','case_id','customer_name','customer_number','alt_number','companylist','vehicle_number','vehicle_type','payment_type','company_cash','case_mode','amount','pay_date','vehicle_from','location','company_kilometer','surveyor_name','inspection_type','surveyor_kilometer','surveyor_cash','cd_date','time','remarks','status']
            #


