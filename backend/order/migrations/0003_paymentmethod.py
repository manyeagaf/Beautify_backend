# Generated by Django 4.0.4 on 2022-10-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=150)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]