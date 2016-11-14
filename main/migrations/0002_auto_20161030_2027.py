# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subfield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('grade', models.ForeignKey(to='main.Grade')),
            ],
        ),
        migrations.RemoveField(
            model_name='papersheet',
            name='grade',
        ),
        migrations.AddField(
            model_name='papersheet',
            name='subfield',
            field=models.ForeignKey(default=1, to='main.Subfield'),
            preserve_default=False,
        ),
    ]
