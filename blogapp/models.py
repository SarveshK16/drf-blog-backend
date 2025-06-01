from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    facebook_link = models.URLField(max_length=235, blank=True, null=True)
    twitter_link = models.URLField(max_length=235, blank=True, null=True)
    instagram_link = models.URLField(max_length=235, blank=True, null=True)
    youtube_link = models.URLField(max_length=235, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="photos/", blank=True, null=True)

    def __str__(self):
        return self.username
    
class Blog(models.Model):

    CATEGORY = (
        ("Technology", "Technology"),
        ("Economy", "Economy"),
        ("Business", "Business"),
        ("Sports", "Sports"),
        ("Lifestyle", "Lifestyle"),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="blogs", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=CATEGORY, blank=True, null=True)
    featured_image = models.ImageField(upload_to="blog_images/", blank=True, null=True)

    class Meta: 
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1
        while Blog.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{num}"
            num += 1
        self.slug = slug

        if not self.is_draft and self.published_at is None:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)