from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.utils.datetime_safe import datetime

# Create your models here.

SUBCATEGORY_CHOICES = (
    ('none', 'NONE'),
    ('bag', 'BAG'),
    ('shoes', 'SHOES'),
    ('watches', 'WATCHES'),
)

SIZE_CHOICES = (
    ('', '-- choose a option --'),
    ('Size S', 'Size S'),
    ('Size M', 'Size M'),
    ('Size L', 'Size L'),
    ('Size XL', 'Size XL'),
)

COLOR_CHOICES = (
    ('', '-- choose a option --'),
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Black', 'Black'),
    ('White', 'White'),
    ('Grey', 'Grey'),
)


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=20, choices=SUBCATEGORY_CHOICES, default='none')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    # size = models.CharField(max_length=20, choices=SIZE_CHOICES, default='none')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg', upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='current_user_cart', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)  # add this new attribute to cart

    count = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    entry_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    # total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    # price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Item in Cart'
        verbose_name_plural = 'Items In Cart'

    def __str__(self):
        # return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)
        return "User: \"{}\" has {} '{}' item in their cart".format(self.user, self.count, self.product)

# class Entry(models.Model):
#     product = models.ForeignKey(Product, null=True, on_delete='CASCADE')
#     cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
#     quantity = models.PositiveIntegerField()
#
#     class Meta:
#         verbose_name = 'entry'
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#         return "This entry contains {} {}(s).".format(self.quantity, self.product.name)


# @receiver(post_save, sender=Entry)
# def add_entry_to_cart(sender, instance, **kwargs):
#         line_cost = instance.quantity * instance.product.price
#         instance.cart.total += line_cost
#         instance.cart.count += instance.quantity
#         instance.cart.updated = datetime.now()
#
#         instance.cart.save()


# @receiver(post_delete, sender=Entry)
# def delete_entry_and_update_cart(sender, instance, deleted, **kwargs):
#     # instance.delete()
#     # line_cost = instance.quantity * instance.product.price
#     # instance.cart.total -= line_cost
#     # instance.cart.count -= instance.quantity
#     # instance.cart.updated = datetime.now()
#     if deleted:
#         Entry.objects.filter(id=instance.id).delete()
#

# @receiver(post_save, sender=Entry)
# def update_cart(sender, instance, **kwargs):
#     # line_cost = instance.quantity * instance.product.price
#
#     total_update_to = instance.cart.total
#     count_update_to = instance.cart.count
#     instance.cart.updated = datetime.now()
#
#     Cart.objects.filter(user_id=instance.cart.user_id).update(count=count_update_to, total=total_update_to)


# @receiver(post_save, sender=get_user_model())
# def create_user_cart(sender, instance, created, **kwargs):
#     if created:
#         Cart.objects.create(user=instance)
