from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import FormName
# Create your views here.

def index(request):
    mydict = {'my_entry':'My index App page'}
    return render(request,'AppTwo/index.html',mydict)
   

def help(request):
    mydict = {'my_entry':'My help App page'}
    return render(request,'AppTwo/help.html',mydict)

def user(request):
    user_list = User.objects.all()
    mydict = {'user':user_list}
    return render(request,'AppTwo/user.html',mydict)

def sign_up(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
        
    return render(request,'AppTwo/sign_up.html',{'form':form})
