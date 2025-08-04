from rest_framework.pagination import PageNumberPagination


class VbenPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "size"

    def paginate_queryset(self, queryset, request, view=None):
        if (
                int(request.query_params.get(self.page_query_param, "1")) == -1
                and int(request.query_params.get(self.page_size_query_param, f"{self.page_size}")) == -1
        ):
            return None
        return super().paginate_queryset(queryset, request, view)
