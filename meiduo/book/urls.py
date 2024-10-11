from django.urls import path
from django.contrib import admin
from book.views import index

# 固定写法urlpatterns = []

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index)
]
