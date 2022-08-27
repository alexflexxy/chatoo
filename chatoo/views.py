from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ChatForm, UserForm, PicturesForm, ProfileForm
from .models import Profile


# Create your views here.
def home(request):
    return render(request, 'chatoo/index.html')

def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = PicturesForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                profile.profile_pic = request.FILES['photo']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = PicturesForm()
    return render(request, 'registration/signup.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered} )

@login_required
def dashboard(request):
    if request.method == "POST":
        form = ChatForm(request.POST or None)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.save()
            return redirect("dashboard")
    
    form = ChatForm()
    return render(request, 'chatoo/dashboard.html', {"form": form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "chatoo/profile_list.html", {"profiles": profiles})

def profile(request, pk):      
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "chatoo/profile.html", {"profile": profile})
