from django.conf.urls import url, include
from django.contrib import admin
from api import views
from rest_framework import routers

VERSION = 'api/v1/'

router = routers.SimpleRouter(trailing_slash='optional')
router.register(r'provas', views.ProvasViewSet)
router.register(r'cursos', views.CursosViewSet)
router.register(r'disciplinas', views.DisciplinaViewSet)
router.register(r'periodos', views.PeriodosViewSet)

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^provas/(?P<pk>[^/.]+)/add/$', views.ProvasViewSet.as_view({'get':'incrementar_classificacao_prova'}))
]

urlpatterns += router.urls