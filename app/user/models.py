from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from service.models import TimeStampedModel

CHOICES = {
    '성별': [('M', 'Male'), ('F', 'Female')],
    '가입단계': [
        ('이름', 'name'),
        ('성별', 'gender'),
        ('나이', 'age'),
        ('완료', 'complete'),
    ]
}


class YouAreUserManager(BaseUserManager):
    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('Users must have an phone address')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(phone, password, **extra_fields)


class YouAreUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(verbose_name="전화번호", max_length=30, unique=True)  # TODO PHONE
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    current_join_step = models.CharField(verbose_name='가입단계', max_length=30, blank=True, default='gender')

    email = models.EmailField(verbose_name='이메일', max_length=255, blank=True, null=True)
    birthday = models.DateField(verbose_name='생년월일', blank=True, null=True)
    gender = models.CharField(verbose_name='성별', max_length=1, choices=CHOICES['성별'], default='M')

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = YouAreUserManager()

    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '{}{}'.format(self.last_name, self.first_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.phone


class Device(TimeStampedModel):
    class Meta:
        verbose_name = "기기 정보"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    user = models.ForeignKey('user.YouAreUser', verbose_name='사용자')
    unique_key = models.CharField(verbose_name="Device 고유키", max_length=200, unique=True)
    is_active = models.BooleanField(verbose_name="유효", default=True)


class Friends(TimeStampedModel):
    class Meta:
        verbose_name = '친구'
        verbose_name_plural = verbose_name

    user = models.ForeignKey(YouAreUser, verbose_name='사용자')
    phone = models.CharField(verbose_name='전화번호', max_length=30, blank=True, null=True)
    name = models.CharField(verbose_name='이름', max_length=30, blank=True, null=True)
    # 안 쓸듯
    email = models.EmailField(verbose_name='이메일', max_length=255, blank=True, null=True)
    birthday = models.DateField(verbose_name='생년월일', blank=True, null=True)
    gender = models.CharField(verbose_name='성별', max_length=1, choices=CHOICES['성별'], default='M', blank=True,
                              null=True)
