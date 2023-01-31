# Generated by Django 4.0.4 on 2022-09-29 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='/sample.png', null=True, upload_to='', verbose_name='category image'),
        ),
        migrations.AlterField(
            model_name='media',
            name='img_url',
            field=models.ImageField(default='/sample.png', help_text='format: required, default-default.png', upload_to='', verbose_name='product image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='/sample.png', help_text='format: required, default-default.png', upload_to='', verbose_name='product image1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='/sample.png', help_text='format: required, default-default.png', null=True, upload_to='', verbose_name='product image2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, default='/sample.png', help_text='format: required, default-default.png', null=True, upload_to='', verbose_name='product image3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, default='//sample.png', help_text='format: required, default-default.png', null=True, upload_to='', verbose_name='product image4'),
        ),
    ]