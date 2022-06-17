# Generated by Django 4.0.3 on 2022-06-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QrCodeApp', '0004_qrcode_delete_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='get_email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]