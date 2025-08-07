from django.db import models

# Create your models here.


class Menu(models.Model):
    FOLDER = "folder"
    PAGE = "page"
    MENU_TYPE = ((FOLDER, "mulu"), (PAGE, "yemian"))

    name = models.CharField(verbose_name="路由名称", max_length=50, unique=True)
    path = models.CharField(
        verbose_name="路由路径",
        max_length=100,
    )
    component = models.CharField(
        verbose_name="组件路径",
        max_length=100,
    )
    type = models.CharField(
        max_length=10, verbose_name="caidan leixing", choices=MENU_TYPE
    )
    redirect = models.CharField(
        verbose_name="重定向路径", max_length=100, null=True, blank=True
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    class Meta:
        verbose_name = "菜单表"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return f"{self.name} - {self.meta.title}"


class MenuMeta(models.Model):
    BADGE_DOT = "dot"
    BADGE_NORMAL = "normal"
    BADGE_CHOICE = ((BADGE_DOT, "点"), (BADGE_NORMAL, "文字"))
    active_icon = models.CharField(
        verbose_name="激活图标（菜单)", max_length=50, null=True, blank=True
    )
    active_path = models.CharField(
        verbose_name="当前激活的菜单", max_length=50, null=True, blank=True
    )
    affix_tab = models.BooleanField(verbose_name="是否固定标签页", default=False)
    affix_tab_order = models.IntegerField(verbose_name="固定标签页的顺序", default=0)
    # authority (optional) string[]
    badge = models.CharField(verbose_name="徽标", max_length=100, null=True, blank=True)
    badge_type = models.CharField(
        verbose_name="徽标类型",
        choices=BADGE_CHOICE,
        null=True,
        max_length=10,
        blank=True,
    )
    badge_variants = models.CharField(
        verbose_name="徽标颜色", max_length=20, null=True, blank=True
    )
    full_path_key = models.BooleanField(
        verbose_name="是否将路由的完整路径作为tab key", default=True
    )
    hide_children_in_menu = models.BooleanField(
        verbose_name="页面的子页面是否在菜单中隐藏", default=False
    )
    hide_in_bread_crumb = models.BooleanField(
        verbose_name="页面是否在面包屑中隐藏", default=False
    )
    hide_in_menu = models.BooleanField(
        verbose_name="页面是否在菜单中隐藏", default=False
    )
    hide_in_tab = models.BooleanField(
        verbose_name="页面是否在标签页中隐藏", default=False
    )
    icon = models.CharField(verbose_name="图标", max_length=50, null=True, blank=True)
    iframe_src = models.CharField(
        verbose_name="iframe 地址", max_length=200, null=True, blank=True
    )
    ignore_access = models.BooleanField(verbose_name="页面是否忽略权限", default=False)
    keep_alive = models.BooleanField(
        verbose_name="页面是否开启缓存,仅在标签页启用时有效", default=False
    )
    link = models.CharField(verbose_name="外链", max_length=200, null=True, blank=True)
    title = models.CharField(
        verbose_name="标题名称",
        max_length=200,
    )
    order = models.IntegerField(verbose_name="排序", null=True, blank=True)

    menu = models.OneToOneField(
        Menu, on_delete=models.CASCADE, related_name="meta", primary_key=True
    )

    class Meta:
        verbose_name = "菜单元属性表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
