from django.db.models import Q
from django.views.generic import TemplateView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Award, Blog, Client, Company, Contact, FAQ, FAQQuery, Industry, JobApplication, JobOpening, Project, Service, Testimonial, WhyChooseUs
from .serializers import AwardSerializer, BlogSerializer, ClientSerializer, CompanySerializer, ContactSerializer, FAQQuerySerializer, FAQSerializer, IndustrySerializer, JobApplicationSerializer, JobOpeningSerializer, ProjectSerializer, ServiceSerializer, TestimonialSerializer, WhyChooseUsSerializer


class HomePageView(TemplateView):
    template_name = 'website/home.html'


class PublicViewSet(viewsets.ReadOnlyModelViewSet):
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({'success': True, 'message': 'Data fetched successfully', 'data': response.data})

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({'success': True, 'message': 'Data fetched successfully', 'data': response.data})


class ServiceViewSet(PublicViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    lookup_field = 'slug'

class WhyChooseUsViewSet(PublicViewSet):
    queryset = WhyChooseUs.objects.filter(is_active=True)
    serializer_class = WhyChooseUsSerializer

class IndustryViewSet(PublicViewSet):
    queryset = Industry.objects.filter(is_active=True)
    serializer_class = IndustrySerializer
    lookup_field = 'slug'

class ClientViewSet(PublicViewSet):
    queryset = Client.objects.filter(is_active=True).select_related('industry')
    serializer_class = ClientSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(industry__slug=self.request.query_params['industry']) if self.request.query_params.get('industry') else queryset

class ProjectViewSet(PublicViewSet):
    queryset = Project.objects.filter(is_active=True).select_related('client', 'industry')
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    @action(detail=False, methods=['get'])
    def featured(self, request):
        return self.list_queryset(request, self.get_queryset().filter(is_featured=True))
    def list_queryset(self, request, queryset):
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'message': 'Data fetched successfully', 'data': serializer.data})

class TestimonialViewSet(PublicViewSet):
    queryset = Testimonial.objects.filter(is_active=True).select_related('client')
    serializer_class = TestimonialSerializer

class AwardViewSet(PublicViewSet):
    queryset = Award.objects.filter(is_active=True)
    serializer_class = AwardSerializer

class CompanyViewSet(PublicViewSet):
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer

class CareerViewSet(PublicViewSet):
    queryset = JobOpening.objects.filter(is_active=True)
    serializer_class = JobOpeningSerializer
    lookup_field = 'slug'
    @action(detail=True, methods=['post'], serializer_class=JobApplicationSerializer)
    def apply(self, request, slug=None):
        job = self.get_object()
        serializer = JobApplicationSerializer(data={**request.data, 'job': job.pk}, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Your application has been submitted successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'message': 'Validation failed', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class BlogViewSet(PublicViewSet):
    queryset = Blog.objects.filter(is_published=True)
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')
        if category: queryset = queryset.filter(category__iexact=category)
        if search: queryset = queryset.filter(Q(title__icontains=search) | Q(short_description__icontains=search) | Q(content__icontains=search))
        return queryset
    @action(detail=False, methods=['get'])
    def latest(self, request):
        return self.list_queryset(request, self.get_queryset()[:5])
    def list_queryset(self, request, queryset):
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'message': 'Data fetched successfully', 'data': serializer.data})

class FAQViewSet(PublicViewSet):
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        return queryset.filter(category__iexact=category) if category else queryset

class SubmissionViewSet(viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Your request has been submitted successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'message': 'Validation failed', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ContactViewSet(SubmissionViewSet):
    serializer_class = ContactSerializer

class FAQQueryViewSet(SubmissionViewSet):
    serializer_class = FAQQuerySerializer
