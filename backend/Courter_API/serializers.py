from rest_framework import serializers
from . import models


class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class courtSerializer(serializers.ModelSerializer):
    current_court = serializers.SlugRelatedField(many=True, slug_field='username', queryset=models.Player.objects.filter(logged_in=True, waiting_court__isnull=True))
    waiting_court = serializers.SlugRelatedField(many=True, slug_field='username', queryset=models.Player.objects.filter(logged_in=True, current_court__isnull=True))

    class Meta:
        model = models.Court
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
