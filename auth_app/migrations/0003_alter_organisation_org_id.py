# Generated by Django 5.0.6 on 2024-07-06 12:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_rename_userid_user_user_id_user_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='org_id',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]