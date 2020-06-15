from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers, models, permissions



class HelloApiView(APIView):
    """ Test API view """
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ REturn a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most controll over your app logic',
            'Is mapped manually to urls'
        ]
        
        return Response({'message': 'hello world', 'an_apiview': an_apiview})
    
    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk=None):
        """ updating an object """
        return Response({'method':'PUT'})
    
    
    def patch(self, request, pk=None):
        """ partialy updating an object """
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method':'DELETE'})



class HelloApiViewset(viewsets.ViewSet):
    """ Test API viewset """
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """ return a hello message """
        
        a_viewset = [
            'Uses actions(list, create, retrive, upadte, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionalities with less code',
        ]
        
        
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    
    
    
    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data=request.data)
        
        if  serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
            
    def retrive(self, request, pk=None):
        """ handle getting an object by ID """
        return Response({'HTTP_method':'GET'})
    
    def update(self, request, pk=None):
        """ handle updating an object by ID """
        return Response({'HTTP_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """ handle partialy updating an object by ID """
        return Response({'HTTP_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """ handle deleting an object by ID """
        return Response({'HTTP_method':'DELETE'})
    
    
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating User profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    
    
    
    
    
class UserLoginApiView(ObtainAuthToken):
    """ Handle create user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES