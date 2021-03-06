# Generated by Django 2.0.5 on 2018-05-28 14:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ART_MANIAC_APP', '0002_auto_20180528_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
