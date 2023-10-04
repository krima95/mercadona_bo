from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Index.html page
def products(request):
    template = loader.get_template('products/products.html')
    return HttpResponse(template.render())
