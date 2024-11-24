from django.shortcuts import render ,  redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project , Tag
from .forms import ProjectForm , ReviewForm
from .utils import searchProjects , paginateProjects
from django.contrib import messages
###moved below to utils
# from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage   

# Create your views here.

def projects(request):
    projects,search_query = searchProjects(request)
    # page = 1
    custom_range , projects =  paginateProjects(request , projects , 3)
    
    context = { "projects" : projects, "search_query": search_query , 'custom_range' : custom_range}
    # return HttpResponse('Here are our Projects!!')
    #PASS IN context dictionary
    return(render(request,'projects/projects.html', context))    #NOTE :  the file path is project/projects.html  -  "templates is not included in the file path"

def project(request, pk):
    # return HttpResponse('SINGLE PROJECTS!!' + ' ' + str(pk))
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        
        projectObj.getVoteCount
        ##Update Project Vote Count
        messages.success(request, "Your review was Submitted!")
        return redirect ('project', pk = projectObj.id)

    tags = projectObj.tags.all()
    return(render(request,'projects/single-project.html',{'project':projectObj,'tags':tags , 'form':form} ))


#if user is not logged in  - send To login page
@login_required(login_url="login")
def createProject (request):
    form = ProjectForm()
    profile = request.user.profile
    if request.method == 'POST':
        newtags = request.POST.get('newtags').split()
        print(request.POST)
        # request.FILES  - relates to enctype="multipart/form-data" on the html template
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False) #create the instance of the save
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)   ### ", created"  and get_or_create - does not ad if already exists
                project.tags.add(tag)  #add the tag to the project
            return redirect('account')   ####use 

    context = {'form': form}
    return render(request,"projects/project_form.html", context)

#if user is not logged in  - send To login page
@login_required(login_url="login")
def updateProject (request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)  ## instance pass in the Existing values to Edit

    if request.method == 'POST':
        print(request.POST)
        newtags = request.POST.get('newtags').split()
        print(newtags)
        form = ProjectForm(request.POST, request.FILES , instance=project)   ## instance pass in project To update
        if form.is_valid():
            form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)   ### ", created"  and get_or_create - does not ad if already exists
                project.tags.add(tag)  #add the tag to the project
            return redirect('account')

    context = {'form': form}
    return render(request,"projects/project_form.html", context)

#if user is not logged in  - send To login page
@login_required(login_url="login")
def deleteProject(request, pk):
    project  = Project.objects.get(id=pk)
    if request.method == 'POST':
        ## When SUBMIT is clicked it it uses the id from the rendered URTL
        ## e58a9c1e-c48b-4259-b3f7-8f1c06437734 in the Project Model
        project.delete()
        return redirect('projects')
    context = {'object':project}
    ## this Renders The URL EXAMPLE -->> http://127.0.0.1:8000/delete-project/e58a9c1e-c48b-4259-b3f7-8f1c06437734/
    return render(request, 'delete_template.html', context )