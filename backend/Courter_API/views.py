from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


# Create your views here.
class AdminPlayerViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Player.objects.all()
    serializer_class = serializers.playerSerializer


class AdminCourtViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Court.objects.all()
    serializer_class = serializers.courtSerializer


class CourtView(APIView):
    def get(self, request):
        court = models.Court.objects.all()
        serializer = serializers.courtSerializer(court, many=True)
        return Response(serializer.data)

