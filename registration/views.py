from django.shortcuts import render, redirect
from .forms import Signup_form
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created! Log In Now')
            return redirect('login')    
    else:
        form=Signup_form()
    return render(request,'registration/register1.html',{'form':form})
