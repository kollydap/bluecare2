from rest_framework import serializers
from .models import Tested

class TestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tested
        fields = '__all__'