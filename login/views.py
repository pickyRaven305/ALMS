from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
from .forms import RegisterForm, ProfileForm,UserPasswordChangeForm,UpdateEmailForm
from .models import User_profile
from django.contrib.auth.models import User
from datetime import datetime





# Create your views here.
# user login page and user creation logic
def login_user(request):
    if request.method == "POST":
        username = request.POST['email'] #getting username
        password = request.POST['password']#getting password
        user = authenticate(request, username=username, password=password) #authenticating a user
        
        # if user is authenticated
        if user is not None:
            login(request, user)
            messages.success(request,'welcome ' + request.user.first_name +" "+request.user.last_name)       
            return redirect("/") 
    
        else:
            messages.error(request,'Login Unscessfull')
            return redirect("/auth/login_user") 
                   
    else:
        return render(request,"auth/login.html",{})
    
#user logout
def signout(request):
    logout(request)
    return redirect("/")

#new user registeration and login
def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #geting details from html
            firstName = request.POST.get('first_name')
            lastName = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password1')
            C_password = request.POST.get('password2')
            address  = str(request.POST.get('address'))
            city  = str(request.POST.get('city'))
            state  = str(request.POST.get('state'))
            zipcode  = str(request.POST.get('zipcode'))
            
            # checks for dulicate user
            if (User.objects.filter(username=email).exists()):
                messages.error(request,"user already exists !!!")
                return render(request, 'auth/register.html', context={'form': form})

         
            else:
                
                try:
                    user_profile = User_profile(first_name=firstName,last_name=lastName,email=email,address= address,phone=phone,city = city , state= state, zipcode=zipcode)
                    user = User.objects.create_user(username = email,password = password,date_joined = datetime.today(),first_name = firstName,last_name = lastName,email = email)
                    user_profile.save()
                    user.save()
                    login(request, user)
                    messages.success(request,"User regsistered sucessfully")
                    return redirect('/')
                
                
                except Exception as e:
                    messages.error(request,"Some error occured!!")
                    print(e)
                    
          
    return render(request, 'auth/register.html', context={'form': form})

# upadate user info 
def profile(request,pk):
    user=User.objects.get(id=pk)
    user_profile=User_profile.objects.get(email=user.email)
    #intializing the fields with current data to be corrected
    form = ProfileForm(initial={'email':user_profile.email,"first_name":user_profile.first_name,"last_name":user_profile.last_name,"phone":user_profile.phone,"address":user_profile.address,"city":user_profile.city,"state":user_profile.state,"zipcode":user_profile.zipcode})
    if request.method == 'POST':
            form = ProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                try:
                    #geting details from html
                    
                    firstName = request.POST.get('first_name')
                    lastName = request.POST.get('last_name')
                    email = request.POST.get('email')
                    phone = request.POST.get('phone')
                    address  = str(request.POST.get('address'))
                    city  = str(request.POST.get('city'))
                    state  = str(request.POST.get('state'))
                    zipcode  = str(request.POST.get('zipcode'))
                    
                    update_user_profile = User_profile(id=user_profile.id,first_name=firstName,last_name=lastName,email=email,address= address,phone=phone,city = city , state= state, zipcode=zipcode)
                    
                    user.username = email
                    user.first_name=firstName
                    user.last_name=lastName
                    user.email=email
                    
                    user.save()            
                    update_user_profile.save()
                    logout(request)
                    
                    return redirect("/")

                except Exception as e:
                    print(e)
                    messages.error(request,"something went wrong please try again")   
        
    return render(request,'auth/profile.html',context={"form":form})

# change pasword logic
def change_password(request,pk):
    #getting user details
    user=User.objects.get(id=pk)
    user_profile=User_profile.objects.get(email=user.email)
    
    form = UserPasswordChangeForm(request.user,request.POST)   
    
    if request.method=='POST':
        form = UserPasswordChangeForm(request.user,request.POST)   
        if form.is_valid():
            #upadting password with hash algo
            user=form.save()
            update_session_auth_hash(request, user)
                
            messages.success(request, 'Your password was successfully updated! Please login again')
            logout(request)
            return redirect("/")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserPasswordChangeForm(request.user)
        return render(request, "auth/change_password.html", {
        'form': form})
            
    return render(request,"auth/change_password.html",context={"form":form})

#updating email
def update_email(request,pk):
    #getting user details
    user=User.objects.get(id=pk)
    user_profile=User_profile.objects.get(email=user.email)
    
    form = UpdateEmailForm(initial={'email':user_profile.email})
    
    if request.method == 'POST':
            form = UpdateEmailForm(request.POST)
            if form.is_valid():
                #getting email
                try:
                    email = request.POST.get('email')

                        #checking if user with same email already exsists
                    if (User.objects.filter(username=email).exists()):
                        messages.error(request,"user already exists !!!") 
                        return render(request,'auth/update_email.html',context={"form":form})
 
                    else:
    
                        update_user_profile = User_profile()
                        
                        user_profile.email=email
                        
                        user.username = email
                        user.email=email
                        
                        user.save()            
                        update_user_profile.save()
                        
                        logout(request)
                        return redirect("/")

                except Exception as e:
                    print(e)
                    messages.error(request,"something went wrong please try again")   
    
    return render(request,'auth/update_email.html',context={"form":form})

