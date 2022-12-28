from django.shortcuts import render
from .models import Work


def master(request):
    works = Work.objects.all()
    data = {
        'works': works,
    }
    return render(request, 'me/master.html', data)
