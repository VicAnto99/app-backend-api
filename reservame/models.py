
from django.db import models
from mongoengine import Document, EmbeddedDocument, fields, CASCADE
import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from bson.objectid import ObjectId

#choices=BUSINESS_LINE
BUSINESS_LINE = (
    ('beauty_shop','Estética'),
    ('veterinary', 'Veterinaria'),
    ('fast_food','Comida rápida'),
    ('restaurant','Restaurante'),
    ('club','Discoteca'),
    ('medicine','Medicina'),
    ('coding','Programacion'),
)

# Create your models here.

class Admin(Document):
    name = fields.StringField(max_length=50, required=True)
    last_name = fields.StringField(max_length=50, default='')
    phone_number = fields.StringField(max_length=50, default='')
    profile_image = fields.URLField(default=' ')
    email = fields.EmailField()
    uid = fields.IntField()

class Professionist(Document):
    name = fields.StringField(max_length=50, required=True)
    last_name = fields.StringField(max_length=50, default='')
    phone_number = fields.StringField(max_length=50, default='')
    profile_image = fields.URLField(default=' ')
    email = fields.EmailField()
    calendar = fields.DictField()

class Pyme(Document):
    name = fields.StringField(max_length=50, required=True)
    address = fields.StringField(max_length=255)
    slogan = fields.StringField(max_length=255, default='')
    employees = fields.ListField(fields.ReferenceField(Professionist))
    business_line = fields.StringField(max_length=50)
    description = fields.StringField(max_length=500, default='No existe descripcion de la PyME')
    custom_data_form = fields.DictField()
    image_url = fields.URLField()
    admin = fields.ReferenceField(Admin)
    
    def __str__(self):
        return f'{self.name}'

class BusinessLine(Document):
    name = fields.StringField(max_length=50, required=True)
    description = fields.StringField(max_length=1000)
    pymes = fields.ListField(fields.ReferenceField(Pyme, reverse_delete_rule=CASCADE))
    image_description = fields.URLField()
    static_forms = fields.DictField()

class Appointment(Document):    
    date = fields.DateTimeField(default=datetime.datetime.utcnow) 
    reason = fields.StringField(max_length=555, default=' ')
    pyme = fields.ReferenceField(Pyme, reverse_delete_rule=CASCADE)
    completed = fields.BooleanField(default = False)
    data = fields.DictField()
    
    responsable = fields.ReferenceField(Professionist, reverse_delete_rule=CASCADE)
    
    def __str__(self):
        return f'Fecha: {self.date} \n Razon: {self.reason}'

class UserClient(Document):
    name = fields.StringField(max_length=50, required=True)
    last_name = fields.StringField(max_length=50, default='')
    phone_number = fields.StringField(max_length=50, default='')
    profile_image = fields.URLField(default=' ')
    email = fields.EmailField()
    uid = fields.IntField()
    appointments = fields.ListField(fields.ReferenceField(Appointment))
    calendar = fields.DictField()
    is_admin = fields.BooleanField(default = False)
    

    def __str__(self):
        return f'{self.name} \n {self.email}'

# ----------------------------------------------- JWT AUTH ------------------------------------------
class UserAccountManager(BaseUserManager):
    def create_user(self, email,name,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(name=name,email=email)

        user.set_password(password)
        user.save()
        

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects =  UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email