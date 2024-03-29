# Generated by Django 5.0.2 on 2024-03-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_buzo_delete_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantalon',
            name='categoria',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pantalon',
            name='modelo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pantalon',
            name='nombreArticulo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pantalon',
            name='talle',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='remera',
            name='categoria',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='remera',
            name='modelo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='remera',
            name='nombreArticulo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='remera',
            name='talle',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
