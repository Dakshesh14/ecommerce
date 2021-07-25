from datetime import date

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# django image kit model
# https://pypi.org/project/django-imagekit/
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import Resize


class Category(models.Model):
    ct = models.CharField(max_length=255)

    def __str__(self):
        return self.ct


class Item(models.Model):

    class Meta:
        ordering = ("-date_added",)

    status_choice = (
        ('D', 'Draft'),
        ('F', 'Featured'),
        ('IS', 'In Stock'),
        ('NA', 'Not Available'),
        ('OS', 'Out Of Stock'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)

    price = models.IntegerField()

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=2, choices=status_choice)
    date_added = models.DateField(auto_now=True)

    title_slug = models.CharField(max_length=350)

    class get_published_items(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(~Q(status='D'))

    class get_featured_product(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Q(status='F'))

    objects = models.Manager()
    get_published_items = get_published_items()
    get_featured_product = get_featured_product()

    def save(self, *args, **kwargs):
        if self.date_added:
            today = self.date_added
        else:
            today = date.today()

        self.title_slug = slugify(self.title) + '-' + today.strftime("%d-%b-%Y")
        super(Item, self).save(*args, **kwargs)

    def get_first_thumbnail_img(self):
        img = ItemImage.objects.filter(item=self)
        if img.exists():
            return img.first().image_small
        else:
            return None

    def get_product_image(self):
        print("get_product_image called")
        img = ItemImage.objects.filter(item=self).distinct()
        return img

    def __str__(self):
        return self.title


class ItemImage(models.Model):
    class Meta:
        verbose_name = 'Item image'
        verbose_name_plural = 'Item images'

    image = ProcessedImageField(upload_to="items", processors=[Resize(550, 550)], format="JPEG")
    image_small = ImageSpecField(source="image", processors=[Resize(200, 200)], format="JPEG")

    item = models.ForeignKey('Item', related_name='item_img', on_delete=models.CASCADE)


class CartItem(models.Model):
    item = models.ForeignKey('Item',related_name='cart_item',on_delete=models.CASCADE)
    cart_obj = models.ForeignKey('Cart',related_name="cart_obj",on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item} - {self.quantity}"


class Cart(models.Model):
    user = models.ForeignKey(User, related_name="user_cart_item", on_delete=models.CASCADE)
    total_price = models.IntegerField()

    created = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        total_price = 0
        qs = self.cart_obj.all()
        for item in qs:
            total_price += item.item.price
        self.total_price = total_price
        super(Cart, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}"
