from django.db import models
from django.contrib.auth.models import AbstractUser as _AbstractUser, UserManager as _UserManager
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone


# Create your models here.
class Bvisa(models.Model):
	employee_name = models.CharField(max_length=70)
	enterprise_id = models.EmailField(max_length=70)
	# project = models.CharField(max_length=70)
	PROJECT_OPTIONS = (("Cigna","Cigna"),("Anthem","Anthem"))
	project = models.CharField(max_length=1,choices=PROJECT_OPTIONS)
	whatsapp_number = models.DecimalField(max_digits=10,decimal_places=0)
	travel_start_date = models.DateField(auto_now=False,auto_now_add=False)
	travel_end_date =  models.DateField(auto_now=False,auto_now_add=False)
	CAPABILITY_OPTIONS = (("Capability1","Capability1"),("Capability2","Capability2"))
	capability = models.CharField(max_length=1,choices=CAPABILITY_OPTIONS)



# class UserManager(_UserManager):
#     def register(self,membership_start_date,membership_end_date, first_name, username, password, email,user_type,last_name='',verify_code='',verify_time_limit='',):
#         if self.count()==0:
#             user = self.create_superuser(membership_start_date=membership_start_date,
#                                         membership_end_date=membership_end_date,
#                                         username=username,
#                                         first_name=first_name,
#                                         email=email,
#                                         password=password,
#                                         last_name=last_name,
#                                         verify_code=verify_code,
#                                         verify_time_limit=verify_time_limit,
#                                         user_type=user_type,
#                                         is_active=True)

#         else:
#             user = self.create_user(membership_start_date=membership_start_date,
#                                         membership_end_date=membership_end_date,
#                                         username=username,
#                                         first_name=first_name,
#                                         email=email,
#                                         password=password,
#                                         last_name=last_name,
#                                         verify_code=verify_code,
#                                         verify_time_limit=verify_time_limit,
#                                         user_type=user_type)

#         return user


# class AbstractUser(_AbstractUser):
#     user_type = models.ForeignKey(Membership, blank=True, null=True,on_delete=models.PROTECT)
#     membership_start_date = models.DateTimeField(blank=True, null=True)
#     membership_end_date = models.DateTimeField(blank=True, null=True)
#     is_active = models.BooleanField(default=False)
#     verify_code = models.CharField(max_length=512, blank=True, null=True, help_text='Account verification code', editable=False)
#     verify_time_limit = models.DateTimeField(blank=True, null=True, editable=True)
#     reset_code = models.CharField(max_length=512, blank=True, null=True, help_text='Account verification code', editable=False)
#     reset_time_limit = models.DateTimeField(blank=True, null=True, editable=False)
#     created_on = models.DateTimeField(auto_now=True)
#     updated_on = models.DateTimeField(auto_now_add=True)

#     objects = UserManager()

#     REQUIRED_FIELDS = ['email',]

#     class Meta:
#         abstract = True
#         indexes = [
#             models.Index(fields=['email','user_type','is_active'], name='user_idx'),
#             models.Index(fields=['email'],name='user_email_idx')
#         ]

#     @classmethod
#     def get_by_username(cls, username):

#         return cls.objects.get(username__iexact=username)

# class User(AbstractUser):
#     """
#     Extends Django authentication user model.
#     """

