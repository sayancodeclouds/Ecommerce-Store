# Generated by Django 5.0 on 2024-01-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_orderupdate_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]