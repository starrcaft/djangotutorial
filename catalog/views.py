from django.shortcuts import render
# rest frame work
from rest_framework import viewsets
from .serializers import PostSerializer

from .models import Post
from .serializers import PostSerializer
# Create your views here.


def post_list(request):
    posts= Post.objects
    return render(request, 'catalog/post_list.html', {})

class DetailPost(viewsets.ModelViewSet) :
    qeuryset = Post.objects.all()
    serializer_class = PostSerializer
