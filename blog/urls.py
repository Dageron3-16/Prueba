from unicodedata import name
from django.urls import path, include
from .views import BlogListView

app_name="blog"

urlpatterns = [
      path('', BlogListView.as_view(), name="home")
]
