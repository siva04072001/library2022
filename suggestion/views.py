from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from suggestion . serializers import SuggestionSerializer
# Create your views here.
@csrf_exempt
def suggestionApi(request, stuId=0):
    
    #adding new student detail 
    
    if request.method == 'POST':
        
        data = JSONParser().parse(request)
        Serializers = SuggestionSerializer(data=data)
        if Serializers.is_valid():
            Serializers.save()
            return JsonResponse("Submitted Sucessfully", safe=False)
        return JsonResponse("Failed to submit", safe=False)