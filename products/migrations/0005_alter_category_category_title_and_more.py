# Generated by Django 4.2.5 on 2023-10-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_category_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_title",
            field=models.CharField(max_length=30, verbose_name="Catéguorie"),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_title",
            field=models.CharField(max_length=30, verbose_name="Nom du produit"),
        ),
    ]
