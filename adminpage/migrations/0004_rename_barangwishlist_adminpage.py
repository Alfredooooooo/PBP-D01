# Generated by Django 4.1 on 2022-11-02 08:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminpage', '0003_alter_barangwishlist_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BarangWishlist',
            new_name='AdminPage',
        ),
    ]
