from django.utils import timezone
from rest_framework import serializers
from .models import Award, Blog, Client, Company, Contact, FAQ, FAQQuery, Industry, JobApplication, JobOpening, Project, Service, Testimonial, WhyChooseUs


def image_url(request, value):
    return request.build_absolute_uri(value.url) if value else None


class MediaModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        for field in ('image', 'logo', 'featured_image', 'profile_image', 'resume'):
            if field in data and getattr(instance, field, None):
                data[field] = image_url(request, getattr(instance, field)) if request else getattr(instance, field).url
        return data


class ServiceSerializer(MediaModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class WhyChooseUsSerializer(MediaModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = '__all__'

class IndustrySerializer(MediaModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

class ClientSerializer(MediaModelSerializer):
    industry_name = serializers.CharField(source='industry.name', read_only=True)
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('created_at',)

class ProjectSerializer(MediaModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    industry_name = serializers.CharField(source='industry.name', read_only=True)
    class Meta:
        model = Project
        fields = '__all__'

class TestimonialSerializer(MediaModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class AwardSerializer(MediaModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class CompanySerializer(MediaModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ('id', 'job', 'full_name', 'email', 'mobile', 'city', 'resume', 'cover_letter', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate_job(self, job):
        if not job.is_active:
            raise serializers.ValidationError('This job opening is no longer accepting applications.')
        if job.application_deadline and job.application_deadline < timezone.localdate():
            raise serializers.ValidationError('The application deadline has passed.')
        return job

    def validate_resume(self, resume):
        if resume.size > 5 * 1024 * 1024:
            raise serializers.ValidationError('Resume must be 5 MB or smaller.')
        return resume

class BlogSerializer(MediaModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'mobile', 'company', 'subject', 'message', 'created_at')
        read_only_fields = ('id', 'created_at')

class FAQQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQQuery
        fields = ('id', 'name', 'email', 'phone', 'subject', 'service', 'question', 'created_at')
        read_only_fields = ('id', 'created_at')
