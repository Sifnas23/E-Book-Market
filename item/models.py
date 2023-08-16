from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    Name = models.CharField(max_length=100)

    class Meta:
        ordering = ('Name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Name
    
class Item(models.Model):
    Name = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    Book_Name = models.CharField(max_length=50, blank=True, null=True)
    Author = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    Image = models.ImageField(upload_to='book_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('Name',)
        verbose_name_plural = "Item"

    def __str__(self):
        return self.Book_Name
    

