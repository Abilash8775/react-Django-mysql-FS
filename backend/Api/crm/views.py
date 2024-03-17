from django.shortcuts import render
from .models import User
from .serializers import Userform
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
class Create(CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = Userform
class Operations(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userform