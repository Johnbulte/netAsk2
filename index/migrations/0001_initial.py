# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-25 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('upwd', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'db_table': 'user',
                'verbose_name': '用户',
            },
        ),
    ]
