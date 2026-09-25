from django import forms
from django.contrib import admin

from .models import Award, Blog, Client, Company, Contact, FAQQuery, Industry, JobApplication, JobOpening, Opening, Project, Service, Testimonial, WhyChooseUs


class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'short_description', 'description')
        labels = {
            'title': 'Heading',
            'short_description': 'Short description',
            'description': 'Related points',
        }


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    fields = ('title', 'short_description', 'description')
    list_display = ('title',)
    search_fields = ('title',)


class WhyChooseUsAdminForm(forms.ModelForm):
    class Meta:
        model = WhyChooseUs
        fields = ('image', 'title', 'description')
        labels = {
            'title': 'Heading',
            'description': 'Short description',
        }


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    form = WhyChooseUsAdminForm
    fields = ('image', 'title', 'description')
    list_display = ('title',)
    search_fields = ('title',)


class IndustryAdminForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ('image', 'name')
        labels = {'image': 'Background image', 'name': 'Industry name'}


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    form = IndustryAdminForm
    fields = ('image', 'name')
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'is_active', 'created_at')
    list_filter = ('is_active', 'industry')
    search_fields = ('name',)


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'short_description', 'featured_image')
        labels = {
            'title': 'Heading',
            'short_description': 'Short description',
            'featured_image': 'Background image',
        }


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    fields = ('title', 'short_description', 'featured_image')
    list_display = ('title',)
    search_fields = ('title',)


class TestimonialAdminForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('feedback', 'client_name', 'designation')
        labels = {
            'feedback': 'Brief comment',
            'client_name': 'User name',
            'designation': 'User position',
        }


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialAdminForm
    fields = ('feedback', 'client_name', 'designation')
    list_display = ('client_name',)
    search_fields = ('client_name',)


class AwardAdminForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ('image', 'title')
        labels = {'image': 'Logo', 'title': 'Award name'}


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    form = AwardAdminForm
    fields = ('image', 'title')
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = ('logo', 'name', 'company_type')
    list_display = ('logo', 'name', 'company_type')
    search_fields = ('name', 'company_type')


class JobOpeningAdminForm(forms.ModelForm):
    class Meta:
        model = JobOpening
        fields = ('employment_type', 'experience_required', 'title', 'location', 'description')
        labels = {
            'employment_type': 'Type',
            'experience_required': 'Duration',
            'title': 'Position name',
            'description': 'Short description',
        }


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    form = JobOpeningAdminForm
    fields = ('employment_type', 'experience_required', 'title', 'location', 'description')
    list_display = ('title', 'location')
    search_fields = ('title', 'location')


@admin.register(Opening)
class OpeningAdmin(admin.ModelAdmin):
    fields = ('type_of_job', 'background_image', 'heading', 'address', 'short_description')
    list_display = ('heading', 'type_of_job', 'address')
    search_fields = ('heading', 'type_of_job', 'address')


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
