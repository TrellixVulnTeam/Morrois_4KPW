# Generated by Django 2.2 on 2019-10-24 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190803_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Collection',
            field=models.CharField(choices=[('Alliterative Morte Arthur', 'Art 8: Alliterative Morte Arthur'), ('Octavian', 'Art 10: Octavian'), ('Isumbras', 'Art 11: Isumbras'), ('Sir Degreuant', 'Art 15: Sir Degreuant')], default='Alliterative Morte Arthur', max_length=50),
        ),
    ]