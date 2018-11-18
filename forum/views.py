from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comments
from .forms import Add_Post,Add_Comment
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        form = Add_Post(request.POST or None)
        if form.is_valid():
            content = request.POST.get('content')
            title = request.POST.get('title')
            form = Post.objects.create(title=title, author=request.user, content=content)
            form.save()
            messages.success(request, f'Posted')
            return redirect('user-home')    
    else:
        form=Add_Post()
    posts = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts,
        'form' : form,
    }
    return render(request,'forum/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comments.objects.filter(comment_to=post).order_by('-date_posted')
    paginator = Paginator(comments,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if request.method == 'POST':
        form = Add_Comment(request.POST or None)
        if form.is_valid():
            content = request.POST.get('content')
            form = Comments.objects.create(comment_to=post, author=request.user, content=content)
            form.save()
            messages.success(request, f'Comment Posted')
            return redirect('post-detail', pk=pk)    
    else:
        form=Add_Comment()
    context = {
        'post' : post,
        'comments' : comments,
        'form' : form
    }
    return render(request,'forum/post_detail.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'forum/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False