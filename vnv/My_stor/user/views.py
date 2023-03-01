from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ("/")
   
    context ={}  
    return render(request,'user/signin.html',context)

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "user/signin.html")
            
    else:
        form = CreateUserForm()
    context = {"form":form}
    return render(request,'user/register.html',context)
    


