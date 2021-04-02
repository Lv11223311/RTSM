from django.db import models

# Create your models here.
from django_countries.fields import CountryField
from django.core.validators import RegexValidator


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    phone_regex = RegexValidator(regex='1[0-9]{10}',
                                 message="Phone number must be entered in the format: '12345678901'. Up to 11 digits allowed.")

    account = models.CharField(max_length=128, unique=True, verbose_name="账号")
    name = models.CharField(max_length=128, verbose_name="姓名")
    password = models.CharField(max_length=256, verbose_name="密码")
    country = CountryField(multiple=True, default="中国", verbose_name="国家")
    email = models.EmailField(unique=True, verbose_name="邮箱")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    verbose_name="手机号")  # validators should be a list
    sex = models.CharField(max_length=32, choices=gender, default="男", verbose_name="性别")
    c_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
