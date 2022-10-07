from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_sort = request.GET.get("sort", 'id')

    if phones_sort == 'name':
        phones_objects = Phone.objects.all().order_by('name')
    elif phones_sort == 'min_price':
        phones_objects = Phone.objects. all().order_by('price')
    elif phones_sort == 'max_price':
        phones_objects = Phone.objects.all().order_by('-price')
    else:
        phones_objects = Phone.objects.all().order_by('id')

    context = {'phones' : phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    context = {'phone' : phone_object}
    return render(request, template, context)



