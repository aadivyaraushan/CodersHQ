# Generated by Django 3.2.11 on 2022-01-28 13:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_auto_20220128_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='prize_pool',
            field=models.IntegerField(default=0, verbose_name='Total prize pool'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='reward',
            field=ckeditor.fields.RichTextField(default='1'),
            preserve_default=False,
        ),
    ]
