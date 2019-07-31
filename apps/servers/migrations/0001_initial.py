# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-31 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('idcs', '0001_initial'),
        ('cabinet', '0002_auto_20190731_1730'),
        ('manufacturer', '0002_auto_20190731_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(db_index=True, help_text='ip\u5730\u5740', max_length=15, unique=True, verbose_name='ip\u5730\u5740')),
                ('netmask', models.CharField(help_text='\u5b50\u7f51\u63a9\u7801', max_length=15, verbose_name='\u5b50\u7f51\u63a9\u7801')),
                ('remark', models.CharField(help_text='\u5907\u6ce8', max_length=200, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'resources_ip',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u7f51\u5361\u8bbe\u5907\u540d', max_length=20, verbose_name='\u7f51\u5361\u8bbe\u5907\u540d')),
                ('mac', models.CharField(help_text='MAC\u5730\u5740', max_length=32, verbose_name='MAC\u5730\u5740')),
                ('remark', models.CharField(help_text='\u5907\u6ce8', max_length=200, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'resources_networkdevice',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(db_index=True, help_text='\u7ba1\u7406IP', max_length=15, unique=True, verbose_name='\u7ba1\u7406IP')),
                ('hostname', models.CharField(db_index=True, help_text='\u4e3b\u673a\u540d', max_length=20, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('cpu', models.CharField(help_text='CPU', max_length=50, verbose_name='CPU')),
                ('mem', models.CharField(help_text='\u5185\u5b58', max_length=32, verbose_name='\u5185\u5b58')),
                ('disk', models.CharField(help_text='\u78c1\u76d8', max_length=200, verbose_name='\u78c1\u76d8')),
                ('os', models.CharField(help_text='\u64cd\u4f5c\u7cfb\u7edf', max_length=50, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('sn', models.CharField(db_index=True, help_text='SN', max_length=50, verbose_name='SN')),
                ('rmt_card_ip', models.CharField(db_index=True, help_text='\u7ba1\u7406\u7ba1\u7406\u5361IP', max_length=15, unique=True, verbose_name='\u7ba1\u7406\u7ba1\u7406\u5361IP')),
                ('cabinet_position', models.CharField(help_text='\u673a\u67dc\u4f4d\u7f6e', max_length=20, null=True, verbose_name='\u673a\u67dc\u4f4d\u7f6e')),
                ('uuid', models.CharField(db_index=True, help_text='UUID', max_length=30, unique=True, verbose_name='UUID')),
                ('last_check', models.DateTimeField(auto_now=True, db_index=True, help_text='\u68c0\u6d4b\u65f6\u95f4', verbose_name='\u68c0\u6d4b\u65f6\u95f4')),
                ('remark', models.CharField(help_text='\u5907\u6ce8', max_length=200, null=True, verbose_name='\u5907\u6ce8')),
                ('cabinet', models.ForeignKey(help_text='\u6240\u5728\u673a\u67dc', null=True, on_delete=django.db.models.deletion.CASCADE, to='cabinet.Cabinet', verbose_name='\u6240\u5728\u673a\u67dc')),
                ('idc', models.ForeignKey(help_text='\u6240\u5728\u673a\u623f', null=True, on_delete=django.db.models.deletion.CASCADE, to='idcs.Idc', verbose_name='\u6240\u5728\u673a\u623f')),
                ('manufacturer', models.ForeignKey(help_text='\u5236\u9020\u5546', on_delete=django.db.models.deletion.CASCADE, to='manufacturer.Manufacturer', verbose_name='\u5236\u9020\u5546')),
                ('model_name', models.ForeignKey(help_text='\u670d\u52a1\u5668\u578b\u53f7', on_delete=django.db.models.deletion.CASCADE, to='manufacturer.ProductModel', verbose_name='\u670d\u52a1\u5668\u578b\u53f7')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'resources_server',
            },
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='host',
            field=models.ForeignKey(help_text='\u6240\u5728\u670d\u52a1\u5668', on_delete=django.db.models.deletion.CASCADE, to='servers.Server', verbose_name='\u6240\u5728\u670d\u52a1\u5668'),
        ),
        migrations.AddField(
            model_name='ip',
            name='device',
            field=models.ForeignKey(help_text='\u6240\u5728\u7f51\u5361', on_delete=django.db.models.deletion.CASCADE, to='servers.NetworkDevice', verbose_name='\u6240\u5728\u7f51\u5361'),
        ),
    ]
