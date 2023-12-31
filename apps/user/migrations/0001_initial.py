# Generated by Django 3.2 on 2023-07-30 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('bio', models.TextField(null=True)),
                ('present_work_space', models.CharField(max_length=100, null=True)),
                ('live_country', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
