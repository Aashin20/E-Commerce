from django.shortcuts import render
from . models import ProductInfo
# Create your views here.

def index(request):

    return render(request,'index.html')

def products(request):
    product_list= ProductInfo.objects.all()
    list={'products':product_list}
    return render(request,'products.html',list)

def product_info(request):
    return render(request,'product_details.html')