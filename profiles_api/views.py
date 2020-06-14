from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API view """
    
    def get(self, request, format=None):
        """ REturn a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most controll over your app logic',
            'Is mapped manually to urls'
        ]
        
        return Response({'message': 'hello world', 'an_apiview': an_apiview})
