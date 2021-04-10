from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):

    prod1 = Product()
    prod1.name = 'Black top'
    prod1.price = '100'
    prod1.img = 'product-1.jpg'

    prod2 = Product()
    prod2.name = 'Black top'
    prod2.price = '100'
    prod2.img = 'product-2.jpg'

    prod3 = Product()
    prod3.name = 'Black top'
    prod3.price = '100'
    prod3.img = 'product-3.jpg'

    prod4 = Product()
    prod4.name = 'Black top'
    prod4.price = '100'
    prod4.img = 'product-4.jpg'

    prod5 = Product()
    prod5.name = 'Black top'
    prod5.price = '100'
    prod5.img = 'product-5.jpg'

    prod6 = Product()
    prod6.name = 'Black top'
    prod6.price = '100'
    prod6.img = 'product-6.jpg'

    prod7 = Product()
    prod7.name = 'Black top'
    prod7.price = '100'
    prod7.img = 'product-7.jpg'

    prod8 = Product()
    prod8.name = 'Black top'
    prod8.price = '100'
    prod8.img = 'product-8.jpg'

    prod9 = Product()
    prod9.name = 'Black top'
    prod9.price = '100'
    prod9.img = 'product-9.jpg'

    prod10 = Product()
    prod10.name = 'Black top'
    prod10.price = '100'
    prod10.img = 'product-10.jpg'

    prods = [prod1,prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10]

    return render(request, "index.html", {'prods': prods})
def products(request):
    prod1 = Product()
    prod1.name = 'Black top'
    prod1.price = '100'
    prod1.img = 'product-1.jpg'

    prod2 = Product()
    prod2.name = 'Black top'
    prod2.price = '100'
    prod2.img = 'product-2.jpg'

    prod3 = Product()
    prod3.name = 'Black top'
    prod3.price = '100'
    prod3.img = 'product-3.jpg'

    prod4 = Product()
    prod4.name = 'Black top'
    prod4.price = '100'
    prod4.img = 'product-4.jpg'

    prod5 = Product()
    prod5.name = 'Black top'
    prod5.price = '100'
    prod5.img = 'product-5.jpg'

    prod6 = Product()
    prod6.name = 'Black top'
    prod6.price = '100'
    prod6.img = 'product-6.jpg'

    prod7 = Product()
    prod7.name = 'Black top'
    prod7.price = '100'
    prod7.img = 'product-7.jpg'

    prod8 = Product()
    prod8.name = 'Black top'
    prod8.price = '100'
    prod8.img = 'product-8.jpg'

    prod9 = Product()
    prod9.name = 'Black top'
    prod9.price = '100'
    prod9.img = 'product-9.jpg'

    prod10 = Product()
    prod10.name = 'Black top'
    prod10.price = '100'
    prod10.img = 'product-10.jpg'

    prods = [prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10]

    return render(request, "product-list.html", {'prods':prods})
def cart(request):
    return render(request, "cart.html")
def checkout(request):
    return render(request, "checkout.html")
def myaccount(request):
    return render(request, "my-account.html")
def productdetail(request):
    prod1 = Product()
    prod1.name = 'Black top'
    prod1.price = '100'
    prod1.img = 'product-1.jpg'

    prod2 = Product()
    prod2.name = 'Black top'
    prod2.price = '100'
    prod2.img = 'product-2.jpg'

    prod3 = Product()
    prod3.name = 'Black top'
    prod3.price = '100'
    prod3.img = 'product-3.jpg'

    prod4 = Product()
    prod4.name = 'Black top'
    prod4.price = '100'
    prod4.img = 'product-4.jpg'

    prod5 = Product()
    prod5.name = 'Black top'
    prod5.price = '100'
    prod5.img = 'product-5.jpg'

    prod6 = Product()
    prod6.name = 'Black top'
    prod6.price = '100'
    prod6.img = 'product-6.jpg'

    prod7 = Product()
    prod7.name = 'Black top'
    prod7.price = '100'
    prod7.img = 'product-7.jpg'

    prod8 = Product()
    prod8.name = 'Black top'
    prod8.price = '100'
    prod8.img = 'product-8.jpg'

    prod9 = Product()
    prod9.name = 'Black top'
    prod9.price = '100'
    prod9.img = 'product-9.jpg'

    prod10 = Product()
    prod10.name = 'Black top'
    prod10.price = '100'
    prod10.img = 'product-10.jpg'

    prods = [prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10]
    return render(request, "product-detail.html", {'prods':prods})
def wishlist(request):
    return render(request, 'wishlist.html')
def login(request):
    return render(request, 'login.html')
def contact(request):
    return render(request, 'contact.html')
