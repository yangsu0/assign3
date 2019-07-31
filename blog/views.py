from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from blog.models import Blog
from .forms import BlogPost

# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if 'search' in request.GET:
        query = request.GET['search']  
        blogs = Blog.objects.all().filter(title__contains=query)
        result = blogs    
        return render(request, 'home.html', {'searched_blogs' : result, 'query': query })    
    else:
        result = None
        return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

    


def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.title = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog')

def portfolio(request):
    return render(request,'portfolio.html')

def blogpost(request):
    if request.method=='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('/blog')
    else:
        form = BlogPost()
        return render(request, 'new.html',{'form':form})