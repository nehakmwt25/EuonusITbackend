from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.utils.text import slugify

phone_validator = RegexValidator(r'^\+?[0-9\s().-]{7,20}$', 'Enter a valid mobile number.')


class OrderedActiveModel(models.Model):
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['display_order', '-created_at']


class Service(OrderedActiveModel):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    short_description = models.TextField()
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title


class ITService(Service):
    class Meta:
        proxy = True


class WhyChooseUs(OrderedActiveModel):
    title = models.CharField(max_length=160)
    description = models.TextField()
    icon = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to='why-choose-us/', blank=True, null=True)

    def __str__(self): return self.title


class Industry(OrderedActiveModel):
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='industries/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self): return self.name


class Client(models.Model):
    name = models.CharField(max_length=160)
    logo = models.ImageField(upload_to='clients/', blank=True, null=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name


class Project(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField()
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    technologies = models.CharField(max_length=500, blank=True)
    featured_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: ordering = ['-is_featured', '-created_at']

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title


class Testimonial(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='testimonials')
    client_name = models.CharField(max_length=160)
    designation = models.CharField(max_length=160, blank=True)
    company = models.CharField(max_length=160, blank=True)
    feedback = models.TextField()
    profile_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: ordering = ['-created_at']

    def __str__(self): return self.client_name


class Award(models.Model):
    title = models.CharField(max_length=180)
    organization = models.CharField(max_length=180, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='awards/', blank=True, null=True)
    award_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self): return self.title


class Company(models.Model):
    name = models.CharField(max_length=160)
    logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    company_type = models.CharField('Type of the company', max_length=120, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self): return self.name


class JobOpening(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    department = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=160)
    employment_type = models.CharField(max_length=80, default='Full-time')
    experience_required = models.CharField(max_length=160, blank=True)
    description = models.TextField()
    responsibilities = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    salary_range = models.CharField(max_length=120, blank=True)
    application_deadline = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'JobOpenings'

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title


class Opening(models.Model):
    type_of_job = models.CharField('Type of job', max_length=120)
    background_image = models.ImageField(upload_to='openings/', blank=True, null=True)
    heading = models.CharField(max_length=180)
    address = models.CharField(max_length=255)
    short_description = models.TextField()

    class Meta:
        verbose_name = 'Opening'
        verbose_name_plural = 'Openings'

    def __str__(self): return self.heading


class JobApplication(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('reviewed', 'Reviewed'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected'), ('selected', 'Selected')]
    job = models.ForeignKey(JobOpening, on_delete=models.PROTECT, related_name='applications')
    full_name = models.CharField(max_length=160)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, validators=[phone_validator])
    city = models.CharField(max_length=120, blank=True)
    resume = models.FileField(upload_to='resumes/', validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: ordering = ['-created_at']


class Blog(models.Model):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    author = models.CharField(max_length=160, default='Euonus Editorial')
    short_description = models.TextField()
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    category = models.CharField(max_length=120, blank=True)
    tags = models.CharField(max_length=500, blank=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: ordering = ['-published_at', '-created_at']

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=120, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: ordering = ['display_order', '-created_at']

    def __str__(self): return self.question


class Contact(models.Model):
    STATUS_CHOICES = [('new', 'New'), ('contacted', 'Contacted'), ('closed', 'Closed')]
    name = models.CharField(max_length=160)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, validators=[phone_validator])
    company = models.CharField(max_length=160, blank=True)
    subject = models.CharField(max_length=220)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: ordering = ['-created_at']


class FAQQuery(models.Model):
    STATUS_CHOICES = [('new', 'New'), ('answered', 'Answered'), ('closed', 'Closed')]
    name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_validator], blank=True)
    subject = models.CharField(max_length=220, blank=True)
    service = models.CharField(max_length=160, blank=True)
    question = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: ordering = ['-created_at']
