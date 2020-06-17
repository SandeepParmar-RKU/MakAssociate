import django_filters
from .models import *

class CaseFilter(django_filters.FilterSet):
    class Meta:
        model = Case
        fields = {
            'sourcelist': ['exact', ],
            'case_id': ['icontains', ],
            'companylist': ['exact', ],
            'vehicle_number': ['icontains',],
            'surveyorlist': ['exact', ],
            'cd_date': ['exact', ], 
            'status': ['exact', ],
        }