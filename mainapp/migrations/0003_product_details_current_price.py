# Generated by Django 4.0.1 on 2022-06-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_businessman_details_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='current_price',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=100),
            preserve_default=False,
        ),
    ]