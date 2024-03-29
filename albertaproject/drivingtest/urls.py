from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('result/', views.result, name='result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
