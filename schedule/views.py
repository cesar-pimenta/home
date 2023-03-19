from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def schedule_list(request):
    return render(request,
                 'schedule/list.html', )
