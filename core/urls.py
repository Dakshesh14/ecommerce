from django.contrib import admin
from django.urls import path, include, re_path

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    # for user authentication
    path('accounts/', include("accounts.urls"), name='accounts'),

    # for blogs related urls
    path('', include("blogs.urls"), name='blog'),

    # for blogs related urls
    path('', include("products.urls"), name='products'),

    # for frontend related urls
    path('', include("frontend.urls"), name='frontend'),

    # for ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += [
    re_path(r'^(?:.*)$', TemplateView.as_view(template_name='frontend/index.html')),
]
