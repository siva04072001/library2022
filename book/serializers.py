from django.contrib.auth.models import User
from rest_framework import fields, serializers
from rest_framework.authtoken.models import Token

from book.models import Book, Rating, audio, video, audioRating, videoRating
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('id','username','password')
        extra_kwargs={'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields= ('id','title','author','description','published','is_published','genre','photoFile','file','no_of_rating','avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields= ('id','stars','user','book')

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model=audio
        fields= ('id','title','author','description','published','is_published','genre','photoFile','file','no_of_rating','avg_rating')

class audioRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=audioRating
        fields= ('id','stars','user','audios')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=video
        fields= ('id','title','author','description','published','is_published','genre','photoFile','file','no_of_rating','avg_rating')

class videoRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=videoRating
        fields= ('id','stars','user','videos')