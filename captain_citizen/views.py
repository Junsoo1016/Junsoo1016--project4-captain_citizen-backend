from rest_framework import generics
from .serializers import UserSerializer, HelpRequestSerializer
from .models import User, HelpRequest

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HelpRequestList(generics.ListCreateAPIView):
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer

class HelpRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer
