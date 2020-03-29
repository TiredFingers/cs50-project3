# Generated by Django 3.0.4 on 2020-03-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200314_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodaddition',
            name='big_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='foodaddition',
            name='small_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='plate',
            name='big_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='plate',
            name='small_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]