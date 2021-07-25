from datetime import date

from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import Q


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

    objects = models.Manager()
    get_published_items = get_published_items()

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

    def get_featured_product(self):
        return Item.objects.filter(status='F').distinct()

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

    image = ProcessedImageField(upload_to="items", processors=[
                                Resize(550, 550)], format="JPEG")
    image_small = ImageSpecField(source="image", processors=[
                                 Resize(200, 200)], format="JPEG")

    item = models.ForeignKey(
        'Item', related_name='item_img', on_delete=models.CASCADE)
