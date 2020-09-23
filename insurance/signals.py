from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Policy)
def transaction_saved(sender,instance,created=True, **kwargs):
    if created:
        instance.buyerdebit = instance.buyernet - instance.buyeramount
        instance.sellerdebit = instance.sellernet - instance.selleramount
        instance.save()


# @receiver(post_save, sender=Policy)
# def transaction_updated(sender,instance,created, **kwargs):
#     if created == False:
#         instance.buyerdebit = instance.buyernet - instance.buyeramount
#         instance.sellerdebit = instance.sellernet - instance.selleramount
#         instance.save()

