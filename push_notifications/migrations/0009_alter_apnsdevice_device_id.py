# Generated by Django 3.2.9 on 2022-01-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0008_webpush_add_edge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='device_id',
            field=models.UUIDField(blank=True, db_index=True, help_text='UUID / UIDevice.identifierForVendor()', null=True, verbose_name='Device ID'),
        ),
    ]