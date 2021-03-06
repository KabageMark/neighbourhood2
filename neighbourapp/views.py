from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,NeighbourHood,Business,Post
from .forms import NewProfileForm,NewBusinessForm,NewNeighbourHoodForm,NewPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    title = 'neighbourhood'
    neighbourhood = NeighbourHood.get_all()
    form = NewNeighbourHoodForm
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            new_neighbourhood = form.save()
            new_neighbourhood.user = current_user
            new_neighbourhood.save()
        return redirect('neighbourhood')
    return render(request, 'neighbourhood.html',{ "neighbourhood": neighbourhood,"form":form,})

@login_required(login_url='/accounts/login/')
def Profiles(request):
    profile = Profile.get_all()
    form = NewProfileForm
    title = 'neighbourhood'
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save()
            new_profile.user = current_user
            new_profile.save()
        return redirect('profile')
    return render(request, 'profile.html',{"profile":profile,"form":form})

@login_required(login_url='/accounts/login/')
def business(request):
    business = Business.get_all()
    form = NewBusinessForm
    title = 'neighbourhood'
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            new_business = form.save()
            new_business.user = current_user
            new_business.save()
        return redirect('business')
    return render(request, 'business.html',{"business":business, "form":form})

@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.get_all()
    form = NewPostForm
    title = 'neighbourhood'
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            new_post.user = current_user
            new_post.save()
        return redirect('home')
    return render(request, 'index.html',{"posts":posts, "form":form})

def search_results(request):
    title = 'neighbourhood'
                                                                  
    if 'search' in request.GET and request.GET['search']:
        search_item = request.GET.get('search')
        searched_business = Business.objects.filter(name=search_item)
        message = f"{searched_business}"
        return render(request, 'search.html',{"message":message,"business": searched_business})
    else:
        message = "You haven't searched for any business"
        return render(request, 'search.html',{"message":message})