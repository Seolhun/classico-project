# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('hits', models.IntegerField(default=0)),
                ('commentDepth', models.IntegerField(default=0)),
                ('fileDepth', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('hates', models.IntegerField(default=0)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('modifiedBy', models.CharField(max_length=200, null=True)),
                ('modifiedDate', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('approvedComment', models.BooleanField(default=False)),
                ('depth', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('hates', models.IntegerField(default=0)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('modifiedBy', models.CharField(max_length=200, null=True)),
                ('modifiedDate', models.DateTimeField(blank=True, null=True)),
                ('boardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classico_board.Board')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('originName', models.CharField(max_length=200)),
                ('savedName', models.CharField(max_length=200)),
                ('size', models.IntegerField(default=0)),
                ('path', models.FilePathField(default=0)),
                ('file', models.FileField(default=0, upload_to='')),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('modifiedBy', models.CharField(max_length=200, null=True)),
                ('modifiedDate', models.DateTimeField(blank=True, null=True)),
                ('boardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classico_board.Board')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]