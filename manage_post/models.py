from pyexpat import model

from django.db import models
from django.contrib.auth import get_user_model
##from ckeditor.fields import RichTextField
User = get_user_model()



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Category', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=40)
    featured = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'


#Articulo

class Article(models.Model):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField(upload_to='Article', blank=True, null=True)
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Article'
    verbose_name_plural = 'Articles'


#Calificaciones
class Rating(models.Model):
    value = models.FloatField()
    description = models.CharField(max_length=255)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username

class Meta:
    verbose_name = 'Rating'
    verbose_name_plural = 'Ratings'
