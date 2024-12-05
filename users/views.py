from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .models import Profile , Skill
from django.contrib.auth.models import User 
from .forms import CustomUserCreationForm ,  ProfileForm ,  SkillForm ,  MessageForm
from django.db.models import Q
from .utils import searchProfiles , paginateProfiles
import os
# Create your views here.


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)  ##Saving and holing an instance of it 
            user.username = user.username.lower() #   then converts the instance of the user to lower case
            user.save()  ##then performs the save

            messages.success(request, "User Account Created!")

            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.error(request , "An Error has occured")


    context = {'page':page , 'form':form}
    return render(request, 'users/login-register.html' , context)

def loginPage(request):
    page = 'login'
    ##Dont let logged in user be on the log in page  -  can use decorators instead
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username  = request.POST['username'].lower()
        password  = request.POST['password']

        try:
            user = User.objects.get(username = username)
            print(user)
        except:
            messages.error(request,"Username does not Exist")
        
        user = authenticate(request,username = username , password = password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request,"Username or Password is Incorrect")


    return render(request, 'users/login-register.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request,"User was logged out")
    return redirect('login')


def profiles(request):
    print(os.getcwd())
    search_query = ''
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 3)
    # if request.GET.get('search_query'):
    #     search_query = request.GET.get('search_query')
    #     print('PROFILE SEARCH : ' , search_query)

    
    context = {'profiles':profiles , 'search_query':search_query, 'custom_range': custom_range}
    print ('END OF VIEW')
    return render(request, 'users/profiles.html', context)

def userProfile(request,pk):
    profile  = Profile.objects.get(id=pk)
    ### skill (is the model) (_set) is an attribut -  to get data from the model
    topSkills  = profile.skill_set.exclude(description__exact = "") # Exclude Empty description
    otherSkills  = profile.skill_set.filter(description = "")

    context = {'profile' : profile , 'topSkills' : topSkills , 'otherSkills' : otherSkills}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills  = profile.skill_set.all() # get all skills  -  different to what userProfile (seperated to stills with and without descriptions)
    projects = profile.project_set.all()

    context = {'profile' : profile , 'skills' : skills , 'projects' : projects}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount (request):
    profile = request.user.profile
    print(profile)
    form  = ProfileForm(instance=profile)

    if request.method  == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance= profile)
        if form.is_valid():
            form.save()

            return redirect ('account')
    
    # form = ProfileForm()
    context = {'form':form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def createSkill (request):
    profile = request.user.profile
    form = SkillForm()

    if request.method  == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill was Created!")
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def updateSkill (request , pk): #pk is the primary key of The skill to Modify
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    form = SkillForm(instance=skill)
    
    if request.method  == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            # skill = form.save(commit=False)
            # skill.owner = profile
            form.save()
            messages.success(request, "Skill was updated!")
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/skill_form.html', context)



@login_required(login_url='login')
def deleteSkill (request , pk): #pk is the primary key of The skill to Modify

    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method  == 'POST':
        skill.delete()
        messages.success(request, "Skill was deleted!")
        return redirect('account')

    context = {'object':skill}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def inbox (request):
    profile = request.user.profile
    messageRequests = profile.messages.all()  ## "messages" in this case is The related name from the Model -   no need for _set
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests':messageRequests,'unreadCount':unreadCount}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def viewMessage (request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message, 'profile':profile}

    ##{{message.name}}
    return render(request, 'users/message.html', context)

def createMessage (request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm

    try:
        sender = request.user.profile
    except:
        sender = None
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request,"Your message was sent successfully!")
            return redirect('user-profile', pk= recipient.id)
    
    context = {'recipient':recipient , 'form':form}

    ##{{message.name}}
    return render(request, 'users/message-form.html', context)