from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyAccountManager(BaseUserManager):

    def create_user(self,email,username,phone,name,password=None):

        '''
            

        '''
        if not email:
            raise ValueError()
        if not username:
            raise ValueError()
        user  = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email",max_length=255,unique=True)
    #required as it is for custom user imp****
    username        = models.CharField(max_length=30,unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    #*******required as it is for custom user imp
    phone           = models.CharField(max_length=10)
    name            = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True


class Property(models.Model):
    property_name         = models.CharField(max_length=100, verbose_name=("property name"))
    property_holder       = models.ForeignKey(Account,default = None, verbose_name= ("property holder"), on_delete=models.CASCADE)
    property_description  = models.CharField(max_length=2000,verbose_name='property description')
    property_available    = models.BooleanField(default=True)
    property_rent         = models.FloatField(max_length=100)
    property_address      = models.CharField(max_length=500)
    property_landmark     = models.CharField(max_length=100)
    date_added            = models.DateTimeField(auto_now_add = True)
 
class PropertyImages(models.Model):
    prop_id = models.ForeignKey(Property,on_delete=models.CASCADE,default = None,)
    property_img = models.ImageField(upload_to='images/property')
    property_img_tag = models.CharField(max_length=500,default='Property Image')


# class Notifications(models.Model):
#     sent_user      = 



