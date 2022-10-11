from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinLengthValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_contractor', False)
        extra_fields.setdefault('is_customer', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    email = models.EmailField('E-mail адрес', unique=True)

    first_name = models.CharField("Имя", max_length=150, blank=True)
    last_name = models.CharField("Фамилия", max_length=150, blank=True)
    patronymic = models.CharField("Отчество", max_length=150, blank=True, null=True)

    is_contractor = models.BooleanField("Подрядчик", default=False)
    is_customer = models.BooleanField("Заказчик", default=False)


class CustomerManager(models.Manager):
    def create(self, **data_fields):
        user = User.objects.create_user(
            email=data_fields.get('email'),
            password=data_fields.get('password'),
            first_name=data_fields.get('first_name'),
            last_name=data_fields.get('last_name'),
            patronymic=data_fields.get('patronymic'),
            is_customer=True,
        )
        fields_for_contractor = {
            "position": data_fields.get("position"),
            "department": data_fields.get("phone_number"),
            "phone_number": data_fields.get("phone_number"),
        }
        return super().create(user=user, **fields_for_contractor)


class CustomerAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="customer_account")
    phone_number = models.CharField(
        "Телефон",
        blank=False,
        null=False,
        max_length=11,
        validators=[MinLengthValidator(limit_value=11)]
    )
    position = models.CharField("Должность", max_length=255, blank=True, null=True)
    department = models.CharField("Подразделение", max_length=255, blank=True, null=True)

    objects = CustomerManager()


class ContractorManager(models.Manager):
    def create(self, **data_fields):
        user = User.objects.create_user(
            email=data_fields.get('email'),
            password=data_fields.get('password'),
            first_name=data_fields.get('first_name'),
            last_name=data_fields.get('last_name'),
            patronymic=data_fields.get('patronymic'),
            is_contractor=True,
        )
        fields_for_contractor = {
            "TIN": data_fields.get("TIN"),
            "short_title": data_fields.get("short_title"),
            "position": data_fields.get("position"),
            "phone_number": data_fields.get("phone_number"),
        }
        return super().create(user=user, **fields_for_contractor)


class ContractorAccount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="contractor_account")
    TIN = models.CharField(
        "ИНН",
        max_length=10,
        validators=[MinLengthValidator(limit_value=10)],
        blank=False,
        null=False
    )
    short_title = models.CharField("Короткое название", max_length=255, blank=True, null=True)
    position = models.CharField("Должность", max_length=255, blank=False, null=False)
    phone_number = models.CharField(
        "Телефон",
        blank=False,
        null=False,
        max_length=11,
        validators=[MinLengthValidator(limit_value=11)]
    )

    objects = ContractorManager()
