from django.shortcuts import render,redirect
from .models import Article,Comment,Contact,Blog,Blogform
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    articels = Article.objects.all()
    comment = Comment.objects.all()
    blogs = Blog.objects.all()
    contacts = Contact.objects.all()
    enquiry = Blogform.objects.all()
    context = {'articels': articels, 'comment':  comment,'blogs': blogs,'contacts': contacts,'enquiry':enquiry}

    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        comment_section = request.POST.get('comment_section','')
        comments= Blogform(name=name,email=email,comment_section=comment_section)
        comments.save()
    return render(request,'index.html',context)
def blog(request):
    comment = Comment.objects.all()
    blogs = Blog.objects.all()
    enquiry = Blogform.objects.all()
    context = {'comment':  comment, 'blogs': blogs,'enquiry':enquiry}

    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        comment_section = request.POST.get('comment_section','')
        comments= Blogform(name=name,email=email,comment_section=comment_section)
        comments.save()
    return render(request,'blog.html',context)
def about(request):
    articels = Article.objects.all()
    context = {'articels': articels}
    return render(request,'about.html',context)
def contact(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}

    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        contact= Contact(name=name,email=email,subject=subject,message=message)
        contact.save()

    return render(request,'contact.html',context)
def marketing(request):
    return render(request,'marketing.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('about')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')

    return render(request,'login.html')
   
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('about')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return redirect('index')
   