from django.urls import path
from django.views.generic import TemplateView
appname = 'frontend'

urlpatterns = [
    path('', TemplateView.as_view(template_name="frontend/index.html"), name='some'),
]