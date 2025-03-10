# Generated by Django 5.0.2 on 2024-06-05 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InvestmentBasket",
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
                ("name", models.CharField(max_length=255)),
                ("volatility", models.FloatField()),
                ("cagr", models.FloatField(help_text="Compound Annual Growth Rate")),
                ("manager_description", models.TextField()),
                ("minimum_investment_amount", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Holding",
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
                ("asset_name", models.CharField(max_length=255)),
                ("distribution_percentage", models.FloatField()),
                (
                    "basket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="holdings",
                        to="aianalysis.investmentbasket",
                    ),
                ),
            ],
        ),
    ]
