import django_filters
from .models import *

class CaseFilter(django_filters.FilterSet):
    status = django_filters.MultipleChoiceFilter(choices=status_list)
    class Meta:
        model = Case
        fields = {
            'cc_date' : ['exact'],
            'sourcelist': ['exact'],
            'case_id': ['icontains'],
            'companylist': ['exact'],
            'vehicle_number': ['icontains'],
            'surveyorlist': ['exact'],
            'cd_date': ['exact'],
            'status': ['exact'],
        }
