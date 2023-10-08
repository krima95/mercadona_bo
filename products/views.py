from .models import Product
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Page d'accueil
def home(request):

    return render(request, 'products/index.html')


# Formulaire créer un compte
def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Compte créé avec succès!")

            return redirect("login")

    context = {'form': form}

    return render(request, 'products/register.html', context=context)


# Formulaire se connecter

def login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'products/login.html', context=context)


# Déconnexion
def user_logout(request):
    auth.logout(request)

    messages.success(request, "Vous êtes déconnecté !")

    return redirect("login")


# Tableau de bord
@login_required(login_url='login')
def dashboard(request):

    records = Product.objects.all()

    context = {'records': records}

    return render(request, 'products/dashboard.html', context=context)


"""
# - Create a record

@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)


# - Update a record

@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='login')
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)

    context = {'record': all_records}

    return render(request, 'webapp/view-record.html', context=context)


# - Delete a record

@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")


"""
