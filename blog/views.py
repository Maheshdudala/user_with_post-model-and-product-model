from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def home(request):
    return render (request,'home.html')

def post_list(request):
    posts=Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    posts=Post.objects.filter(updated_at__lte=timezone.now()).order_by('updated_at')
    
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.updated_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updated_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .models import User,UserForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home (request):
    return render(request,'home.html')
def add_user(request):
    if request.method=="POST":
        f=UserForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserForm
        d={'form':f}
        return render(request,'form.html',d)
def login_view(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['userid']=user.id
            login(request,user)
            return render(request,'user.html')
        else:
            return HttpResponse("Invalid Username and PAssword")
    else:
        return render(request,'login.html')
def logout_view(request):
    logout(request)                         
    return redirect('/')        