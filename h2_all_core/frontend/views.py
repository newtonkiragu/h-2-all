from django.shortcuts import render, redirect, get_object_or_404
from .models import Borehole, Price, Stat
from django.db.models import Sum
from .form import NewPriceForm, NewBoreholeForm


# Create your views here.

def home(request):
    # NewProfileForm=form
    boreholes = Borehole.objects.all()
    return render(request, 'index.html', locals())


def make_stats(borehole):
    sales = borehole.stats.all()
    data = {
        'total_sales': sales.count(),
        'total_money': sum(map(lambda x: x.data['amount'], sales))
    }
    return data


def borehole(request, borehole_id):
    borehole = get_object_or_404(Borehole.objects, id=borehole_id)
    stats = make_stats(borehole)
    return render(request, 'borehole.html', locals())


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
        form = NewPriceForm(request.POST, request.FILES)
        if form.is_valid():
            current_price = form.save(commit=False)
            current_price.price = current_price
            current_price.save()
            return redirect('index')
    else:
        form = NewPriceForm()
    return render(request, 'forms/new_price.html', {"form": form})


def create_borehole(request, borehole_id=None):
    SECRET_KEY = 'm3wl4ce_4aj73%vpaa!bn$6aa%&9=pho8!i#y=**t9-3_h5^@2'
    borehole = None
    if borehole_id is not None:
        borehole = get_object_or_404(Borehole.objects, id=borehole_id)
    print(borehole)
    form = NewBoreholeForm(instance=borehole)
    prices = Price.objects.all()
    if request.method == 'POST':
        form = NewBoreholeForm(request.POST, request.FILES, instance=borehole)
        if form.is_valid():
            new_borehole = form.save(commit=False)
            new_borehole.save()
            return redirect(home)
        else:
            print(form.errors)
    return render(request, 'forms/new_borehole.html', {"form": form, "prices": prices})


def stat(request):
    stat = get_object(Stat)

    return render(request, 'templates/borehole.html', )
