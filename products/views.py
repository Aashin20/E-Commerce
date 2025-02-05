from django.shortcuts import render
from . models import ProductInfo
from django.core.paginator import Paginator
# Create your views here.

def index(request):

    return render(request,'index.html')

def products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list= ProductInfo.objects.order_by('priority')
    product_paginator=Paginator(product_list,3)
    product_list=product_paginator.get_page(page)
    list={'products':product_list}
    return render(request,'products.html',list)

def product_info(request,pk):
    product=ProductInfo.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_details.html',context)