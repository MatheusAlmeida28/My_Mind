from django.shortcuts import render, redirect
from pessoa.models import Pessoa
from django.contrib import messages


def listar_monitoramento(request):

    if request.method == 'GET':
        registros = Pessoa.objects.all()

        return render(request,'home.html', {'registros': registros})

    elif request.method == "POST":

        nome = request.POST.get('nome')
        acontecimento_negativo = request.POST.get('acontecimento_negativo')
        acontecimento_positivo = request.POST.get('acontecimento_positivo')
        estado_mental = request.POST.get('estado_mental')
        alerta_crises = request.POST.get('alerta_crises')
        data_acontecimento = request.POST.get('data_acontecimento')
        data_superaçao = request.POST.get('data_superaçao')

        atendimento = Pessoa(
            nome = nome,
            acontecimento_negativo = acontecimento_negativo,
            acontecimento_positivo = acontecimento_positivo,
            estado_mental = estado_mental,
            alerta_crises = alerta_crises,
            data_acontecimento = data_acontecimento,
            data_superaçao = data_superaçao,

        )

        atendimento.save()
        messages.success(request, 'Resgistro Adicionado ')
        print('salvei')
        return redirect('/')




