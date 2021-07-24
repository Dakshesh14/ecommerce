from django.urls import path

from . import views

app_name = "blogs"

urlpatterns = [
    # api for listing all blogs
    path('blogs',views.BlogListAPI.as_view(),name="blogs"),

    # api for blog's detail
    path('blog/<str:title_slug>',views.BlogDetailAPI.as_view(),name="blog"),
]