# Generated by Django 4.0.4 on 2022-10-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(default='images/default.png', help_text=('format: required, default-default.png',), upload_to=''),
        ),
    ]
