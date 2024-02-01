from django.shortcuts import render

# Create your views here.
#    goods    приложение

def catalog(request):
    return render(request, 'catalog.html')

def product(request):
    return render(request, 'product.html')



