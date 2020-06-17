from django.forms import DateTimeInput, DateInput


class FengyuanChenDatePickerInput(DateInput):
    template_name = 'widgets/fengyuanchen_datepicker.html' 