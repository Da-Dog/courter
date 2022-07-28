from rest_framework import serializers
from . import models


class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class courtSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Court
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
