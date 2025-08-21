from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

from menu.models import Menu

# Create your models here.


class UserDetail(models.Model):
    user = models.OneToOneField(get_user_model(), models.CASCADE, related_name="detail")
    avatar = models.ImageField("头像", "avatar", upload_to="avatar/")
    nickname = models.CharField(
        "昵称", "nickname", max_length=150, validators=[UnicodeUsernameValidator]
    )

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Role(models.Model):
    name = models.CharField(verbose_name="角色名", max_length=50)
    label = models.CharField(verbose_name="角色标签", max_length=50)
    status = models.BooleanField(verbose_name="状态", default=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    menus = models.ManyToManyField(Menu, related_name="roles")
