# Generated by Django 2.2.9 on 2022-03-02 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estados', '0002_auto_20220302_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
