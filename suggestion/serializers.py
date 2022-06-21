from django.contrib.auth.models import User
from rest_framework import fields, serializers
from suggestion . models import suggestion

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=suggestion
        fields= '__all__'