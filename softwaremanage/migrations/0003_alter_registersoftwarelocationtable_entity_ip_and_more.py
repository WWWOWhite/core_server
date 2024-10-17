# Generated by Django 4.0 on 2024-05-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softwaremanage', '0002_registersoftwarelocationtable_registersoftwaretable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registersoftwarelocationtable',
            name='entity_ip',
            field=models.GenericIPAddressField(verbose_name='entity ip'),
        ),
        migrations.AlterField(
            model_name='registersoftwarelocationtable',
            name='node_ip',
            field=models.GenericIPAddressField(verbose_name='node ip'),
        ),
    ]