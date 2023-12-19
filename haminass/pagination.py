from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 5

class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            # 'page': int(self.request.GET.get('page', DEFAULT_PAGE)), # can not set default = self.page
            # 'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'data': data
        })