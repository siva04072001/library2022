from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'

class AudioConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name = 'audios'

class VudioConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name = 'videos'