from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import MinLengthValidator


class UserManager(BaseUserManager):
    def create_user(self, full_name, email, password=None, is_active=False):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.full_name = full_name
        user.save()

        return user

    def create_superuser(self, email, password, full_name):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.create_user(
            full_name=full_name, email=email, password=password
        )
        user.is_admin = True
        user.save()

        return user


class UserProfile(AbstractBaseUser):
    objects = UserManager()
    full_name = models.CharField(max_length=255, unique=False, default="")
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(
        max_length=255, validators=[MinLengthValidator(6)]
    )

    is_active = models.BooleanField(
        'active',
        default=False,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ["password", "full_name"]
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    ordering = ('created',)
    is_admin = models.BooleanField('admin', default=False)

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
