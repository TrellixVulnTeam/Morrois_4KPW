# Generated by Django 2.2 on 2019-07-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_product_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Collection',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
