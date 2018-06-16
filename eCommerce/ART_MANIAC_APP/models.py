from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category',
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('ART_MANIAC_APP:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, db_index=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('product',)
        indexes = [models.Index(fields=['id', 'slug']),
                   ]

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse('ART_MANIAC_APP:product_detail', args=[self.id, self.slug])





