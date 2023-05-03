from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.common import slugify


class User(AbstractUser):
    image = models.ImageField('Image',upload_to='banners/', null=True, blank=True)
    followers = models.IntegerField(null=True, blank=True, default=0)
    following = models.IntegerField(null=True, blank=True, default=0)
    bio = models.CharField('Bio',max_length=300, null=True)
    name = models.CharField('Name',max_length=300, null=True)
    number = models.CharField('Number',max_length=300, null=True)

    slug = models.SlugField(max_length=255, null=True, blank=True)
    
    
    
    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.username)}'
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'