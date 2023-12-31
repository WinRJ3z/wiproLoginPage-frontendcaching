# Generated by Django 4.2.3 on 2023-08-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "authentication",
            "0002_alpineversions_kindleversions_postgresqlversions_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Business",
            fields=[
                ("quarter", models.FloatField(blank=True, null=True)),
                (
                    "ser_ref",
                    models.TextField(blank=True, db_column="SER_REF", null=True),
                ),
                ("industry_code", models.TextField(blank=True, null=True)),
                ("industry_name", models.TextField(blank=True, null=True)),
                ("filledjobs", models.IntegerField(blank=True, null=True)),
                ("filledjobsrevised", models.IntegerField(blank=True, null=True)),
                ("filledjobsdiff", models.IntegerField(blank=True, null=True)),
                (
                    "filledjobs_diff",
                    models.IntegerField(
                        blank=True, db_column="filledjobs%diff", null=True
                    ),
                ),
                ("total_earnings", models.IntegerField(blank=True, null=True)),
                ("totalearningsrevised", models.IntegerField(blank=True, null=True)),
                ("earningsdiff", models.IntegerField(blank=True, null=True)),
                (
                    "earnings_diff",
                    models.FloatField(blank=True, db_column="earnings%diff", null=True),
                ),
                (
                    "id",
                    models.IntegerField(blank=True, primary_key=True, serialize=False),
                ),
            ],
            options={"db_table": "business", "managed": False,},
        ),
    ]
