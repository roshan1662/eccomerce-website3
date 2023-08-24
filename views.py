from django.shortcuts import render,redirect
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request):
    totalitem =0
    topwears =Product.objects.filter(category='Tw')
    bottomwears =Product.objects.filter(category='BW')
    mobile =Product.objects.filter(category='M')
    # totalitem = len(Cart.objects.filter(user=request.user))

    return render(request, 'app/home.html',{'tw':topwears,'bw':bottomwears,'m':mobile})

def product_detail(request,pk):
    totalitem =0

    data = Product.objects.get(id=pk)
    item_already_in_cart = False
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        item_already_in_cart = Cart.objects.filter(Q(product=data.id) & Q (user=request.user)).exists()
    return render(request, 'app/productdetail.html',{'data':data,'item_already_in_cart':item_already_in_cart,'totalitem':totalitem})


@login_required(login_url='login')
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    # print(product)
    
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')


@login_required(login_url='login')
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        totalitem =0
        cart_product = [p for p in Cart.objects.all() if p.user == user ]
        # print(cart_product)
        totalitem = len(Cart.objects.filter(user=request.user))

        if cart_product:
            for p in cart_product:

                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})

        else:
            return render(request,'app/emptycart.html',{'totalitem':totalitem})

def buy_now(request):
 return render(request, 'app/buynow.html')


# @method_decorator(login_required,name='dispatch')
@login_required(login_url='login')
def profile(request):
    # if request.method== 'POST':
    #     u=request.POST(request.user)
    #     n=request.POST.get('name')
    #     a1=request.POST.get('add1')
    #     a2=request.POST.get('add2')
    #     c=request.POST.get('city')
    #     s=request.POST.get('state')
         
        #  data=costomer(username=u

    #     <label for="inputName" class="form-label">Name</label>
    #   <input type="text" class="form-control" id="inputEmail">
    # </div>
    # <div class="col-12">
    #   <label for="inputAddress" class="form-label">Address</label>
    #   <input type="text" class="form-control" id="inputAddress" placeholder="1234 Main St">
    # </div>
    # <div class="col-12">
    #   <label for="inputAddress2" class="form-label">Address 2</label>
    #   <input type="text" class="form-control" id="inputAddress2" placeholder="Apartment, studio, or floor">
    # </div>
    # <div class="col-12">
    #   <label for="inputCity" class="form-label">City</label>
    #   <input type="text" class="form-control" id="inputCity">
    # </div>
    # <div class="col-md-4">
    #   <label for="inputState" class="form-label">State</l
    form=costomerform()
    totalitem =0
    totalitem = len(Cart.objects.filter(user=request.user))

    if request.method == 'POST':
        form=costomerform(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city= form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            data = Costomer(user=usr,name=name,locality=locality,city=city,state=state,
            zipcode=zipcode
            )
            data.save()
            messages.success(request,"congrotulations!! profile has been saved")

            
    return render(request, 'app/profile.html',{'form':form,'active':"btn-primary",'totalitem':totalitem})


@login_required(login_url='login')
def address(request):
    totalitem =0
    totalitem = len(Cart.objects.filter(user=request.user))

    add=Costomer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'totalitem':totalitem,'active':"btn-primary"})


@login_required(login_url='login')
def orders(request):
    totalitem =0
    totalitem = len(Cart.objects.filter(user=request.user))

    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op,'totalitem':totalitem})

def change_password(request):
    if request.method == "POST":
    
        newpass=request.POST.get('npass')
        totalitem =0
        totalitem = len(Cart.objects.filter(user=request.user))
        u=User.objects.get(username=request.user.username)
        u.set_password(newpass)
        u.save()
        messages.success(request,"Password has been changed")
        # return redirect('login')
    return render(request, 'app/changepassword.html',{'totalitem':totalitem})

def mobile(request,data=None):

    totalitem =0
    totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        mobiles=Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung':

        mobiles=Product.objects.filter(category='M').filter(brand=data)

    return render(request, 'app/mobile.html',{'mobiles':mobiles,'totalitem':totalitem})

def laptop(request,data=None):
    if data == None:
        laptop=Product.objects.filter(category='L')
    elif data == 'hp' or data == 'dell':

        laptop=Product.objects.filter(category='L').filter(brand=data)

    return render(request, 'app/laptop.html',{'laptop':laptop})




def topwear(request):
    topwear=Product.objects.filter(category='Tw')
    return render(request, 'app/topwear.html',{'topwear':topwear})

def bottomwear(request):
    bottomwear=Product.objects.filter(category='BW')
    return render(request, 'app/bottomwear.html',{'bottomwear':bottomwear})    





def loginpage(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user=authenticate(request,username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         return redirect('profile')
    # if request.method=='POST':
    #     u=request.POST.get('username')
    #     p=request.POST.get('password')
    #     user=authenticate(request,username=u,password=p)
    #     # print(user)
    #     if user is not None:

    #         login(request,user)
    #         return redirect('profile')
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None :

            # login(request,user)
            login(request,user)
            return redirect('profile')
        else:
            # return HttpResponse ("Username or Password is incorrect!!!")
            messages.success(request,"Username or Password is incorrect!!!")
    return render(request, 'app/login.html')


def customerregistration(request):
    # form=CostomerRegistrationForm()
    # if request.method== 'POST':
    #     form=CostomerRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            # return HttpResponse("Your password and confrom password are not Same!!")
            messages.success(request,"Your password and confrom password are not Same!!")

        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'username is already exists')
            return redirect('customerregistration')  

        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email is already exists')
            return redirect('customerregistration')                
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'app/customerregistration.html')

def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def checkout(request):
    user = request.user
    add = Costomer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user ]
        # print(cart_product)
    if cart_product:
        for p in cart_product:

            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        total_amount = amount+shipping_amount    
    return render(request, 'app/checkout.html',{'add':add,'totalamount':total_amount,'cart_items':cart_items})


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity +=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data ={
            'quantity':c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
            } 
        return JsonResponse(data)



def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        c.quantity -=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            

        data ={
            'quantity':c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
            } 
        return JsonResponse(data)

        

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user = request.user))
        
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
           

        data ={
          
            'amount' : amount,
            'totalamount' : amount + shipping_amount
            } 
        return JsonResponse(data)    

@login_required(login_url='login')
def payment_done(request):
    user = request.user
    costid = request.GET.get('custid')
    costomer = Costomer.objects.get(id=costid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,costomer=costomer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')    

                
