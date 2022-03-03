from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Maquina, Evento, Status
from .serializers import MaquinaSerializer, EventoSerializer, StatusSerializer


class EventoAPIView(APIView):
    """
    Api de eventos tcs
    """
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MaquinaAPIView(APIView):
    """
    Api de maquinas tcs
    """
    def get(self, request):
        maquinas = Maquina.objects.all()
        serializer = MaquinaSerializer(maquinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaquinaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StatusAPIView(APIView):
    """
    Api de status tcs
    """
    def get(self, request):
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


