
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def home(request):
    # lost all the posts in the database
    posts = Post.objects.all()[:11]

    data = {
        'posts': posts
    }
    return render(request,'home.html',data)

def post(request , url):
    post = Post.objects.filter(url=url)
    #print(post)
    return render(request, 'posts.html' , {'post': post})