# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class SummerUserInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    u_id = models.IntegerField(blank=True, null=True)
    coin = models.CharField(max_length=8, blank=True)
    now_position = models.CharField(max_length=4, blank=True)
    last_play_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'summer_user_info'
