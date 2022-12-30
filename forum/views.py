from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Q
from django.core.paginator import Paginator # for pagination




from .models import User, Informations, Thread, Post

from django import forms

import re
from re import match
import random
from random import choice, randint
from django.views.decorators.csrf import csrf_exempt 


from django.shortcuts import redirect

# Create your views here.
def index(request):


    threads = Thread.objects.all().order_by('-post__post_created') #threads ordered by last post added
   
    threads2 = [] # this is created because if not, there were doubles
    
    for thread in threads:
        if thread not in threads2:
            threads2.append(thread) #this eliminates the doubles
    paginator = Paginator(threads2, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) #paginator options

    return render(request, "forum/index.html", {
        "threads": threads2,
        'page_obj': page_obj
        
            })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "forum/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "forum/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "forum/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            Informations.objects.create(who=user, origin="N/A", birth="1900-01-01", bio="N/A", image="images/noavatar.png", gender = "") # create informations also, related by key to the informations model, setting for example a default avatar

        except IntegrityError:
            return render(request, "forum/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "forum/register.html")

class NewThread(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'size':50, 'maxlength':50}),label="Title") 
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50, 'maxlength':1000, "id": "content"})) # giving this form the ID of content for the dom queryselector
    photo =  forms.CharField(label="Picture/Screenshot Attachment URL", required=False)                       

@login_required
def new(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewThread(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            photo = form.cleaned_data["photo"]
            user = request.user
            if (title not in Thread.objects.filter(title=title).values_list('title', flat=True)): #ensuring that the title is one of a kind
                Thread.objects.create(madeby=user, title=title, content=content,photo=photo)
                onwhat=Thread.objects.get(title=title)
                who=Informations.objects.get(who=user)

                Post.objects.create(madeby=user, onwhat=onwhat, who=who)
                return HttpResponseRedirect(title)

            else:
                return HttpResponse("Please change the title of your thread, one already exists")


        else:

            return HttpResponse("Error")

    return render(request, "forum/new.html", {
        "form": NewThread()
    })

class NewPost(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50, 'maxlength':750}))

def profile(request, username):


    
    user = User.objects.get(username=username)
    last = User.objects.get(username=user).last_login # last login information
    threads = len(Thread.objects.filter(madeby=user)) #number of threads by the user
    posts1 = len(Post.objects.filter(madeby=user))#number of posts by the user
    posts = posts1 - threads # this line because we decided to create a blank post on each thread creation so the thread is placed at top since the latest post is the parameter of order. So we substract the number of threads to the posts to have the real posts number
    total = (threads*3) + posts # our point system for the stars
    
  
    return render(request, "forum/profile.html", {

        "user": user,
        "informations" : Informations.objects.get(who=user),
        "last": last,
        "threads": threads,
        "posts": posts,
        "total":total

    })

class InformationsForm(forms.Form):
    birth = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    CHOICES= (
    ('',''),
    ('Male','Male'),
    ('Female','Female'),
    )    
    gender = forms.ChoiceField(choices=CHOICES, label="Gender")
    origin = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'maxlength':25}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":50, 'maxlength':254}))
    image = forms.ImageField()




@login_required
def account(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = InformationsForm(request.POST, request.FILES) # request.FILES is necessary for the images upload

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            birth = form.cleaned_data["birth"]
            gender = form.cleaned_data["gender"]
            user = request.user
            bio = form.cleaned_data["bio"]
            image = form.cleaned_data["image"]
            origin = form.cleaned_data["origin"]


            if (len(Informations.objects.filter(who=user)) >0): # this line to ensure that if the user already filled his informations once, the new filling will erase the last one, not creating a new line in the model because this is a one to one relationship
                Informations.objects.filter(who=user).delete()
                Informations.objects.create(who=user, origin=origin, birth=birth, bio=bio, image=image, gender = gender)

            else:
                Informations.objects.create(who=user, origin=origin, birth=birth, bio=bio, image=image, gender = gender)

            return redirect("index")

        else:

            return HttpResponse("Error")

    return render(request, "forum/account.html", {
        "form": InformationsForm()
    })


def thread(request, title):

    thread = Thread.objects.get(title__contains=title)
    madeby = thread.madeby
    madeby2 = User.objects.get(username=madeby)
    posts = Post.objects.filter(onwhat=thread).order_by('post_created')  
    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    if (Informations.objects.get(who=madeby2) != ""):
        madeby3 = Informations.objects.get(who=madeby2)
        return render(request, "forum/thread.html", {
            "thread": thread,
            "madeby": madeby3,
            "posts": posts,
            "page_obj": page_obj
        })
    else:

        return render(request, "forum/thread.html", {
            "thread": thread,
            "posts": posts
        })

def search(request):

    if request.method == "POST":
        title = request.POST.get("q") 
        title1 = title.lower() # forcing query to lowercase

        mylist = list(Thread.objects.all().values_list('title', flat=True)) # retrieving threads list

    

        if title.casefold() not in map(str.casefold, mylist): # this is searching (all lowercase or casefold (case insensitive)) in the threads list
            r = re.compile(f".*{title1}") # reggex for matching
            newlist = list(filter(r.match, map(str.casefold, mylist))) 
            if (not title):  
                return HttpResponse("Enter something to search")

            if (len(newlist) == 0):
                return HttpResponse("No match")

            else:
                return render(request, "forum/search.html", {
                    "newlist": newlist
                })

     
        return redirect("thread", title=title)

    else:

            return HttpResponse("Error")

   




@csrf_exempt
@login_required
def save(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    content = data.get("content", "")
    title = data.get("title", "")
    onwhat = Thread.objects.get(title=title)

    user = request.user
    who=Informations.objects.get(who=user)

    Post.objects.create(content=content, madeby=user, onwhat=onwhat, who=who) #creates a new post
    
    return JsonResponse({"message": "Successfully posted"}, status=201)
    
@csrf_exempt
@login_required
def close(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    title = data.get("title", "")
    Thread.objects.filter(title=title).update(closed=True) # update the element to closed = TRUE

    
    return JsonResponse({"message": "Successfully closed"}, status=201)
    