import datetime

from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICE = (('DCG', 'DCG'),
               ('CUSTOMER', 'CUSTOMER'),
               )


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_validation_email = models.BooleanField(default=False, verbose_name='is_validation_email')   # 是否验证邮件
    telephone = models.CharField('Telephone', max_length=100, blank=True)
    last_update = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'
        ordering = ['user__id', ]

    def __str__(self):
        return self.user.__str__()


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=30, verbose_name="Verify Code")
    email = models.EmailField(max_length=50, verbose_name=u"Email")
    send_type = models.CharField(verbose_name="Verify Type",
                                 choices=(("register", "Register"), ("forget", "Forget Password"),
                                          ("update_email", "Modify Email")),
                                 max_length=30)
    is_used = models.BooleanField(default=False, verbose_name='is_used')
    send_time = models.DateTimeField(verbose_name="Send Date", auto_now=True)

    class Meta:
        verbose_name = "Email Verify"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
