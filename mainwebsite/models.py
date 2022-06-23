
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager

# Create your models here.

class Sliders(models.Model):
    title = models.CharField(max_length=200)
    rsnumber= models.CharField(max_length=200)
    image = models.ImageField(max_length=20, null= True) 
    lighttext = models.CharField(max_length=200)
    boldtext = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class OurServices(models.Model):
    serviceTitle = models.CharField(max_length=200)
    serviceNumber = models.IntegerField()
    image = models.ImageField(upload_to='images/', max_length=20, null= True) 
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class HomeAboutUs(models.Model):
    aboutUsTitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', max_length=20, null= True) 
    headingTag = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)
    list1 = models.CharField(max_length=200)
    list2 = models.CharField(max_length=200)
    list3 = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
class HomeWhyUs(models.Model):
    whyUsTitle = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='images/', max_length=20, null= True) 
    image2 = models.ImageField(upload_to='images/', max_length=20, null= True) 
    headingTag = models.CharField(max_length=200)
    heading1 = models.CharField(max_length=200)
    heading2 = models.CharField(max_length=200)
    heading3 = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
class CompanySummary(models.Model):
    summaryTitle = models.CharField(max_length=200) 
    summaryNumber = models.CharField(max_length=200)
    totalNumber = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
class Gallery(models.Model):
    galleryTitle = models.CharField(max_length=200) 
    image = models.ImageField(max_length=30, null= True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
    testimonialTitle = models.CharField(max_length=20)
    name = models.CharField(max_length=20) 
    companyname = models.CharField(max_length=20) 
    image = models.ImageField(max_length=30, null= True)
    testimony = models.CharField(max_length=200, default='testimony nkoaa')
    created = models.DateTimeField(auto_now_add=True)
    
class Blog(models.Model):
    title = models.CharField(max_length=50) 
    my_field = tinymce_models.HTMLField()
    image = models.ImageField(max_length=30, null= True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

class Contact(models.Model):
    siteTitle = models.CharField(max_length=50) 
    image = models.ImageField(max_length=30, null= True)
    titleTag = models.CharField(max_length=50) 
    pageTitle = models.CharField(max_length=50) 
    contactUs = tinymce_models.HTMLField()
    locationHeading = models.CharField(max_length=50) 
    locationText = models.CharField(max_length=50) 
    locationSubText = models.CharField(max_length=50) 
    email = models.CharField(max_length=50) 
    phoneNumber = models.CharField(max_length=50) 
    mapUrl = models.CharField(max_length=1000)
    
class MainServices(models.Model):
    siteTitle = models.CharField(max_length=50) 
    serviceTitle = models.CharField(max_length=30, null= True)
    serviceTag = models.CharField(max_length=30, null= True)
    backgroundImage = models.ImageField(max_length=30, null= True)
    titleTag = models.CharField(max_length=50) 
    pageTitle = models.CharField(max_length=50) 
    serviceHeading = models.CharField(max_length=50) 
    headingTag = models.CharField(max_length=50) 
    servicetext = tinymce_models.HTMLField()
    ourExpertiseHeading = models.CharField(max_length=50) 
    expertiseImage = models.ImageField(max_length=30, null= True)
    companyPDF = models.FileField()
    list1 = models.CharField(max_length=50) 
    list2 = models.CharField(max_length=50) 
    list3 = models.CharField(max_length=50) 
    list4 = models.CharField(max_length=50) 
    telImage = models.ImageField(max_length=30, null= True)
    tel = models.CharField(max_length=50) 

class MainAbout(models.Model):
    siteTitle = models.CharField(max_length=50)
    titleTag = models.CharField(max_length=50)  
    image = models.ImageField(max_length=30, null= True)

class MainBlog(models.Model):
    siteTitle = models.CharField(max_length=50)
    titleTag = models.CharField(max_length=50)  
    image = models.ImageField(max_length=30, null= True)
    
class MainGallery(models.Model):
    siteTitle = models.CharField(max_length=50)
    title = models.CharField(max_length=50)  
    image = models.ImageField(max_length=30, null= True)
    
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)
#     content = models.TextField()
    
#     def _str_(self):
#         return self.user.username 