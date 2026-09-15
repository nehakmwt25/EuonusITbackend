from django.contrib import admin
from .models import Award, Blog, Client, Company, Contact, FAQ, FAQQuery, Industry, JobApplication, JobOpening, Project, Service, Testimonial, WhyChooseUs


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'display_order', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'display_order')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'display_order')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'is_active', 'created_at')
    list_filter = ('is_active', 'industry')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'is_featured', 'is_active', 'created_at')
    list_filter = ('is_active', 'is_featured', 'industry')
    search_fields = ('title', 'short_description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_active', 'created_at')
    list_filter = ('is_active', 'rating')
    search_fields = ('client_name', 'company', 'feedback')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'award_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'organization')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'employment_type', 'is_active', 'application_deadline')
    list_filter = ('is_active', 'employment_type', 'department')
    search_fields = ('title', 'description', 'requirements')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'email', 'status', 'created_at')
    list_filter = ('status', 'job')
    search_fields = ('full_name', 'email', 'mobile')
    readonly_fields = ('created_at',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_published', 'published_at')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'short_description', 'content', 'tags')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'is_active', 'display_order')
    list_filter = ('is_active', 'category')
    search_fields = ('question', 'answer')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

@admin.register(FAQQuery)
class FAQQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'question')
    readonly_fields = ('created_at',)
