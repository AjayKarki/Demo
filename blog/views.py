from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404

def home(request):
    return render(request,'blog/home.html')

def blog_list(request):

    if request.method=='GET':
        blog_list = Blog.objects.published()
        context = {
            'blogs':blog_list
        }
        return render(request,'blog/blog-list.html', context=context)

def blog_details(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {
        'blog':blog
    }
    return render(request,'blog/blog-details.html',context=context)