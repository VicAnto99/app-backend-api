from rest_framework import serializers
from reservame.models import *
from rest_framework_mongoengine import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class AdminSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Admin
        fields = 'id','name', 'last_name', 'phone_number', 'profile_image', 'email', 'uid',
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = 'id', 'email', 'name', 'password',

class PymeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Pyme
        fields = 'id', 'name', 'address', 'slogan','employees', 'business_line', 'description' ,'custom_data_form', 'image_url', 'admin'  

class AppointmentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Appointment
        fields = 'id', 'date', 'reason', 'pyme', 'completed', 'data', 'responsable'

class UserClientSerializer(serializers.DocumentSerializer):
    class Meta:
        model = UserClient
        fields = 'id', 'name', 'last_name', 'phone_number', 'profile_image', 'email', 'uid', 'appointments', 'calendar', 'is_admin'

class BusinessLineSerializer(serializers.DocumentSerializer):
    class Meta: 
        model = BusinessLine
        fields = 'id', 'name', 'description', 'pymes', 'image_description', 'static_forms'

class ProfessionistSerializer(serializers.DocumentSerializer):
    class Meta: 
        model = Professionist
        fields = 'id','name', 'last_name', 'phone_number', 'profile_image', 'email', 'calendar'

