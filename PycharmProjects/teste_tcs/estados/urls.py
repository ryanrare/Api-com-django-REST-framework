from django.urls import path

from .views import EventoAPIviews, EventosAPIviews, MaquinaAPIviews, MaquinasAPIviews, StatusAPIviews, StatussAPIviews

urlpatterns = [
    path('maquinas/', MaquinasAPIviews.as_view(), name='maquinas'),
    path('maquinas/<int:pk>', MaquinaAPIviews.as_view(), name='maquina'),
    path('maquinas/<int:maquina_pk>/eventos', EventosAPIviews.as_view(), name='maquina_eventos'),
    path('maquinas/<int:maquina_pk>/status', StatussAPIviews.as_view(), name='maquina_status'),

    path('eventos/', EventosAPIviews.as_view(), name='eventos'),
    path('eventos/<int:pk>', EventoAPIviews.as_view(), name='evento'),
    path('eventos/<int:evento_pk>/maquinas', MaquinasAPIviews.as_view(), name='evento_maquinas'),
    path('eventos/<int:evento_pk>/status', StatussAPIviews.as_view(), name='evento_status'),


    path('status', StatussAPIviews.as_view(), name='status'),
    path('status/<int:pk>', StatusAPIviews.as_view(), name='status'),
    path('status/<int:status_pk>maquinas', MaquinasAPIviews.as_view(), name='status_maquinas'),
    path('status/<int:_status_pk>eventos', EventosAPIviews.as_view(), name='status_eventos'),

]