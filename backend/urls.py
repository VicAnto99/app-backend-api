"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from rest_framework import routers
from reservame import views
from reservame.admin import reservame_site
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView


router = routers.DefaultRouter()
router.register(r'pymes', views.PymeView, 'pyme')
router.register(r'appointments', views.AppointmentView, 'appointment')
router.register(r'user_accounts', views.UserAccountView, 'user_account')
router.register(r'users_clients', views.UserClientView, 'user_client')
router.register(r'business_lines', views.BusinessLineView, 'business_line')
router.register(r'professionists', views.ProfessionistView, 'professionist')
router.register(r'admins', views.AdminView, 'admin')


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'reservame_admin/', reservame_site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', TemplateView.as_view(template_name="index.html"))    
]

#urlpatterns += [re_path(r'^.*', csrf_exempt(TemplateView.as_view(template_name='index.html')))]


