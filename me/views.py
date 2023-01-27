from django.shortcuts import render
from .models import Work


def master(request):
    works = Work.objects.all()
    work3 = Work.objects.all().order_by('-created_at')[:3]
    data = {
        'work3': work3,
        'works': works,
    }
    return render(request, 'me/master.html', data)
