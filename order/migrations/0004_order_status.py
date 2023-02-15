# Generated by Django 4.0.4 on 2023-02-13 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_paymentmethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'pending'), (2, 'shipped'), (3, 'cancelled'), (4, 'delivered')], default=1),
        ),
    ]