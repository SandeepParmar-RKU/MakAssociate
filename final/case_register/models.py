from django.db import models
from datetime  import datetime,date
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import django_filters
User = get_user_model()
# Create your models here.
source_list = [('AAA','AAA'),('Adroit','Adroit',),('Aniket','Aniket'),('AutoScan','AutoScan'),('Milan','Milan'),('Other','Other'),('Valuation','Valuation'),('Vijay','Vijay'),('Mahindra','Mahindra'),('WeeAssured','WeeAssured'),]
company_list = [('Acko','Acko'),('Auction','Auction'),('AWP','AWP'),('BAJAJ','BAJAJ'),('Bharti','Bharti'),('Car Dekho','Car Dekho'),('CarTrade','CarTrade'),('Edelweiss','Edelweiss'),
                    ('Future','Future'),('GoDigit','GoDigit'),('HDFC','HDFC'),('Hero Fincorp','Hero Fincorp'),('ICICI','ICICI'),('Iffco','Iffco'),
                    ('Kotak','Kotak'),('Liberty','Liberty'),('L&T','L&T'),('Magma','Magma'),('Maruti Nat','Maruti Nat'),('National','National'),('NewIndia','NewIndia'),
                    ('Oriental','Oriental'),('Rajni','Rajni'),('Raheja QBE','Raheja QBE'),('Reliance','Reliance'),('Royal','Royal'),('SBI','SBI'),('ShriRam','ShriRam'),('Sompo','Sompo'),('TATA','TATA'),('United','United'),('Others','Others')]
vehicle_list = [('BYK','BYK'),('COM','COM'),('PVT','PVT'),('Other','Other')]
payment_option = [('Billing','Billing'),('Customer','Customer')]
case_mode_list = [('Agent','Agent'),('NA','NA'),('Online','Online'),('Surveyor','Surveyor')]
status_list = [('Created','Created'),('Aprroval','Aprroval'),('Assigned','Assigned'),('Hold','Hold'),('Done','Done'),('Missing','Missing'),('Completed','Completed'),('Rejected',"Rejected")]
inspection_list = [('Online','Online'),('Offline','Offline'),('Other','Other')]
surveyor_list = [('Jmngr Bhavesh','Jmngr Bhavesh'),('Jmngr Rajesh','Jmngr Rajesh')]
#^[A-Z0-9]{3}(?:List)?$
#def case_id_validator(id):
  #  if id != "" or unique != True:
    #    raise ValidationError(_("Duplicate or blank field not allowed!"),
    #    params={'id':id},)

#class Sourcelist(models.Model):
   # sourcelist = models.CharField(max_length=10,choices=source_list)
   #
   # def __str__(self):
    #    return self.sourcelist


#class Companylist(models.Model):
 #   companylist = models.CharField(choices=company_list,max_length=256)

  #  def __str__(self):
   #     return self.companylist


class Surveyorlist(models.Model):
    name = models.CharField(max_length=256,unique=True)

    # def fname(self):
    #   return str(self.name) + ' ' + str(self.id);

    def __str__(self):
        return self.name
    #def __init__(*args):
     # sname=


class Case(models.Model):
    cc_date = models.DateField()
    sourcelist = models.CharField(max_length=10,choices=source_list)
    #sourcelist = models.ForeignKey(Sourcelist,on_delete=models.CASCADE)
    case_id = models.CharField(max_length=256,blank=True,null=True,default=None)
    customer_name = models.CharField(max_length=256,default="NA")
    customer_number = models.CharField(max_length=10)
    alt_number = models.CharField(max_length=10,default="0",blank=True)
    companylist = models.CharField(choices=company_list,max_length=256)
   # companylist = models.ForeignKey(Companylist,on_delete=models.CASCADE)
    vehicle_number = models.CharField(blank=False,max_length=256)
    vehicle_type =  models.CharField(choices=vehicle_list,max_length=256)
    payment_type = models.CharField(choices=payment_option,max_length=256,default=payment_option[0])
    company_cash = models.IntegerField(default=0)
    case_mode = models.CharField(choices=case_mode_list,max_length=256,default=case_mode_list[1])
    amount = models.IntegerField(default=0)
    pay_date = models.DateField(null=True,blank=True)
    vehicle_from = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    company_kilometer = models.IntegerField(default=0)
   # surveyorlist = models.CharField(max_length=256,choices=surveyor_list)
    surveyorlist = models.ForeignKey(Surveyorlist,on_delete=models.CASCADE,to_field='name',blank=True,null=True)
    inspection_type = models.CharField(choices=inspection_list,max_length=256,default=inspection_list[0])
    surveyor_kilometer = models.IntegerField(default=0)
    surveyor_cash = models.IntegerField(default=0)
    cd_date = models.DateField(null=True,blank=True)
    time = models.IntegerField(default=0,blank=True)
    remarks = models.CharField(max_length=256,default="NA")
    status = models.CharField(choices=status_list,max_length=256)


    #  def __init__(self):
      #  sname = Surveyorlist.objects.get(pk=1)
      #  return sname.get_surveyorlist_name()

    class Meta:
        ordering = ["-cc_date"]
