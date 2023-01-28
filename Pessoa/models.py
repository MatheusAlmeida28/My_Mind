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

    acontecimento_negativo = models.TextField('Acontecimento Negativo',max_length=100)
    acontecimento_positivo = models.TextField('Acontecimento Positivo',max_length=100)
    estado_mental =  models.CharField("Selecione o seu estado mental atual", max_length=30,choices=avaliacao_diaria)
    alerta_crises = models.CharField("Selecione o seu estado de crise", max_length=30,choices=alerta_crises)
    data_atual = models.DateTimeField(auto_now=True)
    data_acontecimento = models.DateTimeField(auto_now=False)
    data_superaçao = models.DateTimeField(auto_now=False)
