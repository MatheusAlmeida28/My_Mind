from django.shortcuts import render
from pessoa.models import Pessoa


def listar_monitoramento(request):

    if request.method == 'GET':
        registro = Pessoa.objects.all()

        return render(request,'home.html', {'registro': registro})





