from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,  IsAdminUser
from.serializers import ProjectSerializer
from projects.models import Project , Review


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'}
    ]

    return Response(routes) 

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects =Project.objects.all()
    serializer = ProjectSerializer(projects, many = True)  ##turns the query to JSON / many is because we have the full query set
    return Response(serializer.data) 


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProject(request,pk):
    print('USER :', request.user)
    project =Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many = False)  ##turns the query to JSON / many = False As only only object
    return Response(serializer.data) 

@api_view(['POST','PUT'])
@permission_classes([IsAuthenticated])
def projectVote (request , pk):
    
    project =  Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data   ###NOTE .data is made available from the api_view decorator  - -- - BOD of DATA RECIEVED in SERIALIZED

    review , created =  Review.objects.get_or_create(
        owner = user,
        project=project,
    )

    review.value = data['value']
    review.save()
    project.getVoteCount   ###becase the @property decorator is used in the Project Model the () is not needed 

    print('DATA : ' , data)

    serializer =  ProjectSerializer(project,many=False)
    return Response(serializer.data)




# def getRoutes(request):

#     routes = [
#         {'GET':'/api/projects'},
#         {'GET':'/api/projects/id'},
#         {'POST':'/api/projects/id/vote'},
#         {'POST':'/api/users/token'},
#         {'POST':'/api/users/token/refresh'}
#     ]
#     return JsonResponse(routes,safe = False)  ## Json response is set to respond with objects -  safe = Fale enables it to work with lists