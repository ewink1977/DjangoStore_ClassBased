from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('products/', views.Products.as_view(), name = 'products'),
    path('products/<int:id>/', views.ProductView.as_view(), name = 'product_info'),
    path('products/update/', views.ProductUpdate.as_view(), name = 'product_update'),
    path('products/update/delete/<int:id>', views.ProductDelete.as_view(), name = 'product_delete'),
]