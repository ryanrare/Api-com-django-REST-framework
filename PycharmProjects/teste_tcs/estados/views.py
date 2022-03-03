from rest_framework import generics

from .models import Status, Evento, Maquina
from .serializers import StatusSerializer, MaquinaSerializer, EventoSerializer


class EventosAPIviews(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class EventoAPIviews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class MaquinasAPIviews(generics.ListCreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer


class MaquinaAPIviews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer


class StatussAPIviews(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusAPIviews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer




