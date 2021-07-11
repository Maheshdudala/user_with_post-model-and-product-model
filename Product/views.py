from django.shortcuts import render
from django.utils import timezone
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from django.shortcuts import redirect


def pd_list(request):
    posts=Product.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    posts=Product.objects.filter(updated_at__lte=timezone.now()).order_by('updated_at')
    return render(request, 'blog1/pd_list.html', {'posts': posts})

def pd1_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    return render(request, 'blog1/pd_detail.html', {'post': post})    
def pd1_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.updated_at = timezone.now()
            post.save()
            return redirect('pd1_detail', pk=post.pk)
    else:
        form = ProductForm()
    return render(request, 'blog1/pd_edit.html', {'form': form})
def pd1_edit(request, pk):
    post = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
            return redirect('pd1_detail', pk=post.pk)
    else:
        form = ProductForm(instance=post)
    return render(request, 'blog1/pd_edit.html', {'form': form})    