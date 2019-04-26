from django.shortcuts import render, redirect
from .models import Borehole, Price, Stat
from .form import NewPriceForm

# Create your views here.

def home(request):
    # NewProfileForm=form
    return render(request, 'index.html', locals())

def borehole(request):
    return render(request, 'borehole.html', locals())

def create_fie(request):
    current_price = 0
    price = Price.objects.filter()
    form = NewPriceForm()

    if request.method == 'POST':
        form =  NewPriceForm(request.POST, request.FILES, )
        if form.is_valid():
            current_price = form.save(commit=False)
            current_price.price = current_price
            current_price.save()
            return redirect('index')
    else:
        form = NewPriceForm()
    return render(request, 'forms/new_price.html', {"form": form})
