from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from common.enums import GenderTypes

from common.models import BaseModel


# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        
        if not username:
            raise ValueError('The given contact no must be set')
        
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, True, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(db_index=True, unique=True, max_length=50)
    

    is_mobile_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return u"Username: {}".format(self.username)