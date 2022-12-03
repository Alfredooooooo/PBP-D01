# Generated by Django 4.1 on 2022-11-01 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangwishlist',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='barangwishlist',
            name='deskripsi',
            field=models.TextField(max_length=50),
        ),
    ]
