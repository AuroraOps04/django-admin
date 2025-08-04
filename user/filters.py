import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFilter(django_filters.FilterSet):
    nickname = django_filters.CharFilter(lookup_expr='icontains', field_name="detail__nickname")
    username = django_filters.CharFilter(lookup_expr='icontains', field_name="username")

    class Meta:
        model = User
        fields = {
            "is_active": ["exact"],
            #"username": ["icontains"], # 等于生成了一个 username__icontains 而不是 定义了一个 username 然后 匹配方式是icontains
        }