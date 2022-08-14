from audioop import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, CreateView, UpdateView, ListView, FormView, DeleteView

from .models import Post
from .form import PostForm


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
