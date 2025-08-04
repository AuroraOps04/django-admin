from typing import ClassVar
from django.db.models.manager import BaseManager
from django.db import models


# Create your models here.

class Dictionary(models.Model):

    StatusNormal = "normal"
    StatusDisabled = "disabled"
    Status = [
        (StatusNormal, "正常"),
        (StatusNormal, "停用")
    ]
    status = models.CharField(max_length=10, choices=Status, default=StatusNormal, verbose_name="状态")
    name = models.CharField(max_length=100, verbose_name="名称")
    type = models.CharField(max_length=100, verbose_name="类型", unique=True)

    class Meta:
        verbose_name = "字典"
        verbose_name_plural = verbose_name # 如果设置的话在 admin 页面会显示 字典s

    def __str__(self):
        return f'{self.name}'


class DictionaryItem(models.Model):

    StatusNormal = "normal"
    StatusDisabled = "disabled"
    Status = [
        (StatusNormal, "正常"),
        (StatusNormal, "停用")
    ]
    Default = "default"
    NonDefault = "non_default"
    DefaultType = [
        (Default, "是"),
        (NonDefault, "否")
    ]
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name="items")
    sort = models.SmallIntegerField(verbose_name="排序", default=1)
    label = models.CharField(max_length=150)
    value = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=Status, default=StatusNormal, verbose_name="状态")
    is_default = models.CharField(max_length=20, verbose_name="是否默认", default=Default, choices=DefaultType)
    css_class = models.CharField(max_length=100, verbose_name="css 样式属性", blank=True, null=True)
    list_class = models.CharField(max_length=100, verbose_name="表格字典样式", blank=True, null=True)
    class Meta:
        verbose_name = "字典项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.dictionary.name} - {self.label}'