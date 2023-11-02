from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OderPlaced, User
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse


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


#CUSTOMER PROFILE 
class UserProfileView(View):
    def get(self, request):
        fm = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': fm, 'active': 'btn-primary'})
    
    def post(self, request):
        fm = CustomerProfileForm(request.POST)

        if fm.is_valid():
            usr = request.user
            name = fm.cleaned_data['name']
            aria = fm.cleaned_data['aria']
            city = fm.cleaned_data['city']
            zipcode = fm.cleaned_data['zipcode']
            division = fm.cleaned_data['division']

            regi = Customer(user=usr, name=name, aria=aria, city=city, zipcode=zipcode, division=division)
            regi.save()
            messages.success(request, 'Congratulations your profile has been update successfully !!!')
        return render(request, 'app/profile.html', {'form': fm, 'active': 'btn-primary'})



#ADDRESS VIEW
class AddressView(View):
    def get(self, request):
        add = Customer.objects.filter(user=request.user)
        return render(request, 'app/address.html', {'address': add, 'active': 'btn-primary'})
    


#ADD TO CART REDIRECT SHOW CART
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)

    Cart(user=user, product=product).save()      # authenticate user & product id save

    return redirect('/cart')


# SHOW CART (total calculation)
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)

    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]

    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount
            totalamount = amount + shipping_amount
        return render(request, 'app/add_show_cart.html', {'carts':cart, 'totalamount': totalamount, 'amount': amount})
    
    else:
        return render(request, 'app/emptycart.html')
    




#QUANTITY PLUS

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()

        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]

        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount
            totalamount = amount + shipping_amount

        data ={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }

        return JsonResponse(data)




#QUANTITY MINUS

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()

        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]

        for p in cart_product:
            tempamount = (p.quantity * p.product.discount_price)
            amount += tempamount
            totalamount = amount + shipping_amount

        data ={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }

        return JsonResponse(data)


# QUANTITY REMOVE
def remove_cart(request):                     
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))

        c.delete()

        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]

        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount


        data = {
        'amount': amount,
        'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)
    

    
