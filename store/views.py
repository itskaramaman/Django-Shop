from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem

def home(request):
    query_set = Product.objects.values('id', 'title')
    return render(request, 'index.html', {'products': list(query_set)})
