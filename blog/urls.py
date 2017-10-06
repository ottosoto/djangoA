from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar_publicacion ),
    url(r'^postear/(?P<pk>[0-9]+)/$', views.detalle_publicacion, name='postear'),
    url(r'^postear/nuevo/$' , views.nueva_publicacion, name='nueva_publicacion'),
    url(r'^postear/(?P<pk>[0-9]+)/editar/$', views.editar_publicacion, name='editar_publicacion'),
    url(r'^borrador/$', views.borradores_publicacion, name='borradores_publicacion'),
    url(r'^postear/(?P<pk>\d+)/publicar/$', views.postear_publicacion, name='postear_publicacion'),
    url(r'^postear/(?P<pk>\d+)/remover/$', views.remover_publicacion, name='remover_publicacion'),
]
