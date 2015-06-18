#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import urllib
from _models.models import *
from django.http import HttpResponse
from django.shortcuts import redirect
from utils.views import mp_render
import random
from models import weixin
weiXin = weixin()

def hello(request):
    return HttpResponse('hello')

def dafuweng(request):
    weiXin.dafuweng(request)
    return mp_render(request, "index.html")

def summer(request):
    return weiXin.get_user_info(request)

def admin(request):
    return mp_render(request, "index.html")


    

    