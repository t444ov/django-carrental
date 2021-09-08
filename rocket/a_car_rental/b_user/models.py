from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone


class User(AbstractUser):
    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
        db_column='id'
    )
    username = models.CharField(
        error_messages={'unique': 'A user with that username already exists.'},
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator()],
        verbose_name='username'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        db_column='email'
    )
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(4)],
        verbose_name='Password',
        db_column='password'
    )
    last_login = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='last login'
    )
    is_superuser = models.BooleanField(
        default=False,
        help_text='Designates that this user has all permissions without explicitly assigning them.',
        verbose_name='superuser status'
    )
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
        verbose_name='staff status'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
        verbose_name='active'
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name='date joined',
        db_column='date_joined'
    )
    ALPHA = RegexValidator(r'^[a-zA-Zа-яА-Я]*$', 'Only alpha characters are allowed.')
    last_name = models.CharField(
        max_length=60,
        validators=[ALPHA],
        verbose_name='Last name',
        db_column='last_name'
    )
    first_name = models.CharField(
        max_length=60,
        validators=[ALPHA],
        verbose_name='First name',
        db_column='first_name'
    )
    patronymic = models.CharField(
        max_length=60,
        validators=[ALPHA],
        null=True,
        blank=True,
        verbose_name='Patronymic',
        db_column='patronymic'
    )
    date_of_birth = models.DateField(
        verbose_name='Date of birth',
        db_column='date_of_birth'
    )
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(
        max_length=7,
        choices=GENDER,
        verbose_name='Gender',
        db_column='gender'
    )
    NUMERIC = RegexValidator(r'^[0-9+]*$', 'Only numeric characters are allowed.')
    phone_number = models.CharField(
        max_length=12,
        validators=[MinLengthValidator(12), NUMERIC],
        unique=True,
        verbose_name='Phone number',
        db_column='phone_number'
    )
    # document_1 = models.ImageField(
    #     upload_to='img/user_document/',
    #     null=True,
    #     blank=True,
    #     verbose_name="Front side of the document (Driver's license or Pass)",
    #     db_column='document_1'
    # )
    # document_2 = models.ImageField(
    #     upload_to='img/user_document/',
    #     null=True,
    #     blank=True,
    #     verbose_name="Back side of the document (Driver's license or Pass)",
    #     db_column='document_2'
    # )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'
        db_table = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.email}, {self.phone_number}'
