# Generated by Django 4.0.1 on 2022-06-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_newsstory_image_newsstory_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.CharField(default='https://i.picsum.photos/id/1040/4496/3000.jpg?hmac=kvZONlBpTcZ16PuE_g2RWxlicQ5JKVq2lqqZndfafBY', max_length=300),
        ),
    ]
