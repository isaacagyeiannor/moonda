from django.contrib import admin

from . import models

# Register your models here.
class SlidersAdmin(admin.ModelAdmin):
    list_display = ('title',)

class OurServicesAdmin(admin.ModelAdmin):
    list_display = ('serviceTitle',)

class HomeAboutUsAdmin(admin.ModelAdmin):
    list_display = ('aboutUsTitle',)
    
class HomeWhyUsAdmin(admin.ModelAdmin):
    list_display = ('whyUsTitle',)

class CompanySummaryAdmin(admin.ModelAdmin):
    list_display = ('summaryTitle',)
    
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('galleryTitle',)
    
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('testimonialTitle',)

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('siteTitle',)

class MainServicesAdmin(admin.ModelAdmin):
    list_display = ('siteTitle',)

class MainBlogAdmin(admin.ModelAdmin):
    list_display = ('siteTitle',)

class MainAboutAdmin(admin.ModelAdmin):
    list_display = ('siteTitle',)

class MainGalleryAdmin(admin.ModelAdmin):
    list_display = ('siteTitle',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
admin.site.register(models.Sliders, SlidersAdmin)
admin.site.register(models.OurServices, OurServicesAdmin)
admin.site.register(models.HomeAboutUs, HomeAboutUsAdmin)
admin.site.register(models.HomeWhyUs, HomeWhyUsAdmin)
admin.site.register(models.CompanySummary, CompanySummaryAdmin )
admin.site.register(models.Gallery, GalleryAdmin )
admin.site.register(models.Testimonial, TestimonialAdmin )
admin.site.register(models.Comment, CommentAdmin )

admin.site.register(models.Blog, BlogsAdmin)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.MainServices, MainServicesAdmin)
admin.site.register(models.MainBlog, MainBlogAdmin)
admin.site.register(models.MainAbout, MainAboutAdmin)
admin.site.register(models.MainGallery, MainGalleryAdmin)