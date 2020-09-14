from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .resources import *
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter



class PolicyAdmin(ImportExportModelAdmin):

    resource_class = PolicyResource
    search_fields = ('buyer','seller')
    list_display = ('buyer','seller','issueDate','company','buyeramount','buyermode',)
    list_filter = ('buyer','seller',('issueDate', DateRangeFilter))
    

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):

    search_fields = ('buyer_name',)
    list_filter = ('buyer_name',)
    list_display = ('buyer_name','buyernet','buyertotalamount')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):

    search_fields = ('seller_name',)
    list_filter = ('seller_name',)
    list_display = ('seller_name','sellernet','sellertotalamount')


# Register your models here.

admin.site.register(Company)
admin.site.register(Policy,PolicyAdmin)