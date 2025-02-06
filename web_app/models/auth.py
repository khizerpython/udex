from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.core.validators import RegexValidator
from django.urls import reverse_lazy
from django.apps import apps


# App Level Imports
from web_app.models.country import City
from web_app.models.designation import Designation
from web_app.models.others import ModelUUIDField, CreatedAndUpdatedModelFields,IsActive
from web_app.models.department import Department
from web_app.models.role import Role
from web_app.models.regex import *

# Other imports
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

class CustomAuthUserManager(BaseUserManager):
    def get_query_set(self):
          return self.filter(department__is_active=True).filter(active=True)

    contact_number  = models.IntegerField(max_length=255)
    def create_user(self  ,first_name , last_name, username , email , contact_number ,password = None, **extra_fields):
        if not first_name:
            raise ValueError("User Must Have a first name")

        if not last_name:
            raise ValueError("User Must Have a last name")

        if not username:
            raise ValueError("User Must Have a username")
        if not email:
            raise ValueError("User Must Have a email") 
        if not contact_number:
            raise ValueError("User Must Have a contact number")       
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(first_name=first_name, last_name=last_name, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self , first_name, last_name, username , password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            **extra_fields
        )
        user.save(using = self._db)
        return user


GENDER_CHOICES = (
    ('Male', "Male"),
    ('Female', "Female"),
    ('Other', "Other"),
    )


phone_number_regex = RegexValidator(r'((\+923|03)[\d]{9}$|(09)[\d]{8}$|(92)[\d]{10}$|(^\d{11})$)',message="Invalid phone number")

class AuthUser(AbstractBaseUser, ModelUUIDField, CreatedAndUpdatedModelFields,IsActive):
    first_name = models.CharField(max_length=250, validators=[first_name_regex])
    last_name = models.CharField(max_length=250,validators=[last_name_regex])
    username = models.CharField(max_length=200 , unique=True, validators=[username_regex]) 
    email = models.EmailField(max_length=255, unique=False)
    contact_number = models.CharField(max_length=255,validators=[contact_number_regex])
    gender = models.CharField(choices=GENDER_CHOICES,max_length=30)
    dob = models.DateField()

    department_id = models.ManyToManyField(Department)
    role_id = models.ForeignKey(Role,on_delete=models.SET_NULL, null=True, blank=True)
    designation_id = models.ForeignKey(Designation,on_delete=models.SET_NULL, null=True, blank=True)
    city_id = models.ForeignKey(City,on_delete=models.SET_NULL,blank=True,null=True)
    is_lock = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('first_name','last_name' ,'email' ,'contact_number' ,'gender' ,'dob' ,'password')

    objects = CustomAuthUserManager()

    def __str__(self):
        return self.username
    
    @property
    def get_dashboard_url(self):
        if self.is_admin:
            return reverse_lazy("admin_dashboard_url")
        elif self.is_superuser:
            return reverse_lazy("superadmin_dashboard_url")
        else:
            return reverse_lazy("dashboard_url")
    
    @property
    def get_fullname(self):
        return self.first_name + " " + self.last_name
    
    @property
    def get_role_name(self):
        return self.role_id.name
    
    @property
    def is_user_hod(self):
        return self.role_id.is_hod_right
    
    @property
    def is_user_admin_hod(self):
        if(self.is_user_hod):
            return constants.ADMIN_DEPART_UUID in [str(d.id) for d in self.deparment_id.all()]
        return False
    
    @property
    def is_user_hr_hod(self):
        if(self.is_user_hod):
            return constants.HR_DEPART_UUID in [str(d.id) for d in self.deparment_id.all()]
        return False
    
    @property
    def is_user_cto(self):
        if(self.is_user_hod):
            return constants.CTO_DEPART_UUID in [str(d.id) for d in self.deparment_id.all()]
        return False
    
    @property
    def is_user_ch(self):
        if(self.is_user_hod):
            return constants.CH_DEPART_UUID in [str(d.id) for d in self.deparment_id.all()]
        return False
    @property
    def is_user_is(self):
        if(self.is_user_hod):
            return constants.INFOSEC_DEPART_UUID in [str(d.id) for d in self.deparment_id.all()]
        return False
    @property
    def is_user_supply_hod(self):
        if(self.is_user_hod):
            return constants.SUPPLY_CHAIN_DEPART_UUID in [str(d.id) for d in self.deparment_id.all()]
        return False
    

    
    def natural_key(self):
        return self.get_fullname
    
    @property
    def show_resend_activation_link_button(self):
        """
        Property to handle the permission of resending user activation link
        """
        if self.is_first_login: # If is_first_login is False, then the user is already using portal because this field was set to False on first login. We handle this field manually
            if self.last_login is None: # Means that the user hasn't logged-in to the portal. Just an extra sub-check of above condition. (Both current and above condition of above same nature). Framework automatically handle this field 
                self.created_at_naive = self.created_at.replace(tzinfo=None)

                # Now subtract the naive datetime
                difference = datetime.now() - self.created_at_naive

                # difference: timedelta = datetime.now(tz=ZoneInfo("UTC")) - self.created_at # calculating the difference of time from created_at to current in `UTC`
                # difference: timedelta = datetime.now() - self.created_at # calculating the difference of time from created_at to current in `UTC`
                # if difference.days >= 1: # If the difference is greater than 1 in terms of days then proceed because the link generated on the time user creation has 1 day expiry

                #     if self.is_lock and not self.is_active: # Make sure the user is locked (True) and not active (False). These values were set on time of user creation
                #         return True
                if difference.total_seconds() >= (15 * 60):
                    if self.is_lock and not self.is_active:
                        return True    

        return False


class UserForeignKey(models.Model):
    user_id = models.ForeignKey(AuthUser,on_delete=models.SET_NULL,blank=True,null=True)

    class Meta:
        abstract = True  
