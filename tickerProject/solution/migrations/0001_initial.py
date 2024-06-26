# Generated by Django 4.2.8 on 2024-02-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StockData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symbol", models.CharField(max_length=10)),
                ("date", models.DateField()),
                ("open", models.DecimalField(decimal_places=2, max_digits=10)),
                ("high", models.DecimalField(decimal_places=2, max_digits=10)),
                ("low", models.DecimalField(decimal_places=2, max_digits=10)),
                ("close", models.DecimalField(decimal_places=2, max_digits=10)),
                ("volume", models.BigIntegerField()),
            ],
            options={"unique_together": {("symbol", "date")},},
        ),
    ]
