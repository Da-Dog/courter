from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

from datetime import datetime, timedelta


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


class CourtView(APIView):
    def get(self, request):
        try:
            court = models.Court.objects.all().order_by("number")
            serializer = serializers.courtSerializer(court, many=True)
            return Response(serializer.data)
        except AttributeError:
            return Response([])

    def patch(self, request):
        try:
            player = models.Player.objects.get(username=request.data["username"])
            if player.password != request.data["password"]:
                return Response({"error": "Invalid password"})
            if player.current_court is not None:
                court = player.current_court
                if court.start_time and court.start_time + timedelta(minutes=5) < datetime.now():
                    return Response({"error": f"Court {court.number} had been started, please wait util the session ends"})
                court.current_court.remove(player)
                court.save()
                return Response({"message": f"Player removed from court {court.number}"})
            elif player.waiting_court is not None:
                court = player.waiting_court
                court.waiting_court.remove(player)
                court.save()
                return Response({"message": f"Player removed from court {court.number}"})
            else:
                return Response({"error": "Player is not in a court"})
        except KeyError:
            return Response({"error": "Argument 'username' and 'password' is required"})
        except models.Player.DoesNotExist:
            return Response({"error": "Player does not exist"})


class UpdateCourtView(APIView):
    def patch(self, request, pk):
        try:
            court = models.Court.objects.get(pk=pk)
            try:
                player = models.Player.objects.get(username=request.data['username'])
                if not player.logged_in:
                    return Response({"error": "Player is not logged in"})
                if player.password != request.data["password"]:
                    return Response({"error": "Invalid password"})
                if player.current_court is not None:
                    current_court = player.current_court
                    current_court.current_court.remove(player)
                    current_court.save()
                elif player.waiting_court is not None:
                    current_court = player.waiting_court
                    current_court.waiting_court.remove(player)
                    current_court.save()
                if not court.rental_status:
                    if request.data.get("waitlist", False) is True and court.current_court:
                        court.waiting_court.add(player)
                        court.save()
                        return Response({"message": f"Joined court {court.number}'s waiting list!"})
                    elif len(court.current_court.all()) > 4:
                        court.waiting_court.add(player)
                        court.save()
                        return Response({"message": f"Joined court {court.number}'s waiting list!"})
                    elif court.start_time and court.start_time + timedelta(minutes=5) < datetime.now():
                        court.waiting_court.add(player)
                        court.save()
                        return Response({"message": f"Joined court {court.number}'s waiting list!"})
                    else:
                        court.current_court.add(player)
                        court.save()
                        return Response({"message": f"Joined court {court.number}!"})
                else:
                    return Response({"error": "Court is currently rented"})
            except KeyError:
                return Response({"error": "Argument 'username' and 'password' is required"})
            except models.Player.DoesNotExist:
                return Response({"error": "Player does not exist"})
        except models.Court.DoesNotExist:
            return Response({"error": "Court does not exist"})

