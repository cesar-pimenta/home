from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mission.models import Mission


def mission_list(request):
    missoes = Mission.objects.filter(status_missao=2) # Filtra missoes com status ativa.
    return render(request,
                 'mission/list.html', {'missoes': missoes})


def mission_detail(request, id, slug):
    missao = get_object_or_404(Mission, id=id,
                                         slug=slug,
                                         status_missao=2)
    return render(request,
                  'mission/detail.html',
                  {'missao': missao,})