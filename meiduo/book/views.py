from django.shortcuts import render

# Create your views here.
"""
视图
其实就是python函数
视图函数有两个要求：
    1.视图函数的第一个参数就是接受请求。这个请求就是http的HttpRequest类对象
"""
from django.http import HttpRequest
from django.http import HttpResponse


# 我们期望用户输入 http://127.0.0.1:8000/index
# 来访问视图函数

def index(request):
    return HttpResponse("OK呀")
