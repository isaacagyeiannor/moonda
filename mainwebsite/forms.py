from importlib.resources import contents
from django import forms
from .models import Blog, Comment, CompanySummary, Contact, Gallery, OurServices, Sliders, HomeAboutUs, HomeWhyUs, Testimonial

class OurServiceForm(forms.ModelForm):

    class Meta:
        model = OurServices
        fields = ["serviceTitle", "serviceNumber", "image", "title", "text"]
    
class SlidersForm(forms.ModelForm):
    
    class Meta:
        model = Sliders
        fields = ["title","rsnumber", "image", "lighttext", "boldtext"]
        
class HomeAboutUsForm(forms.ModelForm):
    
    class Meta:
        model = HomeAboutUs
        fields = ["image", "headingTag", "heading", "paragraph" , "list1" , "list2", "list3"]

class HomeWhyUsForm(forms.ModelForm):
    
    class Meta:
        model = HomeWhyUs
        fields = ["image1", "image2",  "headingTag", "heading1", "heading2", "heading3", "paragraph"]
    
class CompanySummaryForm(forms.ModelForm):

    class Meta:
        model = CompanySummary
        fields = ["summaryTitle", "totalNumber",  "title", "summaryNumber"]
        
class TestimonialsForm(forms.ModelForm):
    
    class Meta:
        model = Testimonial
        fields = ["testimonialTitle", "name",  "companyname", "image", "testimony"]
        
class BlogsForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ["title", "my_field",  "category", "slug", "image", "author", "tags"]
    
class GalleryForm(forms.ModelForm):
    
    class Meta:
        model = Gallery
        fields = ["title", "image"]
        
class ContactForm(forms.ModelForm):
                                              
    class Meta:
        model = Contact
        fields = ["siteTitle", "image",  "titleTag", "pageTitle" , "contactUs", "locationHeading", "locationText", "locationSubText", "email", "phoneNumber", "mapUrl"]
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')