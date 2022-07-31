from .models import ClimateEducation, ClimateFact
from rest_framework import serializers


class ClimateEducationSerializer(serializers.ModelSerializer):
    """
    Climate Education Serializer
    """
    class Meta:
        model = ClimateEducation
        fields = '__all__'


class ClimateFactSerializer(serializers.ModelSerializer):
    """
    Climate Fact Serializer
    """
    class Meta:
        model = ClimateFact
        fields = '__all__'
