# Generated by Django 5.0.2 on 2024-06-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InvestmentOptimization",
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
                ("email", models.EmailField(max_length=254)),
                (
                    "lifestyle_risk",
                    models.CharField(
                        choices=[("low", "Low"), ("mid", "Mid"), ("high", "High")],
                        max_length=4,
                    ),
                ),
                ("expected_annual_roi", models.IntegerField()),
                ("monthly_investment", models.FloatField()),
                ("current_age", models.IntegerField()),
                ("retirement_age", models.IntegerField()),
                ("annual_salary", models.FloatField()),
                ("monthly_expenses", models.FloatField()),
                ("savings", models.FloatField()),
                ("principal_amount", models.FloatField()),
                ("investment_period", models.IntegerField()),
            ],
        ),
    ]
