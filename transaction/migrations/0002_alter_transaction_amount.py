# Generated by Django 5.0.6 on 2024-07-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.DecimalField(decimal_places=18, max_digits=50),
        ),
    ]