# Generated by Django 4.2.15 on 2024-08-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produto",
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
                ("nome", models.CharField(max_length=255)),
                ("codigo", models.CharField(max_length=50, unique=True)),
                ("descricao", models.TextField()),
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
