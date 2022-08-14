# Generated by Django 4.1 on 2022-08-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="project",
            name="featured",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(blank=True, upload_to="portfolio/images"),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=150),
        ),
    ]
