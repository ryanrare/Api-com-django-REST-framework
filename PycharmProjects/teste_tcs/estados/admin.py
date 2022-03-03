from django.contrib import admin

from .models import Maquina, Evento, Status


@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criacao', 'atualizacao', 'ativo')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('codigo_status', 'data_evento', 'criacao', 'atualizacao', 'ativo')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('nome', 'maquina', 'codigo', 'criacao', 'atualizacao', 'ativo')