from django.db import models

class Pessoa(models.Model):

    avaliacao_diaria = {
        ('P', 'PÉSSIMO'),    
        ('R', 'RUIM'),    
        ('B', 'BOM'),
        ('E', 'EXCELENTE'),
        }

    alerta_crises = {
        ('P', 'PANICO'),    
        ('A', 'ANSIEDADE'),    
        ('D', 'DEPRESSAO'),
    }

    acontecimento_negativo = models.TextField('Acontecimento Negativo',max_length=2000)
    acontecimento_positivo = models.TextField('Acontecimento Positivo',max_length=2000)
    estado_mental =  models.CharField("Selecione o seu estado mental atual",choices=avaliacao_diaria)
    alerta_crises = models.CharField("Selecione o seu estado de crise",choices=alerta_crises)
    data_atual = models.DateTimeField(auto_now=True)
    data_acontecimento = models.DateTimeField(auto_now=False)
    data_superaçao = models.DateTimeField(auto_now=False)
