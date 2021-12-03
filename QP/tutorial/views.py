from django.shortcuts import render
#from django.http.response import JsonResponse
from rest_framework.response import Response
#from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from tutorial.models import Tutorials
from tutorial.serializers import TutorialsSerializer
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from rest_framework.decorators import api_view


class TutorialViewSet(viewsets.ViewSet):
    serializer_class = TutorialsSerializer
    #tutorial_param_config = openapi.Parameter(
        #'id', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    #@swagger_auto_schema(manual_parameters=[tutorial_param_config])
    def list(self,request):
        queryset=Tutorials.objects.all()
        serializer=TutorialsSerializer(queryset,many=True)
        return Response (serializer.data)

    #@swagger_auto_schema(manual_parameters=[tutorial_param_config])
    @action(detail=False)
    def published(self,request):
     # GET all published tutorials 
          queryset = Tutorials.objects.filter(published=True)
          serializer = TutorialsSerializer(queryset, many=True)
          return Response(serializer.data)

    def retrieve(self, request,pk=None):
        id=pk
        if id is not None:
            queryset = Tutorials.objects.get(id=id)
            serializer=TutorialsSerializer(queryset)
            return Response(serializer.data)
        return Response({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    #@swagger_auto_schema(manual_parameters=[tutorial_param_config])
    def create(self,request):
        serializer=TutorialsSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
      id=pk
      queryset=Tutorials.objects.get(pk=id)
      serializer=TutorialsSerializer(queryset,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Data Updated'})
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
      id=pk
      queryset=Tutorials.objects.get(pk=id)
      queryset.delete()
      return Response({'msg':'Data Deleted'})
    
    @action(detail=False,methods=['delete'])
    def delete_all(self,request):
     count = Tutorials.objects.all().delete()
     return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
  
     #

# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     # GET list of tutorials, POST a new tutorial, DELETE all tutorials
#  if request.method == 'GET':
#         tutorials = Tutorials.objects.all()
        
#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
#         tutorials_serializer = TutorialsSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#  elif request.method == 'POST':
#         #tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialsSerializer(data=request.data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#  elif request.method == 'DELETE':
#         count = Tutorials.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


 
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     # find tutorial by pk (id)
#     try: 
#         tutorial = Tutorials.objects.get(pk=pk) 
#     except Tutorials.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
#     # GET / PUT / DELETE tutorial
#     if request.method == 'GET': 
#         tutorial_serializer = TutorialsSerializer(tutorial) 
#         return JsonResponse(tutorial_serializer.data) 
#     elif request.method == 'PUT': 
#         #tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = TutorialsSerializer(tutorial, data=request.data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def tutorial_list_published(request):
#      # GET all published tutorials 
#      tutorials = Tutorials.objects.filter(published=True)
        
#      if request.method == 'GET': 
#         tutorials_serializer = TutorialsSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)