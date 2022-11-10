from django.shortcuts import render
from django.http import HttpResponse
from .models import products
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def product(request):
    product_items = products.objects.all()
    context = {
        'products': product_items
    }
    return render(request, 'myapp/myfile.html', context)

def product_detail(request, id):
    pass