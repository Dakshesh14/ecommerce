from django.shortcuts import render


from products.models import Item
from blogs.models import Blog


def index(request):
    qs = Item.get_featured_product.all()
    blog_qs = Blog.objects.all()[:6]
    return render(request, "pages/index.html", {
        'qs': qs,
        'blog_qs': blog_qs,
    })
