# Generated by Django 4.0.4 on 2022-05-17 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_alter_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipoProd',
            field=models.IntegerField(choices=[[0, 'ninguno'], [1, 'Cuerdas'], [2, 'Percusión'], [3, 'Amplificadores'], [4, 'Accesorios']], null=True),
        ),
    ]