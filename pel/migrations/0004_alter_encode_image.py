# Generated by Django 4.1.7 on 2023-03-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pel', '0003_alter_encode_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encode',
            name='image',
            field=models.ImageField(default='images/test2.png', upload_to='encoded/'),
        ),
    ]
