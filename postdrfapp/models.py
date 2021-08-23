from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext as _
from PIL import Image
# Create your models here.


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.gender


class MyCustomUser(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            return ValueError("User must have email")
        if not username:
            return ValueError("User must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        # hashing the entered password
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            # normalize mean, lowercasing the entered characters
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(verbose_name='email', max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyCustomUser()
    # For checking permissions. to keep it simple all admin have ALL permissons

    def has_perm(self, perm, obj=None):
        return self.is_admin
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)

    def has_module_perms(self, app_label):
        return True
        
    def __str__(self):
        return self.username


class PostType(models.Model):
    post_type = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.post_type


class Post(models.Model):
    user = ForeignKey(CustomUser, on_delete=models.CASCADE)
    postuuid = models.PositiveSmallIntegerField(unique=True)
    posttype = models.ForeignKey(PostType, on_delete=models.DO_NOTHING)
    image = models.ImageField(default ='default.jpg', upload_to ='images/%y/%m/%d/')

    def __str__(self):
        return self.user.username
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
