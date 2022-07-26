from rest_framework import serializers
from . import models


class adminPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class courtSerializer(serializers.ModelSerializer):
    current_court = serializers.SlugRelatedField(many=True, slug_field='username', queryset=models.Player.objects.filter(logged_in=True, waiting_court__isnull=True))
    waiting_court = serializers.SlugRelatedField(many=True, slug_field='username', queryset=models.Player.objects.filter(logged_in=True, current_court__isnull=True))

    class Meta:
        model = models.Court
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
