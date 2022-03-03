from rest_framework import serializers

from .models import Maquina, Evento, Status


class MaquinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maquina
        fields = (
            'id',
            'nome',
            'criacao',
            'ativo'
        )


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = (
            'id',
            'codigo_status',
            'data_evento',
            'criacao',
            'ativo'
        )


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = (
            'id',
            'nome',
            'codigo',
            'maquina',
            'criacao',
            'ativo'
        )