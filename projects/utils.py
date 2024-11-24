from .models import Project,Tag
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage

def paginateProjects(request,projects,results):
    page =   request.GET.get('page')
    # results =  3
    paginator  = Paginator(projects,results)

    try:
        projects  = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects  = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages # get last pages
        projects  = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)   
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    ##create a range of buttons you I want to see At A time
    custom_range = range(leftIndex,rightIndex)
    return custom_range , projects



def searchProjects(request):
    search_query = ''
    if request.GET.get('search_query'): #search_query is the "name =" on the form
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains = search_query)



    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query)|
        Q(description = search_query)|
        Q(owner__name__icontains = search_query)|  ##two sets of double underscores is nested query
        Q(tags__in=tags)
    )

    return projects , search_query