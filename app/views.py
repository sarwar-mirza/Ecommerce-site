from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OderPlaced



# HOME CLASS VIEW INHERITE VIEW FILE
class ProductHomeView(View):
    def get(self, request):
        baseball = Product.objects.filter(category='B')
        football = Product.objects.filter(category='F')
        cricket = Product.objects.filter(category='C')

        context = {'baseball': baseball, 'football': football, 'cricket': cricket}
        return render(request, 'app/home.html', context)
    



#PTODUCT DETAIL VIEW
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        
        return render(request, 'app/productdetail.html', {'product': product})


# SPECIFIC FILTER BASEBALL PRODUCT IN BRAND 

def baseball(request, data=None):
    
    if data == None:
      baseball = Product.objects.filter(category='B')
    elif data == 'adidas' or data == 'Nike' or data == 'Easton':
       baseball = Product.objects.filter(category='B').filter(brand=data)
    
    elif data == 'bellow':
        baseball = Product.objects.filter(category='B').filter(discount_price__lt= 90)
    elif data == 'above':
        baseball = Product.objects.filter(category='B').filter(discount_price__gt= 100)
    return render(request, 'app/baseball.html', {'baseball': baseball})


