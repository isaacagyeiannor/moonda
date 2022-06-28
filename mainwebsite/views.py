from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from .forms import BlogsForm, OurServiceForm, SlidersForm, CompanySummaryForm, TestimonialsForm, ContactForm, GalleryForm, CommentForm
from .models import Comment, CompanySummary, Gallery, HomeAboutUs, HomeWhyUs, MainAbout, MainBlog, Sliders, OurServices, Testimonial, Blog, Contact, MainGallery, MainServices

# Create your views here.

#Login
class LoginInterfaceView(LoginView):
    template_name = 'dashboard/login.html'
    
#Logout
class LogoutInterfaceView(LogoutView):
    template_name = 'dashboard/logout.html'

#Register
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'dashboard/register.html'
    success_url = '/login'

#Dashboard

class DashboardHomePage(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard/index.html'
    
#Dashboardservices
class DetailsOurServiceView(DetailView): 
    model = OurServices
    form_class = OurServiceForm
    context_object_name = 'ourserviceform' 
    template_name = 'dashboard/create-service.html'
    
#Dashboard update services
class UpdateOurServiceView(UpdateView): 
    model = OurServices
    form_class = OurServiceForm
    context_object_name = 'ourserviceform' 
    template_name = 'dashboard/create-service.html'
    success_url = '/dashboard/ourservices'
    
#Dashboard create services
class CreateOurServiceView(CreateView): 
    model = OurServices
    # fields = ['serviceTitle', 'serviceNumber', 'title', 'text']
    form_class = OurServiceForm
    context_object_name = 'ourserviceform' 
    template_name = 'dashboard/create-service.html'
    success_url = '/dashboard/ourservices'
      
#Dashboard Services
class ListOurServiceView(ListView): 
    model = OurServices
    form_class = OurServiceForm
    context_object_name = 'services' 
    template_name = "dashboard/our-services.html"
   
   
    
#Dashboard List Company Summary
class ListCompanySummaryView(ListView): 
    model = CompanySummary
    form_class = CompanySummaryForm
    context_object_name = 'companysummarys' 
    template_name = "dashboard/company-summary.html"
 
#Dashboard Create Company Summary
class CreateCompanySummaryView(CreateView): 
    model = CompanySummary
    form_class = CompanySummaryForm
    context_object_name = 'companysummaryform' 
    template_name = 'dashboard/create-company-summary.html'
    success_url = '/dashboard/company-summary'
       
#Dashboard Update Company Summary
class UpdateCompanySummaryView(UpdateView): 
    model = CompanySummary
    form_class = CompanySummaryForm
    context_object_name = 'ourserviceform' 
    template_name = 'dashboard/create-company-summary.html'
    success_url = '/dashboard/company-summary'
    
#Dashboard Company Summary
class DetailsCompanySummaryView(DetailView): 
    model = CompanySummary
    form_class = CompanySummaryForm
    context_object_name = 'ourserviceform' 
    template_name = 'dashboard/create-service.html'
    

#Testimonials CRUD
#Dashboard List Testimonials
class ListTestimonialsView(ListView): 
    model = Testimonial
    form_class = TestimonialsForm
    context_object_name = 'testimonials' 
    template_name = "dashboard/testimonials.html"
 
#Dashboard Create Testimonials
class CreateTestimonialsView(CreateView): 
    model = Testimonial
    form_class = TestimonialsForm
    template_name = 'dashboard/create-testimonial.html'
    success_url = '/dashboard/testimonials'
       
#Dashboard Update Testimonials
class UpdateTestimonialsView(UpdateView): 
    model = Testimonial
    form_class = TestimonialsForm 
    template_name = 'dashboard/create-testimonial.html'
    success_url = '/dashboard/testimonials'
    
#Dashboard Details Testimonials
class DetailsTestimonialsView(DetailView): 
    model = Testimonial
    form_class = TestimonialsForm
    template_name = 'dashboard/create-testimonial.html'

#Dashboard Delete Testimonials
class DeleteTestimonialsView(DeleteView): 
    model = Testimonial
    template_name = 'dashboard/delete-testimonial.html'
    success_url = '/dashboard/testimonials'
    

# Sliders CRUD
#Dashboard List Testimonials
class ListSlidersView(ListView): 
    model = Sliders
    form_class = SlidersForm
    context_object_name = 'sliders' 
    template_name = "dashboard/sliders.html"
 
#Dashboard Create Testimonials
class CreateSlidersView(CreateView): 
    model = Sliders
    form_class = SlidersForm
    template_name = 'dashboard/create-slider.html'
    success_url = '/dashboard/sliders'
       
#Dashboard Update Testimonials
class UpdateSlidersView(UpdateView): 
    model = Sliders
    form_class = SlidersForm 
    template_name = 'dashboard/create-slider.html'
    success_url = '/dashboard/sliders'
    
#Dashboard Details Testimonials
class DetailsSlidersView(DetailView): 
    model = Sliders
    form_class = SlidersForm
    template_name = 'dashboard/create-slider.html'
    
#BLOG CRUD
#Dashboard List Blogs
class ListBlogsView(ListView): 
    model = Blog
    form_class = BlogsForm
    context_object_name = 'blogs' 
    template_name = "dashboard/blogs.html"
 
#Dashboard Create Blogs
class CreateBlogsView(CreateView): 
    model = Blog
    form_class = BlogsForm
    template_name = 'dashboard/create-blog.html'
    success_url = '/dashboard/blogs'
       
#Dashboard Update Blogs
class UpdateBlogsView(UpdateView): 
    model = Blog
    form_class = BlogsForm 
    template_name = 'dashboard/create-blog.html'
    success_url = '/dashboard/blogs'
    
#Dashboard Details Blogs
class DetailsBlogsView(DetailView): 
    model = Blog
    form_class = BlogsForm
    context_object_name = 'blogs' 
    template_name = 'dashboard/view-blog.html'

#Dashboard Delete Blogs
class DeleteBlogsView(DeleteView): 
    model = Blog
    template_name = 'dashboard/delete-blog.html'
    success_url = '/dashboard/blog'


#Gallery CRUD
#Dashboard List Gallery
class ListGalleryView(ListView): 
    model = Gallery
    form_class = GalleryForm
    context_object_name = 'gallerys' 
    template_name = "dashboard/gallery.html"
 
#Dashboard Create Gallery
class CreateGalleryView(CreateView): 
    model = Gallery
    form_class = GalleryForm
    template_name = 'dashboard/add-picture.html'
    success_url = '/dashboard/gallery'
       
#Dashboard Update Gallery
class UpdateGalleryView(UpdateView): 
    model = Gallery
    form_class = GalleryForm 
    template_name = 'dashboard/add-picture.html'
    success_url = '/dashboard/gallery'
    
#Dashboard Details Gallery
class DetailsGalleryView(DetailView): 
    model = Gallery
    form_class = GalleryForm
    context_object_name = 'gallerys' 
    template_name = 'dashboard/gallery.html'

#Dashboard Delete Gallery
class DeleteGalleryView(DeleteView): 
    model = Gallery
    template_name = 'dashboard/delete-picture.html'
    success_url = '/dashboard/gallery'
    

#CONTACT CRUD
#Dashboard List Contact
class ListContactView(ListView): 
    model = Contact
    form_class = ContactForm
    context_object_name = 'contacts' 
    template_name = "dashboard/contact.html"
 
#Dashboard Create Contact
class CreateContactView(CreateView): 
    model = Contact
    form_class = ContactForm
    template_name = 'dashboard/create-contact.html'
    success_url = '/dashboard/contact'
       
#Dashboard Update Contact
class UpdateContactView(UpdateView): 
    model = Contact
    form_class = ContactForm 
    template_name = 'dashboard/create-contact.html'
    success_url = '/dashboard/contact'
    
#Dashboard Details Contact
class DetailsContactView(DetailView): 
    model = Contact
    form_class = ContactForm
    context_object_name = 'contacts' 
    template_name = 'dashboard/contact.html'

#Google Analytics
class GooglePage(TemplateView):
    template_name = 'dashboard/google-analytics.html'
    
    
#Main Website 
class HomePage(ListView):
    model = OurServices
    context_object_name = 'services'
    template_name = 'mainwebsite/index.html'   
    
    queryset = OurServices.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['sliders'] = Sliders.objects.all()
        context['homeaboutuss'] = HomeAboutUs.objects.all()
        context['homewhyuss'] = HomeWhyUs.objects.all()
        context['companysummarys'] = CompanySummary.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['blogs'] = Blog.objects.all()
        context['gallerys'] = Gallery.objects.all()
        # And so on for more models
        return context
    
class AboutPage(ListView):
    model = MainAbout
    context_object_name = 'mainabouts'
    template_name = 'mainwebsite/about.html'   
    
    queryset = MainAbout.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        context['homeaboutuss'] = HomeAboutUs.objects.all()
        context['summarys'] = CompanySummary.objects.all()
        context['homewhyuss'] = HomeWhyUs.objects.all()
        # And so on for more models
        return context

class GalleryPage(ListView):
    model = MainGallery
    context_object_name = 'maingallerys'
    template_name = 'mainwebsite/gallery.html'   
    
    queryset = MainGallery.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GalleryPage, self).get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all()
        # And so on for more models
        return context
    
class ServicesPage(ListView):
    model = MainServices
    context_object_name = 'services'
    template_name = 'mainwebsite/services.html'

class BlogPage(ListView):
    model = MainBlog
    context_object_name = 'posts'
    template_name = 'mainwebsite/blog-posts.html'
    
    queryset = MainBlog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogPage, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        # And so on for more models
        return context
    
class BlogDetailsPage(DetailView):
    template_name = 'mainwebsite/blog-details.html'
    model = Blog
    context_object_name = 'blogs'
    
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogDetailsPage, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm()
        # And so on for more models
        return context
    
# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm

#     def get_success_URL(self):
#         return reverse ('request: detail', kwargs = {'slug':self.object.post.slug})

#     def form_valid(self, form):
#         post = get_object_or_404(Request, slug = self.kwargs ['slug'])
#         Form.instance.post = Request
#         return super().form_valid(form)
    
class ContactPage(ListView):
    template_name = 'mainwebsite/contact.html'
    model = Contact
    context_object_name = 'contacts'
   
class ErrorPage(TemplateView):
    template_name = 'mainwebsite/404.html'

class TryPage(TemplateView):
    template_name = 'mainwebsite/try.html'