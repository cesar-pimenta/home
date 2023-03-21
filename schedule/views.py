from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event


def schedule_list(request):
    schedules = Event.objects.all()

    return render(request,
                 'schedule/list.html',
                  {'schedules': schedules} )


def schedule_detail(request, id, slug):
    schedule = get_object_or_404(Event, id=id,
                                         slug=slug,)
    return render(request,
                  'schedule/detail.html',
                  {'schedule': schedule,})

