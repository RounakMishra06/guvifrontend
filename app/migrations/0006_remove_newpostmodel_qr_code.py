# Generated by Django 4.0.6 on 2022-08-19 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_newpostmodel_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpostmodel',
            name='qr_code',
        ),
    ]
