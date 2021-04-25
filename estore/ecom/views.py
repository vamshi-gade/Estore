from django.shortcuts import render
from .models import Product
# Create your views here.

prod1 = Product()
prod1.name = 'Veni Vidi Vici'
prod1.price = '300'
prod1.img = 'Veni Vidi Vici  Black Ruched Bodycon Dress.png'
prod1.desc = 'Black Ruched Bodycon Dress'

prod2 = Product()
prod2.name = 'Harpa'
prod2.price = '100'
prod2.img = 'Harpa Women Black Printed A-Line Dress.png'
prod2.desc = 'Women Black Printed A-Line Dress'

prod3 = Product()
prod3.name = 'Tokyo Talkies'
prod3.price = '100'
prod3.img = 'Tokyo Talkies  Women Pink & Blue Floral Print Fit and Flare Dress.png'
prod3.desc = 'Women Pink & Blue Floral Print Fit and Flare Dress'

prod4 = Product()
prod4.name = 'Tokyo Talkies'
prod4.price = '100'
prod4.img = 'Tokyo Talkies  Women Black & White Checked Fit and Flare Dress.png'
prod4.desc = 'Women Black & White Checked Fit and Flare Dress'

prod5 = Product()
prod5.name = 'plusS'
prod5.price = '100'
prod5.img = 'plusS  Women Blue Solid Denim Shirt Dress.png'
prod5.desc = 'Women Blue Solid Denim Shirt Dress'

prod6 = Product()
prod6.name = 'Berrylush'
prod6.price = '100'
prod6.img = 'Berrylush  Drop Dead Gorgeous Cocktail Dress.png'
prod6.desc = 'Drop Dead Gorgeous Cocktail Dress'

prod7 = Product()
prod7.name = 'Berrylush'
prod7.price = '100'
prod7.img = 'Berrylush  Women Blue Printed Maxi Dress.png'
prod7.desc = 'Women Blue Printed Maxi Dress'

prod8 = Product()
prod8.name = 'SASSAFRAS'
prod8.price = '100'
prod8.img = 'SASSAFRAS  Women Olive Green & Pink Accordion Pleat Printed Maxi Dress.png'
prod8.desc = 'Women Olive Green & Pink Accordion Pleat Printed Maxi Dress'

prod9 = Product()
prod9.name = 'Libas'
prod9.price = '400'
prod9.img = 'Libas  Women Blue White Printed Maxi Dress.png'
prod9.desc = 'Women Blue White Printed Maxi Dress'

prod10 = Product()
prod10.name = 'Tokyo Talkies'
prod10.price = '100'
prod10.img = 'Tokyo Talkies  Women Rose Solid Pinafore Dress.png'
prod10.desc = 'Women Rose Solid Pinafore Dress'

prods = [prod1,prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10]


def index(request):
    return render(request, "index.html", {'prods': prods})
def products(request):
    return render(request, "product-list.html", {'prods':prods})
def cart(request):
    return render(request, "cart.html")
def checkout(request):
    return render(request, "checkout.html")
def myaccount(request):
    return render(request, "my-account.html")
def productdetail(request):
    return render(request, "product-detail.html", {'prods':prods})
def wishlist(request):
    return render(request, 'wishlist.html')
def login(request):
    return render(request, 'login.html')
def contact(request):
    return render(request, 'contact.html')
