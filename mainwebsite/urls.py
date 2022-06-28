from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import CreateOurServiceView, ListCompanySummaryView, ListOurServiceView, UpdateOurServiceView

urlpatterns = [
    # path('', views.serviceslist),
    path('', views.HomePage.as_view(), name='home'),
    path('about-us', views.AboutPage.as_view(), name='about'),
    path('blog', views.BlogPage.as_view(), name='blog'),
    path('blog-details/<int:pk>/', views.BlogDetailsPage.as_view(), name='blog_details'),
    path('<slug:slug>/add_comment/', views.CreateBlogDetailsCommentView.as_view(), name='add_blogcomment'),
    path('services', views.ServicesPage.as_view(), name='services'),
    path('gallery', views.GalleryPage.as_view(), name='gallery'),
    path('contact-us', views.ContactPage.as_view(), name='contact'),
    path('no-page-found', views.ErrorPage.as_view(), name='404'),
    path('try', views.TryPage.as_view(), name='try'),
    
    #Login
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    #Logout
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    #Register
    path('register', views.SignUpView.as_view(), name='register'),
    
    #Dashboard
    path('dashboard/', login_required(views.DashboardHomePage.as_view(), login_url='/login'),name='dashboard'),
    
    
    #Our Services CRUD
    path('dashboard/createservice/', login_required(views.CreateOurServiceView.as_view(), login_url='/login'), name='add_service'),
    path('dashboard/ourservices/<int:pk>/', login_required(views.DetailsOurServiceView.as_view(), login_url='/login'), name='update_service'),
    path('dashboard/ourservices/<int:pk>/edit', login_required(views.UpdateOurServiceView.as_view(), login_url='/login'), name='update_service'),
    path('dashboard/ourservices/', login_required(views.ListOurServiceView.as_view(), login_url='/login'), name='view_services'),
    
    #Our Services CRUD
    path('dashboard/create-company-summary/', login_required(views.CreateCompanySummaryView.as_view(), login_url='/login'), name='add_company_summary'),
    path('dashboard/company-summary/<int:pk>/', login_required(views.DetailsCompanySummaryView.as_view(), login_url='/login'), name='update_company_summary'),
    path('dashboard/company-summary/<int:pk>/edit', login_required(views.UpdateCompanySummaryView.as_view(), login_url='/login'), name='update_company_summary'),
    path('dashboard/company-summary/', login_required(views.ListCompanySummaryView.as_view(), login_url='/login'), name='view_company_summary'),

    #Our Testimonials CRUD
    path('dashboard/create-testimonial/', login_required(views.CreateTestimonialsView.as_view(), login_url='/login'), name='add_testimonial'),
    path('dashboard/testimonials/<int:pk>/', login_required(views.DetailsTestimonialsView.as_view(), login_url='/login'), name='update_testimonial'),
    path('dashboard/testimonials/<int:pk>/edit', login_required(views.UpdateTestimonialsView.as_view(), login_url='/login'), name='update_testimonials'),
    path('dashboard/testimonials/', login_required(views.ListTestimonialsView.as_view(), login_url='/login'), name='view_testimonials'),
    path('dashboard/testimonials/<int:pk>/delete', login_required(views.DeleteTestimonialsView.as_view(), login_url='/login'), name='delete_testimonial'),

    #Our Comments CRUD
    path('dashboard/create-comment/', login_required(views.CreateCommentView.as_view(), login_url='/login'), name='add_comment'),
    path('dashboard/comments/<int:pk>/', login_required(views.DetailsCommentView.as_view(), login_url='/login'), name='view_comment'),
    path('dashboard/comments/<int:pk>/edit', login_required(views.UpdateCommentView.as_view(), login_url='/login'), name='update_comment'),
    path('dashboard/comments/', login_required(views.ListCommentView.as_view(), login_url='/login'), name='view_comments'),
    path('dashboard/comments/<int:pk>/delete', login_required(views.DeleteCommentView.as_view(), login_url='/login'), name='delete_comment'),
    
    #Sliders CRUD
    path('dashboard/create-slider/', login_required(views.CreateSlidersView.as_view(), login_url='/login'), name='add_slider'),
    path('dashboard/sliders/<int:pk>/', login_required(views.DetailsSlidersView.as_view(), login_url='/login'), name='update_slider'),
    path('dashboard/sliders/<int:pk>/edit', login_required(views.UpdateSlidersView.as_view(), login_url='/login'), name='update_sliders'),
    path('dashboard/sliders/', login_required(views.ListSlidersView.as_view(), login_url='/login'), name='view_sliders'),
  
    #BLOG CRUD
    path('dashboard/create-blog/', login_required(views.CreateBlogsView.as_view(), login_url='/login'), name='add_blog'),
    path('dashboard/blogs/<int:pk>/', login_required(views.DetailsBlogsView.as_view(), login_url='/login'), name='view_blog'),
    path('dashboard/blogs/<int:pk>/edit', login_required(views.UpdateBlogsView.as_view(), login_url='/login'), name='update_blog'),
    path('dashboard/blogs/', login_required(views.ListBlogsView.as_view(), login_url='/login'), name='view_blogs'),
    path('dashboard/blogs/<int:pk>/delete', login_required(views.DeleteBlogsView.as_view(), login_url='/login'), name='delete_blog'),
    
    #GALLERY CRUD
    path('dashboard/add-picture/', login_required(views.CreateGalleryView.as_view(), login_url='/login'), name='add_picture'),
    path('dashboard/gallery/<int:pk>/', login_required(views.DetailsGalleryView.as_view(), login_url='/login'), name='view_picture'),
    path('dashboard/gallery/<int:pk>/edit', login_required(views.UpdateGalleryView.as_view(), login_url='/login'), name='update_picture'),
    path('dashboard/gallery/', login_required(views.ListGalleryView.as_view(), login_url='/login'), name='view_pictures'),
    path('dashboard/gallery/<int:pk>/delete', login_required(views.DeleteGalleryView.as_view(), login_url='/login'), name='delete_picture'),
    
    #CONTACT CRUD
    path('dashboard/create-contact/', login_required(views.CreateContactView.as_view(), login_url='/login'), name='add_contact'),
    path('dashboard/contact/<int:pk>/', login_required(views.DetailsContactView.as_view(), login_url='/login'), name='view_contact'),
    path('dashboard/contact/<int:pk>/edit', login_required(views.UpdateContactView.as_view(), login_url='/login'), name='update_contact'),
    path('dashboard/contact/', login_required(views.ListContactView.as_view(), login_url='/login'), name='view_contacts'),
    
    #Google Analytics
    path('dashboard/analytics/', login_required(views.GooglePage.as_view(), login_url='/login'), name='analytics'),
  
]
