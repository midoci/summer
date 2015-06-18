#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.conf.urls import patterns
#
urlpatterns = patterns('',
    url(r'^admin$', 'summerManagement.views.admin',name='admin'),
    url(r'^hello$', 'summerManagement.views.hello',name='hello'),
    url(r'^2015summer$', 'summerManagement.views.summer',name='summer'),
    url(r'^dafuweng$', 'summerManagement.views.dafuweng',name='dafuweng'),
    url(r'^getUserInfo$', 'summerManagement.views.getUserInfo',name='getUserInfo'),
    
    
    )
