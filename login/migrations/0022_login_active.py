# Generated by Django 4.0.5 on 2022-07-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_remove_login_active_seassion_remove_login_c_k_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='active',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]