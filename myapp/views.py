from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
# from django.contrib import messagesq2e b

# Create your views here.


#user authentification
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Your username does not match')
                return redirect('signup')    

            # elif User.objects.filter(password = password1).exists():
                # return redirect('signup')

            else:
                user = User.objects.create_user(username=username, password=password1,  first_name=first_name, last_name= second_name, email=email)
                if user:
                    user.save()
                    return redirect('/')

        else:
            messages.info(request, 'Your passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')


        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials not satisfied')
            return redirect('signin')
    else:
        return render(request,'signin.html')
    

def signout(request):
    auth.logout(request)
    return redirect('/')
    return render(request, 'signout.html')

def index(request):
    blog = Blog.objects.filter().last()
    testimony = Testimonies.objects.all()
    podcast = Podcast.objects.filter().last()
    course = Courses.objects.filter().last()
    if request.method == "POST":
        subscibsform = CommunityForm(request.POST)

        if subscibsform.is_valid():
            subscibsform.save()  # save the form data to the database
            return redirect('download_pdf')
    else:
        subscibsform = CommunityForm()

    context ={
        'blog' : blog,
        'testimony':testimony,
        'podcast' : podcast,
        'subscibsform' : subscibsform,
        'course' : course

    }
    return render(request,'index.html', context)

def download_pdf(request):
    return render(request, 'download_pdf.html')

def checksubsciption(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
    
    if Community.objects.filter(email = email).exists():
        messages.error(request, 'The email is already is already taken')
        return redirect('/')
    else:
        user = Community(name=name, email=email)
        user.save()
        messages.success(request, 'Thanks for joining the community')
        return redirect('/')
    return render(request,'index.html')

    
def blog(request):
    blog = Blog.objects.all()
    user =User.objects.filter()

    # print(request.user.is_authenticated)
    context = {
        'blog' : blog,
        # 'user' : user,
    }
    return render(request,'blog.html', context)


@login_required(login_url='signin')
def delete_blog(request, pk):
    delete_blog = Blog.objects.filter(id=pk).first()
    delete_blog.delete()
    return redirect('blog')

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')

    else:
        form = BlogPost()

    context={
        'form' : form
    }
    return render(request, 'add_blog.html', context)


@login_required
def update_blog(request, pk):
    blog_form = Blog.objects.get(id=pk)

    if request.method == 'POST':
        form = BlogPost(request.POST or None, request.FILES or None, instance = blog_form)
        if form.is_valid():
            form.save()
            return redirect('blog')
    
    else:
        form = BlogPost(instance = blog_form)

    context={
        'form' : form,
        'blog_form' : blog_form
    }
    return render(request, 'update_blog.html', context)




def blog_detail(request, pk):
    blog = Blog.objects.get(id = pk)
    
    context ={
        'blog' : blog,
    }

    return render(request, 'blog_detail.html', context )



@login_required
def testimonies(request):

    if request.method == 'POST':
        form = TestimoniesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TestimoniesForm()

    context={
        'form' : form
    }

    return render(request,'testimonies.html', context)

def complete_testimony(request, pk):
    testimony = Testimonies.objects.get(id = pk)

    context={
        'testimony' : testimony
    }
    return render(request, 'complete_testimony.html', context)


@login_required 
def add_testimonies(request):
    all_testimonies = Testimonies.objects.all()
    context={
        # 'form' : form,
        'all_testimonies' : all_testimonies
    }
    return render(request,'add_testimonies.html', context)


@login_required
def create_testimony(request):
    if request.method == 'POST':
        form = TestimoniesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_testimonies')
    else:
        form = TestimoniesForm()
    
    context={
        'form' : form
    }
    return render(request, 'create_testimony.html', context)


@login_required
def delete_testimony(request, pk):
    testimony_delete = Testimonies.objects.get(id = pk)
    testimony_delete.delete()
    return redirect('add_testimonies')


@login_required
def update_testimony(request, pk):
    testimony_update = Testimonies.objects.get(id=pk)
    if request.method == 'POST':
        form = TestimoniesForm(request.POST or None, request.FILES or None, instance= testimony_update)
        if form.is_valid():
            form.save()
            return redirect('add_testimonies')
    else:
        form = TestimoniesForm(instance = testimony_update)

    context={
        'form' : form,
        'testimony_update' : testimony_update
    }
 
    return render(request, 'update_testimony.html', context)



def podcast(request):   

    podcast = Podcast.objects.all()

    context={
        'podcast' : podcast
    }
    return render(request, 'podcast.html', context)

@login_required
def create_podcast(request):
    form = PodcastForm()
    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('podcast')
            
    context={
        'form' : form,
    }
    return render(request, 'create_podcast.html', context)

@login_required
def podcast_update(request, pk):
    podcast_update = Podcast.objects.get(id = pk)
    if request.method == 'POST':
        form = PodcastForm(request.POST or None, request.FILES or None, instance = podcast_update)
        if form.is_valid():
            form.save()
            return redirect('podcast')
    
    else:
        form = PodcastForm(instance = podcast_update)
    
    context={
        'form' : form,
        'podcast_update' : podcast_update
    }

    return render(request, 'podcast_update.html', context)


@login_required
def podcast_delete(request, pk):
    delete_podcast = Podcast.objects.get(id = pk)
    delete_podcast.delete()
    return redirect(podcast)
    # return render(request, 'podcast_delete.html')


def podcast(request):
    podcasts = Podcast.objects.all()

    context={
        'podcast' : podcasts
    }
    return render(request,"podcast.html", context)



def podcast_details(request, pk):
    podcast = Podcast.objects.get(id = pk)
    context={
        'podcast' : podcast
    }

    return render(request, 'podcast_details.html', context)


def events(request):
    upcoming = Event.objects.filter(date_time__gte=timezone.now()).order_by('date_time')

    past = Event.objects.filter(date_time__lt=timezone.now()).order_by('-date_time')

    context={
        'upcoming' : upcoming,
        'past' : past
    }
    return render(request,'events.html', context)


@login_required
def event_update(request, pk):
    event_form = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST or None, request.FILES or None, instance = event_form)
        if form.is_valid():
            form.save()
            return redirect('events')

    else:
        form = EventForm(instance = event_form)
    context={
        'form' : form,
        'event_form' : event_form
    }
    return render(request, 'event_update.html', context)


