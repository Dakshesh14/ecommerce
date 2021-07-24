from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # for user authentication
    path('accounts/', include("accounts.urls"), name='accounts'),

    # for blogs related urls
    path('blog/', include("blogs.urls"), name='blog'),

    # for blogs related urls
    path('', include("products.urls"), name='products'),

    # for index page
    path('', TemplateView.as_view(template_name='pages/index.html'), name="index"),

    # for ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [
#     re_path(r'^(?:.*)$', TemplateView.as_view(template_name='frontend/index.html')),
# ]
