from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # URL DE TESTE
    url(r'^register/$', views.register, name='register'),
    url(r'^register/create_user', views.create_user, name='create_user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
