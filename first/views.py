from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

def test(request):
       return HttpResponse("Hello, word  ну тип привет")



def test2(request):
       with open(r'D:/hlam/work/first/site.html') as f:
           return HttpResponse(f.read())

def start(request):
           return HttpResponse("ну привет")


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'first/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'first/post_detail.html', {'post': post})

def new_post(request):
    if not request.user.is_authenticated:
        return HttpResponse("Ты че сымый умный?")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'first/post_edit.html', {'form': form})


def post_edit(request):
    if not request.user.is_authenticated:
        return HttpResponse("Ты че сымый умный?")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'first/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'first/post_edit.html', {'form': form})
