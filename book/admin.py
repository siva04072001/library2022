from django.contrib import admin
from book . models import Book, Rating, audio, video

admin.site.register(Book)
admin.site.register(Rating)
admin.site.register(audio)
admin.site.register(video)