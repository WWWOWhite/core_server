# Generated by Django 4.0 on 2024-05-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entitymanage', '0003_remove_kgcparamtertable_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enitytable',
            name='entity_port',
        ),
        migrations.AddField(
            model_name='enitytable',
            name='entity_listening_port',
            field=models.IntegerField(null=True, verbose_name='entity listening port'),
        ),
        migrations.AddField(
            model_name='enitytable',
            name='entity_sending_port',
            field=models.IntegerField(null=True, verbose_name='entity sending port'),
        ),
        migrations.AlterField(
            model_name='enitytable',
            name='entity_ip',
            field=models.GenericIPAddressField(verbose_name='entity ip'),
        ),
    ]