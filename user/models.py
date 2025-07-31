from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from typing import ClassVar
from django.db.models.manager import BaseManager

# Create your models here.


class UserDetail(models.Model):
    user = models.OneToOneField(get_user_model(), models.CASCADE, related_name="detail")
    avatar = models.ImageField("头像", "avatar", upload_to="avatar/")
    nickname = models.CharField(
        "昵称", "nickname", max_length=150, validators=[UnicodeUsernameValidator]
    )
