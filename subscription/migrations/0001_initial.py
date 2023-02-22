# Generated by Django 4.1.7 on 2023-02-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('endpoint', models.CharField(max_length=1024, verbose_name='subscriber_end_point')),
                ('public_key', models.CharField(max_length=1024, verbose_name='subscriber_public_key')),
                ('auth_key', models.CharField(max_length=1024, verbose_name='subscriber_auth_key')),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('email', models.CharField(blank=True, default='', max_length=64)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'subscriber',
                'verbose_name_plural': 'subscribers',
                'db_table': 'subscriber',
            },
        ),
    ]
