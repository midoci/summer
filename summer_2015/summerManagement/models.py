#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import json
import hashlib
from _models.models import *
from django.shortcuts import redirect
import urllib


u_id = 0
class weixin(object):
    def __init__(self):
        pass
    
    def get_user_info(self,request,key = None):
        url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_userinfo&state=%s#wechat_redirect'
        url = url % (APPID, "http://hudong.midoci.com/dafuweng", key)
        return redirect(url)
    
    def dafuweng(self,request):
        code = request.GET.get('code')
        if code:
            try:
                user_info = self.getUnionID(appid=APPID, secret=SECRET, code=code)
                u_id = u_id+1
                print user_info
                #if SummerUserInfo.objects.filter(u_id = u_id).exists():
                #    s_user_info = SummerUserInfo.objects.filter(u_id = u_id)
                
                #这里预留 保存数据
            except Exception,e:
                print e
        return u_id
    def getUnionID(self,appid=None, secret=None, code=None):
        userinfo = {}
        try:
            url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&redirect_uri&secret=%s&code=%s&grant_type=authorization_code'
            url = url % (appid, secret, code)
            response = urllib.urlopen(url)
            result = response.read().decode("utf8")
            response.close()
            result_dict = json.loads(result)
            userinfo_url = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s'
            userinfo_url = userinfo_url % (result_dict["access_token"], result_dict['openid'])
            response = urllib.urlopen(userinfo_url)
            userinfo = response.read().decode("utf8")
            userinfo = json.loads(userinfo)
            response.close()
            print userinfo
        except Exception, e:
            print e
            return {}

        
    def summer_user_info(self,request):
        u_id = request.POST.get('u_id')
        u_id = json.loads(u_id)
        if SummerUserInfo.objects.filter(u_id = u_id).exists():
            s_user_info = SummerUserInfo.objects.filter(u_id = u_id)
            now_position = s_user_info[0].now_position
            coin = s_user_info[0].coin
        else:
            try:
                user_info = SummerUserInfo.objects.create(u_id = u_id,
                                                          coin = 10,
                                                          now_position = 0,
                                                          last_play_time = datetime.datetime.now(),
                                                          )
                user_info.save()
                now_position = 0
                coin = 10
            except Exception,e:
                print e 
        return now_position,coin