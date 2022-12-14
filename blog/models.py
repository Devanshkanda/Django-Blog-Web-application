from distutils.command.upload import upload
from operator import truediv
from turtle import title
from django.db import models
from django.utils.html import format_html

# Create your models here.
# catagory models

class Catagory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='catagory/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:100px; height:100px" />'.format(self.image))

    def __str__(self):
        return self.title


# post mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title
#contact modals

class Contact(models.Model):
    name=models.CharField(max_length=111)
    email=models.EmailField(max_length=125)
    message=models.CharField(max_length=200)
    date=models.DateField()
    def __str__(self):
        return self.name
