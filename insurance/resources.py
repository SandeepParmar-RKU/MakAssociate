from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import *

class PolicyResource(resources.ModelResource):
    buyer_name = fields.Field(
        column_name='buyer_name',
        attribute='buyer',
        widget=ForeignKeyWidget(Buyer,'buyer_name')
    )
    seller_name = fields.Field(
        column_name='seller_name',
        attribute='seller',
        widget=ForeignKeyWidget(Seller,'seller_name')
    )
    company = fields.Field(
        column_name='company_name',
        attribute='company',
        widget=ForeignKeyWidget(Company,'company_name')
    )
    class Meta:
        model = Policy
        import_id_fields = ('buyer_name','seller_name','issueDate','company','registrationNumber','vehicle','Type','expiryDate','premiumAmount','net','tp','od','buyerPayout','buyerPercantage','buyernet','buyermode','buyeramount','buyerdebit','buyerremark','sellerPayout','sellerPercantage','sellernet','sellermode','selleramount','sellerdebit','sellerremark')
        export_order = ('buyer_name','seller_name','issueDate','company','registrationNumber','vehicle','Type','expiryDate','premiumAmount','net','tp','od','buyerPayout','buyerPercantage','buyernet','buyermode','buyeramount','buyerdebit','buyerremark','sellerPayout','sellerPercantage','sellernet','sellermode','selleramount','sellerdebit','sellerremark')
        exclude = ('id',)
        skip_unchanged = True
        fields = ['buyer_name','seller_name','issueDate','company','registrationNumber','vehicle','Type','expiryDate','premiumAmount','net','tp','od','buyerPayout','buyerPercantage','buyernet','buyermode','buyeramount','buyerdebit','buyerremark','sellerPayout','sellerPercantage','sellernet','sellermode','selleramount','sellerdebit','sellerremark']