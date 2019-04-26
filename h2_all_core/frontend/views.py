from django.shortcuts import render, redirect, get_object_or_404
from .models import Borehole, Price, Stat
from .form import NewPriceForm, NewBoreholeForm

# Create your views here.

def home(request):
    # NewProfileForm=form
    return render(request, 'index.html', locals())

def borehole(request):
    boreholes = Borehole.objects.all()
    data = {}
    data['boreing'] = boreholes
    return render(request, 'borehole.html', data)

def price_list(request):
    prices = Price.objects.all()
    data = {}
    data['posts'] = prices
    return render(request, 'price.html', data)

def create_price(request):
    current_price = 0
    price = Price.objects.filter()
    form = NewPriceForm()

    if request.method == 'POST':
        form =  NewPriceForm(request.POST, request.FILES)
        if form.is_valid():
            current_price = form.save(commit=False)
            current_price.price = current_price
            current_price.save()
            return redirect('index')
    else:
        form = NewPriceForm()
    return render(request, 'forms/new_price.html', {"form": form})

def create_borehole(request):
    SECRET_KEY = 'm3wl4ce_4aj73%vpaa!bn$6aa%&9=pho8!i#y=**t9-3_h5^@2'
    borehole = Borehole.objects.filter()
    form=NewBoreholeForm()
    if request.method == 'POST':
        form = NewBoreholeForm(request.POST, request.FILES)
        if form.is_valid():
            new_borehole = form.save(commit=False)
            new_borehole.save()
            return redirect('index')
    else:
        form=NewBoreholeForm()
    return render(request, 'forms/new_borehole.html', {"form": form})
    

def stat(request):
    stat = get_object(Stat)
    
    return render(request, 'templates/borehole.html', )
