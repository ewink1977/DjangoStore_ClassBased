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

class ProductUpdate(View):
    def post(self, request):
        updatedProduct = Product.objects.get(id = request.POST['prodID'])
        updatedProduct.manufacturer = request.POST['prodmanu']
        updatedProduct.name = request.POST['prodname']
        updatedProduct.price = request.POST['prodprice']
        updatedProduct.description = request.POST['proddesc']
        updatedProduct.save()
        productID = request.POST['prodID']
        return redirect('product_info', productID)

class ProductDelete(View):
    def get(self, request, id):
        deletingProduct = Product.objects.get(id = id)
        deletingProduct.delete()
        return redirect('products')
