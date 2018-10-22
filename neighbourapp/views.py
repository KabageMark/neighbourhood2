from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,NeighbourHood,Business
from .forms import NewProfileForm,NewBusinessForm
# Create your views here.
def home(request):
    return render(request, 'index.html')


def Profiles(request):
    profile = Profile.get_all()
    form = NewProfileForm
    title = 'awards'
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save()
            new_profile.user = current_user
            new_profile.save()
        return redirect('profile')
    return render(request, 'profile.html',{"profile":profile,"form":form})

def business(request):
    business = Business.get_all()
    form = NewBusinessForm
    title = 'awards'
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            new_business = form.save()
            new_business.user = current_user
            new_business.save()
        return redirect('business')
    return render(request, 'business.html',{"business":business, "form":form})