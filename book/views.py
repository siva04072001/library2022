from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from book.models import Book, Rating, audio, video, audioRating, videoRating
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from book.serializers import AudioSerializer, BookSerializer, RatingSerializer, UserSerializer, VideoSerializer, audioRatingSerializer, videoRatingSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class BookViewset(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    queryset=Book.objects.all()
    authentication_classes=(TokenAuthentication,)

    @action(detail=True, methods=['POST'])
    def rate_book(self, request, pk=None):
        if 'stars' in request.data:

            book=Book.objects.get(id=pk)
            print('Book Title', book.title)

            user=request.user
            
            print('user', user)

            stars= request.data['stars']

            try:
                rating=Rating.objects.get(user=user.id, book=book.id)
                rating.stars=stars
                rating.save()
                serializer=RatingSerializer(rating, many=False)
                response={'message':'Rating upated', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating=Rating.objects.create(user=user, book=book, stars=stars)
                serializer=RatingSerializer(rating, many=False)
                response={'message':'Rating created', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response={'message':'you need to provide ratings'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def SaveFile(request):
        file=request.FILES['uploadedFile']
        file_name= default_storage.save(file.name,file)

        return JsonResponse(file_name, safe=False) 
 


class RatingViewset(viewsets.ModelViewSet):
    serializer_class=RatingSerializer
    queryset=Rating.objects.all()
    authentication_classes=(TokenAuthentication,)
    
    def update(self, request, *args, **kwargs):
        response={'message':'you cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response={'message':'you cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class audioViewset(viewsets.ModelViewSet):
    serializer_class=AudioSerializer
    queryset=audio.objects.all()
    authentication_classes=(TokenAuthentication,)

    @action(detail=True, methods=['POST'])
    def rate_audio(self, request, pk=None):
        if 'stars' in request.data:

            audios=audio.objects.get(id=pk)
            print('Book Title', audio.title)

            user=request.user
            
            print('user', user)

            stars= request.data['stars']

            try:
                rating=audioRating.objects.get(user=user.id, audios=audios.id)
                rating.stars=stars
                rating.save()
                serializer=audioRatingSerializer(rating, many=False)
                response={'message':'Rating upated', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating=audioRating.objects.create(user=user, audios=audios, stars=stars)
                serializer=audioRatingSerializer(rating, many=False)
                response={'message':'Rating created', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response={'message':'you need to provide ratings'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



    @csrf_exempt
    def SaveFile(request):
        file=request.FILES['uploadedFile']
        file_name= default_storage.save(file.name,file)

        return JsonResponse(file_name, safe=False) 

class audioRatingViewset(viewsets.ModelViewSet):
    serializer_class=audioRatingSerializer
    queryset=audioRating.objects.all()
    authentication_classes=(TokenAuthentication,)
    
    def update(self, request, *args, **kwargs):
        response={'message':'you cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response={'message':'you cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)



class videoViewset(viewsets.ModelViewSet):
    serializer_class=VideoSerializer
    queryset=video.objects.all()
    authentication_classes=(TokenAuthentication,)

    @action(detail=True, methods=['POST'])
    def rate_video(self, request, pk=None):
        if 'stars' in request.data:

            videos=video.objects.get(id=pk)
            print('Book Title', videos.title)

            user=request.user
            
            print('user', user)

            stars= request.data['stars']

            try:
                rating=videoRating.objects.get(user=user.id, videos=videos.id)
                rating.stars=stars
                rating.save()
                serializer=videoRatingSerializer(rating, many=False)
                response={'message':'Rating upated', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating=videoRating.objects.create(user=user, videos=videos, stars=stars)
                serializer=videoRatingSerializer(rating, many=False)
                response={'message':'Rating created', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response={'message':'you need to provide ratings'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def SaveFile(request):
        file=request.FILES['uploadedFile']
        file_name= default_storage.save(file.name,file)

        return JsonResponse(file_name, safe=False) 

class videoRatingViewset(viewsets.ModelViewSet):
    serializer_class=videoRatingSerializer
    queryset=videoRating.objects.all()
    authentication_classes=(TokenAuthentication,)
    
    def update(self, request, *args, **kwargs):
        response={'message':'you cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response={'message':'you cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
