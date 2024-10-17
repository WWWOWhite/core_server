# Generated by Django 4.0 on 2024-04-12 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0001_initial'),
        ('softwaremanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterSoftwareLocationTable',
            fields=[
                ('rlsoftwarelocation_index', models.AutoField(primary_key=True, serialize=False, verbose_name='rsoftware index')),
                ('node_ip', models.CharField(max_length=15, verbose_name='node ip')),
                ('entity_ip', models.CharField(max_length=15, verbose_name='entity ip')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterSoftwareTable',
            fields=[
                ('rsoftware_id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='rsoftware_id')),
                ('rsoftware_name', models.CharField(max_length=20, verbose_name='rsoftware name')),
                ('rsoftware_path', models.CharField(max_length=50, verbose_name='rsoftware path')),
                ('rsoftware_version', models.CharField(max_length=50, verbose_name='rsoftware version')),
                ('rsoftware_desc', models.TextField(null=True, verbose_name='rsoftware descryption')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermanage.usertable', verbose_name='user id')),
            ],
        ),
        migrations.RemoveField(
            model_name='softwarelocation',
            name='pc_ip',
        ),
        migrations.AddField(
            model_name='softwarelocation',
            name='entity_ip',
            field=models.CharField(default=0, max_length=15, verbose_name='entity ip'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='RegistSoftwareTable',
        ),
        migrations.AddField(
            model_name='registersoftwarelocationtable',
            name='rsoftware_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='softwaremanage.registersoftwaretable', verbose_name='rsoftware id'),
        ),
    ]