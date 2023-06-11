from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', master, name='master'),
    path('gallery', gallery, name='gallery'),
    path('freebie', freebie, name='freebie'),
    path('send-email/', send_email_view, name='send_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
