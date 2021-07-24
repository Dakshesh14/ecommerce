from datetime import date

from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import Q


class Category(models.Model):
    ct = models.CharField(max_length=255)

    def __str__(self):
        return self.ct


class Item(models.Model):

    class Meta:
        ordering = ("-date_added",)

    status_choice = (
        ('D', 'Draft'),
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

    class get_published_blogs(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(~Q(status='D'))

    objects = get_published_blogs()

    def save(self, *args, **kwargs):
        if self.date_added:
            today = self.date_added
        else:
            today = date.today()

        self.title_slug = slugify(self.title) + '-' + today.strftime("%d-%b-%Y")
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

