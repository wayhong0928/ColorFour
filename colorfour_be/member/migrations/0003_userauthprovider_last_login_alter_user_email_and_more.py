# Generated by Django 4.2 on 2024-09-16 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_delete_googleoauthtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauthprovider',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userauthprovider',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_providers', to=settings.AUTH_USER_MODEL),
        ),
    ]