from datetime import date

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db.models import Q


# django image kit model
# https://pypi.org/project/django-imagekit/
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import Resize


# django ckeditor
# https://pypi.org/project/django-ckeditor/
from ckeditor_uploader.fields import RichTextUploadingField


blog_status = (
    ('D', 'Draft'),
    ('F', 'Featured'),
    ('P', 'Project'),
    ('PB', 'Published'),
    ('PR', 'Private'),
)

# blog custom model manager
class get_published_blogs(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~Q(status='D')).order_by('-date_added')

class get_featured_blogs(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='F').order_by('-date_added')


class Category(models.Model):
    ct = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.ct


class Blog(models.Model):
    title = models.CharField(max_length=255)
    title_slug = models.SlugField(max_length=355,unique=True,blank=True,null=True)

    content = RichTextUploadingField()

    # extra details
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=2,choices=blog_status,default='D')
    keywords = models.TextField()


    thumbnail = ProcessedImageField(upload_to="blogs",processors=[Resize(1920,1080)], format="JPEG")
    thumbnail_small = ImageSpecField(source="thumbnail",processors=[Resize(384,216)], format="JPEG")

    date_added = models.DateField(auto_now_add=True)
    last_edited = models.DateField()


    # custom managers
    objects = models.Manager()
    get_published_blogs = get_published_blogs()
    get_featured_blogs = get_featured_blogs()

    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_added = timezone.now()
            
        self.title_slug = slugify(self.title) + '-' + self.date_added.strftime("%d-%b-%Y")
        self.last_edited = date.today()
        super(Blog, self).save(*args, **kwargs)