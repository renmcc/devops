#!/usr/bin/env python
#coding:utf8
#__time__:2019/8/913:47
#__author__:"ren_mcc"
from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    def get_page_size(self, request):
        try:
            page_size = request.query_params.get("page_size", -1)
            if page_size < 0:
                return self.page_size
            return page_size
        except:
            pass
        return self.page_size