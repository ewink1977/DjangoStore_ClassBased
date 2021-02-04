from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product

class Home(View):
    def get(self, request):
        return render(request, 'html/home.html')

class Products(View):
    def get(self, request):
        context = {
            'products': Product.objects.all()
        }
        return render(request, 'html/products_all.html', context)

    def post(self, request):
        Product.objects.create(
            name = request.POST['prodname'],
            manufacturer = request.POST['prodmanu'],
            price = request.POST['prodprice'],
            description = request.POST['proddesc']
        )
        return redirect('products')

class ProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        context = {
            'product': product
        }
        return render(request, 'html/product.html', context)

