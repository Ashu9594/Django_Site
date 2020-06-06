from django.http import HttpResponse
from django.shortcuts import render
from .models import Category

# Create your views here.
def home(request):

    cat1 = Category()
    cat1.name = 'Adidas'
    cat1.price = 12500
    cat1.desc = 'this is the best footwear brand'
    cat1.img = 'footwear.jpg'

    cat2 = Category()
    cat2.name = 'Samsung M10'
    cat2.price = 25000
    cat2.desc = ' this is the desc for samsung'
    cat2.img = 'samsung.jpeg'
    
    cat3 = Category()
    cat3.name = 'Dell'
    cat3.price = 500000
    cat3.desc = 'this is dell laptop'
    cat3.img = 'dell.jpeg'
    

    # cat4 = Category() 
    # cat4.name = 'Dell'
    # cat4.price = 500000
    # cat4.desc = 'this is dell laptop'
    # cat4.img = 'dell.jpeg'
    
    cat = [cat1,cat2,cat3]
    return render(request, 'home.html',{'cat':cat})
    