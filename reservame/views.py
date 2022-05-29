from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from reservame.serializers import *
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from reservame.models import *
from django.utils.decorators import method_decorator
# Create your views here.

class AdminView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = AdminSerializer

    def get_queryset(self):
        return Admin.objects.all()
class UserAccountView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UserCreateSerializer

    def get_queryset(self):
        return UserAccount.objects.all()
class PymeView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PymeSerializer
    
    def get_queryset(self):
        return Pyme.objects.all()

class AppointmentView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
        return Appointment.objects.all()

class UserClientView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UserClientSerializer

    def get_queryset(self):
        return UserClient.objects.all()

class BusinessLineView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BusinessLineSerializer

    def get_queryset(self):
        return BusinessLine.objects.all()

class ProfessionistView(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = ProfessionistSerializer

    def get_queryset(self):
        return Professionist.objects.all()

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request,format=None):
        return Response({ 'success': 'CSRF cookie set' })