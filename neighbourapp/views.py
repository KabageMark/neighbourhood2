from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,NeighbourHood,Business
from .forms import NewProfileForm
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

# def NewProfiles(request):
#     return render(request, 'profile.html')