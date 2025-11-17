from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator

def home(request):
    products = Product.objects.filter(available=True).order_by('-created')[:24]
    categories = Category.objects.all()
    return render(request, 'core/home.html', {'products': products, 'categories': categories})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(available=True)
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    products_page = paginator.get_page(page)
    return render(request, 'core/product_list.html', {'category': category, 'products': products_page})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'core/product_detail.html', {'product': product})

def search(request):
    q = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=q, available=True)
    return render(request, 'core/product_list.html', {'products': products, 'query': q})
