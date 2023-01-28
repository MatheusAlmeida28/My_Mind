from django.shortcuts import render
from pessoa.models import Pessoa


def listar_monitoramento(request):

    if request.method == 'GET':
        registros = Pessoa.objects.all()

        return render(request,'home.html', {'registros': registros})

    





