# serialization in django
from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'contact', 'location')
        # fields = '__all__'

    def create(self, validated_data):
        pass
        return
