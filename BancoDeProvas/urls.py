"""BancoDeProvas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api import views

# TODO mudar para arquivo de config
# API version
VERSION = 'api/v1'

urlpatterns = [
    # documentation
	url(r'^$', views.index),

    # entry points
	url(r'^'+VERSION+'/provas', views.get_provas), #Listagem de todas as provas
    
    # config default
    url(r'^admin/', admin.site.urls), #Admin do postgres
]
