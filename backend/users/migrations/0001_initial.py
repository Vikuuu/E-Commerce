# Generated by Django 4.2.7 on 2023-11-09 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("first_name", models.CharField(max_length=255, null=True)),
                ("last_name", models.CharField(max_length=255, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserRole",
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
                (
                    "user_role",
                    models.CharField(
                        choices=[("C", "CUSTOMER"), ("S", "SELLER")], max_length=1
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentMethod",
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
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("CRD", "CREDIT AND DEBIT CARD"),
                            ("UPI", "UPI"),
                            ("COD", "CASH ON DELIVERY"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("street_address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("state_province", models.CharField(max_length=255)),
                ("postal_zip_code", models.CharField(max_length=9)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.userprofile",
                    ),
                ),
            ],
        ),
    ]
