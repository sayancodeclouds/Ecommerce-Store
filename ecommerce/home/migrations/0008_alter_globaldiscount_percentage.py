# Generated by Django 5.0 on 2024-01-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_globaldiscount_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globaldiscount',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
