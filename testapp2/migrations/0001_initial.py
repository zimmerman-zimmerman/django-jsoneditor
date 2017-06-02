# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-02 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsoneditor.fields.postgres_jsonfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_django_jsonfield', jsoneditor.fields.postgres_jsonfield.JSONField(blank=True, help_text=b'Test JSON editor for the django postgres-specific JSONField', null=True, verbose_name=b'Test JSON')),
            ],
        ),
        migrations.CreateModel(
            name='TestSubModel1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_inline_json_field', jsoneditor.fields.postgres_jsonfield.JSONField(blank=True, help_text=b'Test JSON editor for the django postgres-specific JSONField', null=True, verbose_name=b'Test JSON')),
                ('par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp2.TestModel')),
            ],
        ),
        migrations.CreateModel(
            name='TestSubModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_inline_json_field', jsoneditor.fields.postgres_jsonfield.JSONField(blank=True, help_text=b'Test JSON editor for the django postgres-specific JSONField', null=True, verbose_name=b'Test JSON')),
                ('par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp2.TestModel')),
            ],
        ),
    ]
