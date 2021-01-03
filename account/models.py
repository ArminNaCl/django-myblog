from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse 

# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError("User must have a Email field")
        user = self.model(
                        email =self.normalize_email(email),
                        **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        user = self.create_user(
                            email =self.normalize_email(email) ,
                            password=password,
                            **kwargs
        )
        user.save(using = self._db)
        return user




class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"),unique=True, db_index=True)
    # avatar = models.ImageField(_("Avatar"), upload_to = 'user/avatar', blank = True)
    full_name = models.CharField(_("Full Name"), max_length= 60 ,default=' ')
    is_staff = models.BooleanField(_("staff_status") , default=False)
    is_superuser = models.BooleanField(_("superuser"),default=False)
    create_at = models.DateTimeField(_("Creat at") , auto_now=True)
    update_at = models.DateTimeField(_('Last update'),auto_now=True)


    is_active = True
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    objects = UserManger()

    # def get_absolute_url(self):
    #     return reverse("blog-view")

    def clean(self):
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the user full_name.
        """
        return self.full_name

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')