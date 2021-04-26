from django.shortcuts import render
from. models import *
from django.contrib.auth.models import User

# Create your views here.
def store(request,*args, **kwargs):
    storeitems = products.objects.all()
    category_items = category.objects.all()
    context = {
        'storeitem': storeitems,
        'category_items':category_items
    }
    return render(request,'home.html',context)

def account(request):


    return render(request,'account.html')

def moredetailed(request):
    return render(request,'moredetail.html',{})

def cart(request):
    return render(request,'cart.html',context)
