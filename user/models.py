from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            ** extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('Directivo', 'Directivo'),
        ('Trabajador', 'Trabajador'),
        ('Cliente', 'Cliente'),
        ('Empresa', 'Empresa')
    )
    username = models.CharField(db_index=True, unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    name = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    rol = models.CharField(max_length=255, blank=True,
                           choices=ROLES, default='Trabajador')
    objects = CustomUserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
