from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin    
)


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, phone_no, password=None):
        if not email:
            raise ValueError("User must have an Email address!")
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            username=username,
            phone_no=phone_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, username, phone_no, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_no=phone_no,
            password=password,
        )
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    phone_no = models.IntegerField()

    is_active = True
    is_staff = False
    is_superuser = False

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_no"]

    def __str__(self):
        return self.email
