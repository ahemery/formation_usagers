"""usagers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from formation import views


urlpatterns = [
    # url(r'^admin.html/', admin.html.site.urls),

    url(r'^$', views.index_view, name='index'),

    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),

    url(r'^formation/$', views.formation_view, name='formation'),
    url(r'^formation/add/$', views.formationAdd_view, name='formation_add'),

    url(r'^stat/$', views.stat_view, name='stat'),

    url(r'^admin/$', views.admin_view, name='admin'),

]
