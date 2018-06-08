# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除记录')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='用户密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('is_active', models.BooleanField(default=False, verbose_name='激活状态')),
            ],
            options={
                'db_table': 's_user_account',
            },
        ),
    ]
