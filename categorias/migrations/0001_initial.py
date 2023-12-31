# Generated by Django 4.2.4 on 2023-08-24 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="categoria",
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
                ("name_category", models.CharField(max_length=100, unique=True)),
                ("description", models.CharField(blank=True, max_length=100)),
                ("slug", models.CharField(max_length=100, unique=True)),
                ("cat_image", models.ImageField(upload_to="categoria")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="creado"),
                ),
                ("update", models.DateTimeField(auto_now=True, verbose_name="cambio")),
            ],
            options={
                "verbose_name": "nombre categoria",
                "verbose_name_plural": "nombres de categorias",
            },
        ),
    ]
