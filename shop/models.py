from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat_name
        

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    