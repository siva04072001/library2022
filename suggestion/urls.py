from unicodedata import name
from django.db import router
from django.urls import re_path, path, include
from suggestion import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    re_path(r'^suggestion/$',views.suggestionApi),
]
urlpatterns = format_suffix_patterns(urlpatterns)