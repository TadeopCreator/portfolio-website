# Generated by Django 4.2.4 on 2023-09-11 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(blank=True, upload_to="portfolio/images"),
        ),
    ]