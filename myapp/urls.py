"""Infinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from myapp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='infinity_home'),
    path('shop/products/', views.products, name='products'),
    path('shop/products/<int:cat_id>/<c_slug>', views.products_cat, name='products-cat'),
    path('shop/product/overview/<int:cat_id>/<c_slug>/<int:p_id>/<p_slug>', views.product_overview,
         name='product_overview'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blog_detail, name='blog-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='shopping-cart'),
    path('add-to-cart/<user_id>/item:<int:p_id>/', views.add_to_cart, name='add_to_cart'),
]
