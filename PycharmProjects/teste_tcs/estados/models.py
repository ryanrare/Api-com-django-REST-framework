from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Maquina(Base):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Maquina'
        verbose_name_plural = ' Maquinas'

    def __str__(self):
        return self.nome


class Evento(Base):
    codigo_status = models.DecimalField(max_digits=3, decimal_places=0, auto_created=True)
    data_evento = models.DateTimeField(default=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return f'{self.codigo_status} foi criado na data {self.data_evento}'


class Status(Base):
    codigo = models.ForeignKey(Evento, related_name=None, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, related_name='maquinas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Status'

    def __str__(self):
        return f'o status "{self.nome}" possui o codigo {self.codigo} da maquina"{self.maquina}"'

