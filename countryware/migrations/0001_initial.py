# Generated by Django 2.0.8 on 2018-08-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(help_text='Country code', max_length=3, primary_key=True, serialize=False, verbose_name='Code')),
                ('name', models.CharField(blank=True, help_text='Country name (english)', max_length=60, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
