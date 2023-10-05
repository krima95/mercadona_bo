from django.shortcuts import render, redirect
from django.template import loader
from .forms import ProductForm
from .models import Product
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product/')
    else:
        form = ProductForm()

    # Pagination
    object_list = Product.objects.all()
    paginator = Paginator(object_list, 3)
    page_number = request.GET.get('page')

    try:
        page_object = paginator.page(page_number)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)
    # pointe vers le fichier du template index.html
    return render(request, 'index.html', {'form': form, 'data': Product.objects.all()})


def upload_form(request):
    context = {'form': ProductForm()}
    return render(request, 'templates/products/index.html', context)


def register(request):
    return render(request, 'products/register.html')


def my_login(request):
    return render(request, 'products/login.html')
