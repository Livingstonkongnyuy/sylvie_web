from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to='media/blog', default = False)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class Ebook(models.Model):
    title= models.CharField( max_length=50)
    ebook_file = models.FileField(upload_to='media/ebooks')


    def __str__(self):
        return self.title

class Testimonies(models.Model):
    name = models.CharField(max_length = 100, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='media/blog', default = False)
    occupation = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonies'
        verbose_name_plural = 'Testimonies'


class Podcast(models.Model):
    ttitles = models.CharField(max_length=50)
    ccontents = models.TextField()
    audio_file = models.FileField(upload_to='media/podcast')
    picture = models.ImageField(upload_to='media/podcast')
    date_times = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ttitles
    
    class Meta:
        verbose_name = 'Podcast'
        verbose_name_plural = 'Podcast'
    


class Event(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_time = models.DateTimeField()
    status = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='media/event_pictures')
    display_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.date_time >= timezone.now():
            self.status = 'upcoming'
            self.display_date = self.date_time.date()
        else:
            self.status = 'past'
            self.display_date = timezone.now().date()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class Courses(models.Model):
    tit = models.CharField(max_length = 100)
    cont = models.TextField()
    image = models.ImageField(upload_to='media/blog', default = False)
    date_createds = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.tit

    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

class Productbooks(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    # image = models.ImageField(upload_to='media/blog', default = False)
    price = models.CharField(max_length = 20, blank = True, null = True)
    picture = models.ImageField(upload_to = 'media/productBooks')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Productbooks'
        verbose_name_plural = 'Productbooks'


class ProductMerchandise(models.Model):
    ttitle = models.CharField(max_length = 100, null=True, blank=True)
    ddescription = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='media/blog', default = False)
    pprice = models.CharField(max_length = 20, null=True, blank=True)
    ppicture = models.ImageField(upload_to = 'media/productMerchandise')

    def __str__(self):
        return self.ttitle

    class Meta:
        verbose_name = 'ProductMerchandise'
        verbose_name_plural = 'ProductMerchandise'


class Community(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communitys'