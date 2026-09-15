from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from .models import Contact, FAQ, JobOpening, Service


class PublicApiTests(APITestCase):
    def test_inactive_services_are_hidden(self):
        Service.objects.create(title='Visible', short_description='Visible', slug='visible', is_active=True)
        Service.objects.create(title='Hidden', short_description='Hidden', slug='hidden', is_active=False)
        response = self.client.get('/api/services/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([item['slug'] for item in response.data['data']], ['visible'])

    def test_contact_requires_valid_email_and_mobile(self):
        response = self.client.post('/api/contact/', {
            'name': 'Test User', 'email': 'invalid', 'mobile': 'x', 'subject': 'Question', 'message': 'A useful message.'
        }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.data['success'])
        self.assertIn('email', response.data['errors'])
        self.assertIn('mobile', response.data['errors'])

    def test_contact_submission_is_saved(self):
        response = self.client.post('/api/contact/', {
            'name': 'Test User', 'email': 'test@example.com', 'mobile': '+919876543210', 'subject': 'Question', 'message': 'A useful message.'
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Contact.objects.filter(email='test@example.com').exists())

    def test_only_published_blogs_and_active_faqs_are_public(self):
        FAQ.objects.create(question='Shown?', answer='Yes', is_active=True)
        FAQ.objects.create(question='Hidden?', answer='No', is_active=False)
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['data']), 1)

    def test_job_application_rejects_large_resume(self):
        job = JobOpening.objects.create(title='Engineer', slug='engineer', location='Jaipur', description='Build things.')
        resume = SimpleUploadedFile('resume.pdf', b'x' * (5 * 1024 * 1024 + 1), content_type='application/pdf')
        response = self.client.post(f'/api/careers/{job.slug}/apply/', {
            'full_name': 'Test User', 'email': 'test@example.com', 'mobile': '+919876543210', 'resume': resume,
        }, format='multipart')
        self.assertEqual(response.status_code, 400)
        self.assertIn('resume', response.data['errors'])
