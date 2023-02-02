from django.shortcuts import render
from .models import Director, AssociateDir, Manager, OperatorsKTZ, OperatorsElec, Crawler, Electric


def home(request):
    directors = Director.objects.filter(pk__range=(1, 4))
    asis = AssociateDir.objects.filter(pk__range=(1, 4))

    context = {
        'directors': directors,
        'asis': asis,
    }
    return render(request, 'work_site/index.html', context)
