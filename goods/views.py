from django.shortcuts import render

from goods.models import Products


# Create your views here.
#    goods    приложение

def catalog(request):

    goods = Products.objects.all()
    context = {
        'title':'Home - Catalog',
        'goods': goods,
    }
    return render(request, 'catalog.html',context)

def product(request):
    return render(request, 'product.html')



