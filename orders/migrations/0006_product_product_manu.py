# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_manu',
            field=models.CharField(max_length=100, default=' '),
            preserve_default=False,
        ),
    ]
