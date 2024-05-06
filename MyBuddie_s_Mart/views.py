from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import json
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def Homepage(request):
    shop = Shop.objects.filter(status = 0)
    top_sell = Product.objects.filter(top_selling=1,status=0)  
    my_product = Product.objects.filter(status=0)  
    email_id = User.email
    if request.user.is_authenticated:
            cart =Cart.objects.filter(user = request.user)
            my_cart =len(cart)        
    # print(email_id)
    return render(request,'home.html',{"shops":shop,"topsellings":top_sell,"mymail":email_id,"my_product":my_product,"mycart": my_cart if request.user.is_authenticated else " "})    # if id is not login use  below  return line

def Shop_page(request):
    shop = Shop.objects.filter(status = 0)
    top_sell = Product.objects.filter(top_selling=1,status=0)   
    email_id = User.email
    if request.user.is_authenticated:
             cart =Cart.objects.filter(user = request.user)
             mycart =len(cart)
    return render(request,'main_shop.html',{"shops":shop,"topsellings":top_sell,"mymail":email_id,"mycart": mycart if request.user.is_authenticated else " "})
    

def Myproduct(request,name):
    if(Shop.objects.filter(name=name,status=0)):
        product = Product.objects.filter(shop__name=name,status = 0)
        myShop_name = name
        shop = Shop.objects.filter(status = 0)
        if request.user.is_authenticated:
                cart =Cart.objects.filter(user = request.user)
                mycart =len(cart)
        # myProduct = Product.objects.filter(status = 0 )
        return render(request,"product.html",{"products":product,"shop_name":myShop_name,"shops":shop,"mycart": mycart if request.user.is_authenticated else " "})
    else:
        messages.warning(request,"No Such Catagory Found")    
        return redirect('homepage')

def Product_details(request,sname,pname):
    if(Shop.objects.filter(name=sname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            myProduct_details =Product.objects.filter(name=pname,status=0).first()
            if request.user.is_authenticated:
                cart =Cart.objects.filter(user = request.user)
                mycart =len(cart)
            return render(request,"product_details.html",{"our_products": myProduct_details,"shop_name":sname,"mycart": mycart if request.user.is_authenticated else " "}) 
        else:
            messages.warning(request,"No Such product Found")    
            return redirect('homepage')  
    else:
        messages.warning(request,"No Such shop Found")    
        return redirect('homepage')     
    
def Add_to_cart(request):
  if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
        data=json.load(request)
        # print(data['product_qty'])
        # print(data['pid'])
        # print(request.user.id)
        product_qty=data['product_qty']
        product_id=data['pid']
        product_status=Product.objects.get(id=product_id)
        if product_status:
            if Cart.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'Product Already in Cart'}, status=200)
            else:
                if product_status.quantity>=product_qty:
                    Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty,shop_name= product_status.shop,product_name=product_status.name)
                    return JsonResponse({'status': 'Product Added to Cart :)'}, status=200)
                else:
                    return JsonResponse({'status': 'Product Stock Not Available!'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart!'}, status=200)
  else: 
    return JsonResponse({'status':'Invalid Access!'}, status=200)   
    
def My_cart(request):
    if request.user.is_authenticated:
        cart =Cart.objects.filter(user = request.user)
        mycart =len(cart)
        my_product=[]
        for a in cart:
          my_product = a.shop_name  
        # print(my_product)        
             
    # print("########################################################")
    # print(request.user.email) 

        # my_pro=[]
        # for a in cart:
        #     my_pro.append(a.product_name)    to get a product name
        # print(my_pro)

        # print(request.user.email)        to get customer email 

        return render(request,'cart.html',{"my_carts":cart,"mycart":mycart,"myshopname":my_product})
    else:
        messages.error(request, "Login to Use Cart")
        return redirect("homepage")
    
def Remove_cart(request,cid):
    cartitem = Cart.objects.get(id=cid) 
    cartitem.delete()
    return redirect("/cart")

def Suppor(request):
    if request.user.is_authenticated:
                cart =Cart.objects.filter(user = request.user)
                mycart =len(cart)
    return render(request, 'support.html',{"mycart": mycart if request.user.is_authenticated else " "})

def Signuppage(request):
    if request.method=='POST':
        username = request.POST.get('signup-name')
        email = request.POST.get('signup-email')
        password = request.POST.get('signup-password')

        try:
            if User.objects.get(username=username):
                messages.info(request,"Username is Already Taken")
                return redirect(Signuppage)
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email is Already Taken")
                return redirect(Signuppage)
        except:
            pass

        my_user = User.objects.create_user(username,email,password)
        my_user.save()
        messages.success(request,"Created Successfully, please Sign in")
        return redirect('signinpage')
        
    return render(request,'signup.html')

def Signinpage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method=='POST':
            myUsername  = request.POST.get('signin-name')
            myPassword = request.POST.get('signin-password')

            user = authenticate(request,username=myUsername,password=myPassword)
            if user is not None:
                login(request,user)
                messages.success(request, "Logged in Successfully ")
                return redirect('homepage')
            else:
                messages.error(request, "Invalid UserName or Password")
                return redirect(Signinpage)
        
        return render(request,'signin.html')

def Logout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('homepage')


#this for email

def Checkout_mail(request):
    cart = Cart.objects.filter(user = request.user)
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
     if request.method=='POST':
        udata=json.load(request)
        my_user_number =udata['our_user_number']
        my_user_address =udata['our_user_address']

         
        my_product=''
        totol_amount = 0
        for a in cart:
            my_product += str("\t"+a.product_name +" "+ " RS: "+ str(int(a.product.price)) + " - "+ str(a.product_qty) + " => "+"\t"+ str(a.shop_name) ) + "\n"
            totol_amount += int(a.product.price)*int(a.product_qty)

    # print("#################################################################")  ###  
    # print(my_product) ###
    # print(totol_amount) ###

        subject = "Happy Shopping :)"
        message = "Your Order is Placed Successfully. "+ "\n" + "your Products will deliver within 15 Minutes" + "\n" "\n" +"\t"+ "Thank You for Shopping with Us :)"
        email = request.user.email
        MY_EMAIL_HOST_USER =settings.EMAIL_HOST_USER
        recipient_list =[email]
        send_mail(subject,message,MY_EMAIL_HOST_USER,recipient_list,fail_silently=True)

        subject = "Happy Shopping :)"
        message = "New Order is Arrived !"+"\n"+"Our Customer's Mobile Number is - "+my_user_number+"\n"+"Our Customer's Address is - "+my_user_address.upper()+"\n"+" your Products are "+"\n \n" + my_product +"\n"+"Total Amount = "+str(totol_amount)
        # email = request.user.email  ###
        MY_EMAIL_HOST_USER =settings.EMAIL_HOST_USER
        # recipient_list =['bhuvanesh1123121@gmail.com']
        recipient_list =['karthikeyan934288@gmail.com']
        # recipient_list =[email] ###
        send_mail(subject,message,MY_EMAIL_HOST_USER,recipient_list,fail_silently=True)
    
    messages.success(request,"Your Order is Placed Successfully :)")
    cart.delete()    
    return redirect('homepage')


