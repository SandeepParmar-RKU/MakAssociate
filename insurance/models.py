from django.db import models
from datetime  import datetime,date
from django.urls import reverse
from django.db.models import Count
from django.db.models import Q,F,Sum

vehicleList = [('Byk','Byk'),('Pvt','Pvt'),('LGcv','LGcv'),('Hgcv','Hgcv'),('Lcv','Lcv'),('MisD','MisD'),('Dvan','Dvan'),('PCV','PCV'),('Rixa','Rixa'),('---','---')]
typeList = [('Tp','Tp'),('Package','Package'),('Od','Od'),('---','---')]
modeList = [('Link','Link'),('Cash','Cash'),('Card','Card'),('Credit','Credit'),('---','---')]
sellermodelist = [('Cash','Cash'),('Credit','Credit'),('ICICI','ICICI'),('HDFC','HDFC'),('YES','YES'),('INDUSIND','INDUSIND'),('Customer','Customer')]

class Buyer(models.Model):
    buyer_name = models.CharField(max_length=256,unique=True)
  
    def __str__(self):
        return self.buyer_name
    
    def buyernet(self):
        queryset = Buyer.objects.filter(policybuyer__buyer_id = self.id).annotate(total=Sum('policybuyer__buyernet',))
        return queryset[0].total
    def buyertotalamount(self):

        queryset = Buyer.objects.filter(policybuyer__buyer_id = self.id).annotate(total=Sum('policybuyer__buyeramount',))
        return queryset[0].total



class Seller(models.Model):
    seller_name = models.CharField(max_length=256,unique=True)


    def __str__(self):
        return self.seller_name


    def sellernet(self):
        queryset = Seller.objects.filter(policyseller__seller_id = self.id).annotate(total=Sum('policyseller__sellernet',))
        return queryset[0].total
    
    def sellertotalamount(self):
        queryset = Seller.objects.filter(policyseller__seller_id = self.id).annotate(total=Sum('policyseller__selleramount',))
        # print(queryset[0].total)
        return queryset[0].total

class Company(models.Model):
    company_name = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.company_name
    


class Policy(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE,related_name='policybuyer')
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,related_name='policyseller')
    issueDate = models.DateField(blank=True)
    company = models.ForeignKey(Company,on_delete=models.DO_NOTHING,to_field='company_name')
    registrationNumber = models.CharField(max_length=256,blank=True)
    vehicle = models.CharField(max_length=256,choices=vehicleList,blank=True)
    Type = models.CharField(max_length=256,choices=typeList,default=typeList[3])
    expiryDate = models.DateField(blank=True,null=True)
    premiumAmount = models.FloatField(default=0)
    net = models.FloatField(default=0)
    tp = models.FloatField(default=0)
    od = models.FloatField(default=0)
    buyerPayout = models.FloatField(default=0)
    sellerPayout = models.FloatField(default=0)
    buyerPercantage = models.FloatField(default=0)
    sellerPercantage = models.FloatField(default=0)
    buyernet = models.FloatField(default=0)
    sellernet = models.FloatField(default=0)
    buyermode = models.CharField(max_length=256,choices=modeList,default=modeList[4])
    sellermode = models.CharField(max_length=256,choices=sellermodelist)
    buyeramount = models.FloatField(default=0)
    selleramount = models.FloatField(default=0)
    sellerremark = models.TextField(blank=True)
    buyerremark = models.TextField(blank=True)
    sellerdebit = models.FloatField(default=0)
    buyerdebit = models.FloatField(default=0)
   
    

  
    def get_absolute_url(self): 
        return reverse("insurance:updatepolicy", kwargs={"id": self.id})

    
    