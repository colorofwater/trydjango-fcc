# Generated by Django 2.0.7 on 2019-12-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191228_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=True),
            preserve_default=False,
        ),
    ]
