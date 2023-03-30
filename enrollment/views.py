from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from schedule.models import Event

@login_required
def main(request, id, slug):
    print(Event.objects.filter(id=id, slug=slug))
    return render(request, 'enrollment/main.html')