
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Contact
from datetime import datetime

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

def contact(request):
     if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name, email=email,message=message,date=datetime.today())
        contact.save()

     return render(request , 'contact.html')