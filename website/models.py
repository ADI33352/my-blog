from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to ='images', default ="")
    timestames = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.title


    

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to ='images', default ="")
    timestames = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.title


    
class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    comments = models.TextField()
    timestames = models.DateTimeField(auto_now_add=True,null=True)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to ='images', default ="")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message  = models.TextField()

    def __str__(self):
        return self.name



class Blogform(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=100)
    comment_section = models.TextField()
    def __str__(self):
        return self.name