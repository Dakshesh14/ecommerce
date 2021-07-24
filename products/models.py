from django.db import models


class Category(models.Model):
    ct = models.CharField(max_length=255)

    def __str__(self):
        return self.ct


class Item(models.Model):

    status_choice = (
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

    def __str__(self):
        return self.title
