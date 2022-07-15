from rest_framework import serializers
from .models import User, HelpRequest

class UserSerializer(serializers.HyperlinkedModelSerializer):
    help_requests = serializers.HyperlinkedRelatedField(
        view_name='help_request_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = User
        fields = (
            'id', 
            'first_name', 
            'last_name',
            'user_id',
            'age',
            'nationality',
            'photo_url', 
            'email',
            'password',
            'address',
            'lat',
            'lng',
            'login',
            'request',
            'created_at',
            'my_requests',
            'help_requests'
            )

class HelpRequestSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    class Meta:
        model = HelpRequest
        fields = (
            'id', 
            'description', 
            'created_at',
            'will_come_help',
            'users'
            'completed'
            )