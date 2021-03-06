from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^candidato', views.candidato, name='candidato'),
    url(r'^resultado/(?P<votacao>[SNA]+)', views.resultado, name='resultado')
]