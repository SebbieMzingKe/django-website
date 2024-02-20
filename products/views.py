from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Fruit
from . forms import FruitSearchForm

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', 
                  {'products':products})

def new(request):
    return HttpResponse('new product')

def search_fruits(request):
    form = FruitSearchForm(request.GET)
    fruits = Fruit.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')

        if search_query:
            fruits = fruits.filter(name__icontains = search_query)
            
    context = {'form':form, 'fruits':fruits}
    return render(request, 'fruit_search.html', context)