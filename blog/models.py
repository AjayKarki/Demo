from django.db import models
from .managers import BlogManager

class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    content = models.TextField()
    slug = models.CharField(max_length=100,unique=True)
    cover_image = models.ImageField(upload_to='blog_images',blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    published = models.BooleanField()

    objects  = BlogManager()

    def __str__(self):
        return self.title