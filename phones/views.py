from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    order = request.GET.get('sort')
    template = 'catalog.html'
    phones = []
    if order == 'min_price':
        phones = Phone.objects.all().order_by('price').values()
    elif order == 'max_price':
        phones = Phone.objects.all().order_by('-price').values()
    elif order == 'alphabetic':
        phones = Phone.objects.all().order_by('name').values()
    else:
        phones = Phone.objects.all().values()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.filter(slug = slug).values()[0]
    print(product)
    context = {'product': product}
    return render(request, template, context)
