from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import AddItemForm,DonateForm
from .models import Item,orders,Donate
from django.contrib.auth.models import User
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from login.models import User_profile

# Create your views here.
#loading add item page

def add_item(request,pk):
    form = AddItemForm()
    
    if request.method=='POST':
        form = AddItemForm(request.POST,request.FILES)
        if form.is_valid():
            #getting data from html pages
            item_name=request.POST.get("item_name")
            item_category=request.POST.get("item_category")
            desc = request.POST.get("desc")
            item_cost = request.POST.get("cost")
            image = request.FILES.get("image")
            
            # if tehere si ocst for food it becomes 0
            if item_category == "food":
                item_cost = 0                
                
            item = Item(name=item_name,category=item_category,cost=item_cost,created_by=request.user,created_on=datetime.today())
            item.image=image
            item.save()
            messages.success(request, "Item added Sucessfully")
            
            messages.success(request, "Item added Sucessfully")               
            
    
    return render(request,"donation/add_item.html",context={"form":form})

#loading order item page


def order_item(request,pk):
    
#getting user and products details from  database
    user=User.objects.get(id=pk)
    products = Item.objects.all().filter(booked=False)
    
    #pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 4)
    try:
        prod_list = paginator.page(page)
    except PageNotAnInteger:
        (PageNotAnInteger)
        prod_list = paginator.page(1)
    except EmptyPage:
        (EmptyPage)
        prod_list = paginator.page(paginator.num_pages)
    
    if request.method=='POST':
        #getting data from html pages
        
        product_id = request.POST.get("submit")
        product_ordered = Item.objects.get(pk=product_id)
        if product_ordered.created_by == request.user:
            messages.error(request,"you can not place order for the item created by you")
            
        else:
            #craeting object of order and products_ordered and saving it
            order = orders(item_ordered = product_ordered,ordered_by=request.user,placed_on=datetime.today())
            order.save()
            
            product_ordered.booked = True
            product_ordered.booked_by = request.user
            product_ordered.save()
            
            created_by = product_ordered.created_by
            by_user = User_profile.objects.get(email = created_by.email)

            messages.success(request,'Order booked for ' + product_ordered.name +" @ Rs. " +str( product_ordered.cost)+"\n"+" from : \n Vendor : "+ by_user.first_name +" "+ by_user.last_name  +"\n"+"Vendor address : "+ by_user.address+"\n"+ by_user.city+" "+by_user.state+" - "+by_user.zipcode) 
        
    params={"products":products,"prod_list":prod_list}
    return render(request, "donation/order_item.html",params)

#loading uplods section

def uploads(request,pk):
#getting user and products details from  database
    
    user=User.objects.get(id=pk)
    products = Item.objects.all().filter(created_by = request.user,booked=False)
    
    #pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 4)
    try:
        prod_list = paginator.page(page)
    except PageNotAnInteger:
        (PageNotAnInteger)
        prod_list = paginator.page(1)
    except EmptyPage:
        (EmptyPage)
        prod_list = paginator.page(paginator.num_pages)
    
    #getting data from html pages
    if request.method=='POST':
        
        product_id = request.POST.get("submit")
        item = Item.objects.get(pk=product_id)
        item.delete()
    params={"prod_list":prod_list}
        
    return render(request, "donation/uploads.html",params)

#loading order history page

def order_history(request,pk):
#getting  products details from  database
    
    products = Item.objects.all().filter(booked_by = request.user)
    
    #pagination
    
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 4)
    try:
        prod_list = paginator.page(page)
    except PageNotAnInteger:
        (PageNotAnInteger)
        prod_list = paginator.page(1)
    except EmptyPage:
        (EmptyPage)
        prod_list = paginator.page(paginator.num_pages)
    if request.method=='POST':
            #getting data from html pages
        
        vendor_id= request.POST.get("submit")
        user = User.objects.get(pk = vendor_id)
        vendor_email = user.email
        by_user = User_profile.objects.get(email = vendor_email)
        vendor = User_profile.objects.get(pk = by_user.id)
        return render(request, "donation/order_history.html",{"prod_list":prod_list,"vendor":vendor})

    return render(request, "donation/order_history.html",{"prod_list":prod_list})
    
#loading donate page
    
def donate(request,pk):
    form = DonateForm()
    #getting data from html pages
    if request.method=='POST':
        
        form = DonateForm(request.POST)
        if form.is_valid():
            doanted_by = User.objects.get(pk=request.user.id)
            donated_amount=request.POST.get("amount")
            
            #checking for amount 
            if(donated_amount):
                donate  = Donate(donated_by=doanted_by,amount = donated_amount, donated_on = datetime.today())
                messages.success(request,"Thank you for doantion Rs. "+ donated_amount)
                donate.save()
                return render(request,"donation/payment_gateway.html")
                
    return render(request,"donation/add_item.html",context={"form":form})
    
#loading demo of an payment gateway page
    # only for demo purpose
def Payments(request):
    if request.method=='POST':   
            #getting data from html pages
             
        return render(request,"donation/payment_gateway.html")
#loading donations history page
        
def donation_history(request,pk):
#getting donations details from  database
    
    donations = Donate.objects.all().filter(donated_by = request.user)
    
    #pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(donations, 4)
    try:
        donor_list = paginator.page(page)
    except PageNotAnInteger:
        (PageNotAnInteger)
        donor_list = paginator.page(1)
    except EmptyPage:
        (EmptyPage)
        donor_list = paginator.page(paginator.num_pages)

    return render(request, "donation/donation_history.html",{"donor_list":donor_list,"donoations":donations})
    
    
    