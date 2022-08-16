from audioop import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, CreateView, UpdateView, ListView, FormView, DeleteView
from .serializer import AuthorSerializer, PublishSerializer, PostSerializer

from .models import Post, Author, Publish
from .form import PostForm
from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class PostDetails(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = "blog/post_detail"

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

        return render(request, 'blog/post_detail.html', {'post': post})


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', ]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return render(request, 'blog/post_detail.html', {'post': post})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_view.html'
    success_url = reverse_lazy('post_list')


# start Django rest-framework

# without Rest Api no models
def no_rest_no_model(request):
    authers = [
        {
            'id': 1,
            'name': 'Duha',
            'address': 'As salt'

        },
        {
            'id': 2,
            'name': 'Ahmad',
            'address': 'Amman'
        }
    ]
    return JsonResponse(authers, safe=False)


# 2 no rest  from model

def no_model_from_model(request):
    data = Author.objects.all()
    response = {
        'authors': list(data.values('name', 'address'))
    }
    return JsonResponse(response)


# list == GET
# creat == POST
# ----------------- #
# pk query == GET
# Update == PUT
# Delete == DELETE

# FBV
# GET POST
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def FBV_List(request):
    # GET
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def FBV_pk(request, pk):
    author = Author.objects.get(pk=pk)
    # GET
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class based view POST and Get
@permission_classes((permissions.AllowAny,))
class CBV_List(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


# Class based view PUT  and GET   and DELETE
@permission_classes((permissions.AllowAny,))
class CBV_pk(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self,request, pk):
        author = self.get_object(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_object(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)