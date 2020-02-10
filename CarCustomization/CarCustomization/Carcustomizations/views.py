
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Carcustomizations.models import Customerlist
from django.db.models import Q
from django.contrib.auth.models import User,auth,Permission
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


from Carcustomizations.forms import LoginForm,RegisterForm
# Create your views here.

def home(request):
 
    return render(request,'index.html')



def contact(request):
 
    return render(request,'contact.html')

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("error.......")
            messages.error(request,"Invalid username")

    return render(request, "auth/login.html", context=context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password_first")
        new_user = User.objects.create_user(username, email, password)
    return render(request, "auth/register.html", context=context)

def logout_page(request):
    logout(request)
    return redirect('/')
    
def search(request): 
    
    query = request.GET['query']
    # allPosts = Post.objects.all()
    allPosts= Customerlist.objects.filter(Q(name__icontains=query) | Q(address__icontains=query))


    params = {'allPosts':allPosts,'query':query}
  
    return render(request,'search.html',params)


 
 
    
