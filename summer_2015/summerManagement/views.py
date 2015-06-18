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
    u_id = weiXin.dafuweng(request)
    return mp_render(request, "index.html",{'u_id':u_id})

def summer(request):
    return weiXin.get_user_info(request)

def admin(request):
    return mp_render(request, "admin.html")

def getUserInfo(request):
    now_position,coin = weiXin.summer_user_info(request)
    return HttpResponse(json.dumps({"now_position": now_position,"coin":coin}))
    

    