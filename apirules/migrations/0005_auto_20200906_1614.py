# Generated by Django 2.2.15 on 2020-09-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirules', '0004_vendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='foto',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
