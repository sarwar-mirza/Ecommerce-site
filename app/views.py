from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OderPlaced, User
from .forms import CustomerRegistrationForm
from django.contrib import messages



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



# SPECIFIC FILTER FOOTBALL PRODUCT IN BRAND 

def football(request, data=None):
    
    if data == None:
      football = Product.objects.filter(category='F')
    elif data == 'adidas' or data == 'Nike' or data == 'Easton':
       football = Product.objects.filter(category='F').filter(brand=data)
    
    elif data == 'bellow':
        football = Product.objects.filter(category='F').filter(discount_price__lt= 90)
    elif data == 'above':
        football = Product.objects.filter(category='F').filter(discount_price__gte= 100)
    return render(request, 'app/football.html', {'football': football})



# SPECIFIC FILTER CRICKET PRODUCT IN BRAND 

def cricket(request, data=None):
    
    if data == None:
      cricket = Product.objects.filter(category='C')
    elif data == 'adidas' or data == 'Easy':
       cricket = Product.objects.filter(category='C').filter(brand=data)
    
    elif data == 'bellow':
        cricket = Product.objects.filter(category='C').filter(discount_price__lt= 90)
    elif data == 'above':
        cricket = Product.objects.filter(category='C').filter(discount_price__gte= 100)
    return render(request, 'app/cricket.html', {'cricket': cricket})


# ALL PRODUCT 
def allproduct(request):
    allprod = Product.objects.all()
    return render(request, 'app/allproduct.html', {'allproduct':allprod})



#CUSTOMER REGISTRATION FORM 

class RegistrationFormView(View):
    def get(self, request):
        fm = CustomerRegistrationForm()
        return render(request, 'app/registrationform.html', {'form':fm})
    
    def post(self, request):
        fm = CustomerRegistrationForm(request.POST)

        if fm.is_valid():
            messages.success(request, "Congratulations your account has been created successfully !!!")
            fm.save()

        return render(request, 'app/registrationform.html', {'form':fm})


