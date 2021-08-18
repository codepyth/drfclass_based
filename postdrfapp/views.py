from django.db.models.query_utils import select_related_descend
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

# GET
class GenderList(generics.ListAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

# POST
class RegisterUser(generics.CreateAPIView):
    queryset = CustomUser
    serializer_class = UserSerializer

# GET, POST
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post
    serializer_class = PostSerializer


# GET, DELETE
class PostDelete(generics.DestroyAPIView):
    queryset = Post
    serializer_class = PostSerializer

class GenderAdd(generics.CreateAPIView):
    queryset = Gender
    serializer_class = GenderSerializer

class GenderDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class PostTypeList(generics.ListAPIView):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer

class PostTypeAdd(generics.CreateAPIView):
    queryset = PostType
    serializer_class = PostTypeSerializer

class PostTypeDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostType
    serializer_class = PostTypeSerializer