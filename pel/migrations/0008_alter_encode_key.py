# Generated by Django 4.1.3 on 2023-03-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pel', '0007_decode_key_encode_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encode',
            name='key',
            field=models.CharField(default=None, max_length=6),
        ),
    ]
