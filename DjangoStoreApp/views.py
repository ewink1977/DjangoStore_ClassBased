from django.shortcuts import render
from django.views.generic import View

class Home(View):
    def get(self, request):
        return render(request, 'html/home.html')

class Products(View):
    def get(self, request):
        return render(request, 'html/products_all.html')

    def post(self, request):
        pass
