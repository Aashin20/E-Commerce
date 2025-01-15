from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def product_info(request):
    return render(request,'product_details.html')