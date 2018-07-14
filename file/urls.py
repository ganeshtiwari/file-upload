from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'file'

urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.files, name='files'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
