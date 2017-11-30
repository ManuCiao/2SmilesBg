# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='img/%Y/%m/%d', default=datetime.datetime(2017, 11, 28, 12, 41, 44, 343715, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
