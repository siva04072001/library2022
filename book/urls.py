from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework.authtoken.views import obtain_auth_token
from .views import BookViewset, RatingViewset, UserViewset, audioRatingViewset, audioViewset, videoViewset, videoRatingViewset
from django.conf.urls.static import static
router= routers.DefaultRouter()
router.register('book',BookViewset)
router.register('users',UserViewset)
router.register('rating',RatingViewset)
router.register('audiorating',audioRatingViewset)
router.register('videorating',videoRatingViewset)
router.register('audio',audioViewset)
router.register('video',videoViewset)

from django.conf import Settings, settings


urlpatterns = [
    
    path('',include(router.urls)),
    path('auth/',obtain_auth_token),
    
    
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
