from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('product-list.html', views.products),
    path('cart.html', views.cart),
    path('checkout.html', views.checkout),
    path('my-account.html', views.myaccount),
    path('product-detail.html', views.productdetail),
    path('contact.html', views.contact),
    path('login.html', views.login),
    path('wishlist.html', views.wishlist),

]