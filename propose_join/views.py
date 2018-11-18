from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ExistingClub,ProposedClub
from administration.models import Onpollclub
from .forms import ProposedClubForm
from django.contrib.auth import get_user_model
from registration.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator


def existingClubList(request):
    
    clubs = ExistingClub.objects.all()
    paginator = Paginator(clubs,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'clubs': clubs,
    }
    return render(request,'propose_join/exlist.html', context)

def proposedClubList(request):
    clubs = Onpollclub.objects.all()
    paginator = Paginator(clubs,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'clubs': clubs,
    }
    return render(request,'propose_join/prlist.html', context)


def proposeClub(request):
    form = ProposedClubForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = ProposedClubForm(request.POST, request.FILES)
        #print(request.user)
        #print(request.POST)
        if form.is_valid():
            club1 = form.save(commit=False)
            club1.name = request.user
            #CustomUser.objects.get(Username=request.user)
            club1.save()
            messages.success(request, f'Your Club Has Been Proposed')
            return redirect('user-home')
    else:
        form = ProposedClubForm()
    context = {
            'form' : form,
    }
    return render(request, 'propose_join/home.html', context)