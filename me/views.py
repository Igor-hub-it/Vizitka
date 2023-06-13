from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
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
    works = Work.objects.all().order_by('-created_at')
    paginator = Paginator(works, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'works': works,
        'page_obj': page_obj,
    }
    return render(request, 'me/gallery.html', data)


def freebie(request):
    sketches = Sketches.objects.all()
    paginator = Paginator(sketches, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'works': sketches,
        'page_obj': page_obj,
    }
    return render(request, 'me/freebie.html', data)


def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        telegram = request.POST.get('telegram')
        from_email = 'igorpigidin@gmail.com'
        to_email = 'igorpigidin@gmail.com'

        send_mail(subject, message, telegram, from_email, [to_email])
        return render(request, 'me/success.html')
    else:
        return render(request, 'me/success.html')


def instructions(request):
    return render(request, 'me/instructions.html')