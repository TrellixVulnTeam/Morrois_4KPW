# Generated by Django 2.2 on 2019-12-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191218_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.TextField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