@login_required
def event_delete(request, pk):
    event_delete= Event.objects.get(id = pk)
    event_delete.delete()
    return redirect('events')

def event_detail(request,pk):
    event = Event.objects.filter(id = pk).first()
    # past = Event.objects.filter(date_time__lt=timezone.now()).order_by('-date_time')
    # event = Event.objects.filter(id=pk) 
    context ={
        # 'upcoming': upcoming,
        # 'past':past,
        'event':event
            }
    return render(request, 'event_details.html', context )


def eventForm(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')

    context={
        'form' : form
    }
    return render(request, 'eventForm.html', context)



def courses(request):
    courses = Courses.objects.all()

    context={
        'courses' : courses
    }
    return render(request,'courses.html', context)


@login_required
def create_courses(request):
    if request.method == 'POST':
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CoursesForm()
    context={
        'form' : form
    }
    return render(request, 'create_courses.html', context)


@login_required
def course_delete(request, pk):
    delete_course = Courses.objects.get(id = pk)
    delete_course.delete()
    return redirect('courses')

@login_required
def course_update(request, pk):
    course = Courses.objects.get(id = pk)

    
    if request.method == 'POST':
        course = CoursesForm(request.POST or None, instance= course)
        if course.is_valid():
            course.save()
            return redirect('courses')
    else:    
        course = CoursesForm(instance= course)
    context={
        'course' : course
    }
    return render(request, 'course_update.html', context)



def course_details(request, pk):
    course = Courses.objects.get(id = pk)

    context={
        'course' : course
    }
    return render(request, 'course_details.html', context)


def products(request):

    return render(request,'products.html')

def product_books(request):
    books = Productbooks.objects.all()

    context={
        'books' : books
    }
    return render(request, 'product_books.html', context)

@login_required
def create_productbook(request):
    if request.method == 'POST':
        form=ProductbooksForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_books')
    else:
        form=ProductbooksForm()
    context={
        'form':form
    }
    return render(request,'productbook_create.html',context)


@login_required
def product_book_delete(request, pk):
    book = Productbooks.objects.get(id = pk)

    book.delete()
    return redirect('product_books')

def productbook_details(request,pk):
    book=Productbooks.objects.get(id=pk)
    context={
        'book':book
    }
    return render(request,'productbook_details.html',context)

@login_required
def product_book_update(request, pk):
    book = Productbooks.objects.get(id = pk)
    if request.method == 'POST':
        form = ProductbooksForm(request.POST or None, request.FILES or None, instance= book)
        if form.is_valid():
            form.save()
            return redirect('product_books')
    else:
        form = ProductbooksForm(instance= book)

    context={
        'form' : form
    }
    return render(request, 'product_book_update.html', context)





def product_merchandise(request):
    merchandise = ProductMerchandise.objects.all()

    context={
        'merchandise' : merchandise
    }
    return render(request, 'product_merchandise.html', context)

@login_required
def create_productmerchandise(request):
    if request.method == 'POST':
        form=ProductMerchandiseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_merchandise')
    else:
        form=ProductMerchandiseForm()
    context={
        'form':form
    }
    return render(request,'productmerchandise_create.html',context)


@login_required
def product_merchandise_delete(request, pk):
    merchandise = ProductMerchandise.objects.get(id = pk)

    merchandise.delete()
    return redirect('product_merchandise')


def productmerchandise_details(request,pk):
    merchandise=ProductMerchandise.objects.get(id=pk)
    context={
        'merchandise':merchandise
    }
    return render(request,'productmerchandise_details.html',context)

@login_required
def product_merchandise_update(request, pk):
    merchandise = ProductMerchandise.objects.get(id = pk)
    if request.method == 'POST':
        form = ProductMerchandiseForm(request.POST or None, request.FILES or None, instance= merchandise)
        if form.is_valid():
            form.save()
            return redirect('product_merchandise')
    else:
        form = ProductMerchandiseForm(instance= merchandise)

    context={
        'form' : form
    }
    return render(request, 'product_merchandise_update.html', context)




def about(request):
    return render(request,'about.html')


def youtube(request):
    return render(request,'youtube.html')



def SubscriptionForm(request):
    if request.method == 'POST':
        subscibsform = CommunityForm(request.POST)
        if subscibsform.is_valid():
            subscribtion = form.save(commit =False)
            subscribtion.subscribed = True
            subscribtion.save()
            return redirect('/')
    else:
        subscibsform = CommunityForm()
 
    context={
        'subscibsform' : subscibsform
    }
    return render(request, 'index.html', context)


def ebook(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.subscribed = True
            subscription.save()
            return redirect('/')
# 
    context = {'form': form}
    return render(request, 'ebook.html', context)

@login_required
def subscription(request):
    subsciption = Community.objects.all()

    context={
        'subsciption' : subsciption
    }
    return render(request, 'subscription.html', context)