from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Banks

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'
