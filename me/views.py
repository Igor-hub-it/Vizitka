from django.shortcuts import render
from .models import Work
from django.core.paginator import Paginator

def master(request):
    works = Work.objects.all()
    work3 = Work.objects.all().order_by('-created_at')[:3]
    data = {
        'work3': work3,
        'works': works,
    }
    return render(request, 'me/master.html', data)

def gallery(request):
    works = Work.objects.all()
    paginator = Paginator(works, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'works': works,
        'page_obj': page_obj,
    }
    return render(request, 'me/gallery.html', data)
