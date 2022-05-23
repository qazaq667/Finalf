from django.db import models
from django.urls import reverse
from tabnanny import verbose

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    image = models.ImageField(upload_to='main/static/images', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)
    howtocare = models.CharField(
        max_length=300, db_index=True, default='Это монстр, уход не нужен, он тебе поможет')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])


class Comment(models.Model):
    comment = models.TextField(max_length=200)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class User(models.Model):
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.username

    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class CRUD(models.Model):
    animal_name = models.CharField(max_length = 50)
    email = models.EmailField(blank=True)
    comment = models.TextField(default = 'Здесь крч хорошая птица и неплохой бэкенд')
    def __str__(self):
        return self.animal_name


class PetInstance(models.Model):
    ...
    class Meta:
        ...
        permissions = (("can_mark_returned", "Set pet as returned"),)