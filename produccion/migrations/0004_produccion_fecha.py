# Generated by Django 5.0.6 on 2024-07-07 22:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_rename_hora_produccion_fechahora_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
