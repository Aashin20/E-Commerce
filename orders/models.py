from django.db import models
from customers.models import Customer
from products.models import ProductInfo
# Create your models here.

class Order(models.Model):
    LIVE=1
    DELETE=0
    CART_STAGE=0
    ORDER_CNF=1
    ORDER_REJECTED=4
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERED,"ORDER_DELIVERED"),
                   (ORDER_REJECTED,"ORDER_CANCELLED"),
                   (ORDER_CNF,"ORDER_CONFIRMED"))
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class OrderedItem(models.Model):
    product=models.ForeignKey(ProductInfo, related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

