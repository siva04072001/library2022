from enum import unique
from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=300, blank=False, unique=True)
    author=models.CharField(max_length=300, default=None)
    description=models.TextField(max_length=300, blank=True)
   # price=models.DecimalField(default=0,max_digits=5, decimal_places=2)
    published=models.DateField(blank=True, null=True, default=None)
    is_published=models.BooleanField(default=False)

    class genreChoice(models.TextChoices):
        Choose="-----"
        Action="Action"
        Sci_Fi="Sci_Fi"
        Education="Education"
        Fantasy="Fantasy"
    genre=models.CharField(max_length=50, choices=genreChoice.choices, default=None)
    photoFile= models.ImageField(upload_to='media/', blank=True)
    file=models.FileField(upload_to='media/', blank=True)
    

    def no_of_rating(self):
        ratings=Rating.objects.filter(book=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings=Rating.objects.filter(book=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0

    def __str__(self) -> str:
        return self.title

class Rating(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together=(('user','book'),)
        index_together=(('user','book'),)
    def __int__(self) -> int:
        return self.book

#audio class
class audio(models.Model):
    title=models.CharField(max_length=100,default=None)
    author=models.CharField(max_length=100, default=None)
    description=models.TextField(max_length=300, blank=True)
    published=models.DateField(blank=True, null=True, default=None)
    is_published=models.BooleanField(default=False)
    class genreChoice(models.TextChoices):
        Choose="-----"
        Action="Action"
        Sci_Fi="Sci_Fi"
        Education="Education"
        Fantasy="Fantasy"
    genre=models.CharField(max_length=50, choices=genreChoice.choices, default=None)
    photoFile= models.ImageField(upload_to='media/', blank=True)
    file=models.FileField(upload_to='media/', blank=True)

    

    def no_of_rating(self):
        ratings=audioRating.objects.filter(audios=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings=audioRating.objects.filter(audios=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0

    def __str__(self) -> str:
        return self.title

class audioRating(models.Model):
    audios=models.ForeignKey(audio, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together=(('user','audios'),)
        index_together=(('user','audios'),)
    def __int__(self) -> int:
        return self.audios


#video class
class video(models.Model):
    title=models.CharField(max_length=100,default=None)
    author=models.CharField(max_length=100, default=None)
    description=models.TextField(max_length=300, blank=True)
    published=models.DateField(blank=True, null=True, default=None)
    is_published=models.BooleanField(default=False)
    class genreChoice(models.TextChoices):
        Choose="-----"
        Action="Action"
        Sci_Fi="Sci_Fi"
        Education="Education"
        Fantasy="Fantasy"
    genre=models.CharField(max_length=50, choices=genreChoice.choices, default=None)
    photoFile= models.ImageField(upload_to='media/', blank=True)
    file=models.FileField(upload_to='media/', blank=True)

    def no_of_rating(self):
        ratings=videoRating.objects.filter(videos=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings=videoRating.objects.filter(videos=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0

    def __str__(self) -> str:
        return self.title

class videoRating(models.Model):
    videos=models.ForeignKey(video, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together=(('user','videos'),)
        index_together=(('user','videos'),)
    def __int__(self) -> int:
        return self.videos