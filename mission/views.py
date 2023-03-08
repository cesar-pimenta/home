from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def mission_list(request):
    return render(request,
                 'mission/list.html', )