# Generated by Django 3.1.1 on 2020-09-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200925_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data',
            field=models.DateField(null=True),
        ),
    ]