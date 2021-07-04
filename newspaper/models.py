from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=160)
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    important_part = models.TextField(max_length=500)
    first_part = models.TextField(max_length=5500)
    last_part = models.TextField(max_length=5500)

    def __str__(self):
        return self.title
    