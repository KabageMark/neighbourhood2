from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile,NeighbourHood,Business
# Create your views here.
def welcome(request):
    return render(request, 'index.html')


def Profiles(request):
    profile = Profile.get_all()
    return render(request, 'profile.html',{"profile":profile,"image":image,})