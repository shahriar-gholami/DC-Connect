# Generated by Django 4.2.8 on 2025-05-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_alter_interface_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='OuterEndPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('path', models.ManyToManyField(blank=True, null=True, to='info.path')),
            ],
        ),
    ]
