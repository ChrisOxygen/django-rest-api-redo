from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """ Serializes a name feild for testing out APIView """
    name = serializers.CharField(max_length=10)
    


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
        
        
    def create(self, validated_data):
        """  Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            
        )
        
        return user