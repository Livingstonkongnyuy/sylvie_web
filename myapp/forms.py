from django import forms
from django.contrib.auth.models import User
from myapp.models import *
from django.core.exceptions import ValidationError


class BlogPost(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = "__all__"

class EbookForm(forms.ModelForm):

    class Meta:
        model= Ebook
        fields = '__all__'

class TestimoniesForm(forms.ModelForm):
    
    class Meta:
        model = Testimonies
        fields = "__all__"


class SignupForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = "__all__"

class PodcastForm(forms.ModelForm):
    
    class Meta:
        model = Podcast
        fields = "__all__"

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"
    


class CoursesForm(forms.ModelForm):

    class Meta:
        model = Courses
        fields = "__all__"
    

class ProductbooksForm(forms.ModelForm):

    class Meta:
        model = Productbooks
        fields = "__all__"
    
class ProductMerchandiseForm(forms.ModelForm):

    class Meta:
        model = ProductMerchandise
        fields = "__all__"

# from django import forms
# from .models import Community
# 
class CommunityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter a community name'
        })

    class Meta:
        model = Community
        fields = "__all__"