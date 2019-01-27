from __future__ import unicode_literals
from django.shortcuts import render
from products.models import Product


def products(request):
    products = Product.objects.all()
    return render(request, "categories.html", {"products": products})

# Product.objects.filter() will find all the product entries from the database whose category is training
# We then assign them to a 'products_list' variable and send that variable to training.html template
def training(request):
    products_list = Product.objects.filter(category__iexact='training')
    return render(request, 'training.html', {"products_list": products_list})

def manuals(request):
    products_list = Product.objects.filter(category__iexact="manuals")
    return render(request, 'manuals.html', {"products_list": products_list})

def templates(request):
    products_list = Product.objects.filter(category__iexact="templates")
    return render(request, 'templates.html', {"products_list": products_list})

def audit(request):
    products_list = Product.objects.filter(category__iexact="audit")
    return render(request, 'audit.html', {"products_list": products_list})