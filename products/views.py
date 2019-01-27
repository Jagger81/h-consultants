from __future__ import unicode_literals
from django.shortcuts import render
from products.models import Product


def products(request):
    return render(request, 'categories.html')

# Product.objects.filter() will find all the product entries from the database whose category is audio
# We then assign them to a 'products_list' variable and send that variable to audio.html template
def training(request):
    return render(request, 'training.html', {'products_list': Product.objects.filter(category='training')})

def manuals(request):
    return render(request, 'manuals.html', {'products_list': Product.objects.filter(category='manuals')})

def templates(request):
    return render(request, 'templates.html', {'products_list': Product.objects.filter(category='templates')})

def audit(request):
    return render(request, 'audit.html', {'products_list': Product.objects.filter(category='audit')})