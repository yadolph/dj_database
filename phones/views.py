from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    order = request.GET.get('sort')
    template = 'catalog.html'
    phones = Phone.objects.all().values()

    if order == 'min_price':
        phones = sorted(phones, key = lambda k: k['price'])
    elif order == 'max_price':
        phones = sorted(phones, key=lambda k: k['price'], reverse=True)
    elif order == 'alphabetic':
        phones = sorted(phones, key=lambda k: k['name'])

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.filter(slug = slug).values()[0]
    print(product)
    context = {'product': product}
    return render(request, template, context)
