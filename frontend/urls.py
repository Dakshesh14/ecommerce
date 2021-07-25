from django.urls import path
from django.views.generic import TemplateView

app_name = 'frontend'

from .views import (
    index
)

urlpatterns = [

    # for index page
    path('', index, name="index"),

    path('', TemplateView.as_view(template_name="frontend/index.html"), name='frontend'),
]
