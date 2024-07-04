from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def Home(request):
    return render(request,'index.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = request.user
        user = authenticate(user,username = username , password = password)
        if user != None:
            login(request,user)

        return redirect('Home')

    return render(request,'login_page.html')

def Sign_in(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')

    else : 
        form = UserCreationForm()

    context = {'form':form}
    return render(request,'Sign_up.html',context)

def Logout(request):
    logout(request)
    return redirect('Home')