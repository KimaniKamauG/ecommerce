from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Weka email wewe!')
        if not password:
            raise ValueError('Finya password ya maana bana!')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 
    


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=200)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []