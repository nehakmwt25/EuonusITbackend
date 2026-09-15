from rest_framework.routers import DefaultRouter
from .views import AwardViewSet, BlogViewSet, CareerViewSet, ClientViewSet, CompanyViewSet, ContactViewSet, FAQQueryViewSet, FAQViewSet, IndustryViewSet, ProjectViewSet, ServiceViewSet, TestimonialViewSet, WhyChooseUsViewSet

router = DefaultRouter()
router.register('services', ServiceViewSet, basename='service')
router.register('it-services', ServiceViewSet, basename='it-service')
router.register('why-choose-us', WhyChooseUsViewSet, basename='why-choose-us')
router.register('industries', IndustryViewSet, basename='industry')
router.register('clients', ClientViewSet, basename='client')
router.register('projects', ProjectViewSet, basename='project')
router.register('testimonials', TestimonialViewSet, basename='testimonial')
router.register('awards', AwardViewSet, basename='award')
router.register('companies', CompanyViewSet, basename='company')
router.register('careers', CareerViewSet, basename='career')
router.register('blogs', BlogViewSet, basename='blog')
router.register('faqs', FAQViewSet, basename='faq')
router.register('contact', ContactViewSet, basename='contact')
router.register('faq-query', FAQQueryViewSet, basename='faq-query')

urlpatterns = router.urls
