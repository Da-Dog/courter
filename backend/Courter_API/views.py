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
    serializer_class = serializers.adminPlayerSerializer


class AdminCourtViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Court.objects.all()
    serializer_class = serializers.courtSerializer


class PlayerView(APIView):
    def get(self, request):
        try:
            player = models.Player.objects.filter(logged_in=True, waiting_court__isnull=True,
                                                  current_court__isnull=True).order_by("username")
            serializer = serializers.playerSerializer(player, many=True)
            return Response(serializer.data)
        except AttributeError:
            return Response([])

    def post(self, request):
        serializer = serializers.playerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

