# Generated by Django 4.2.4 on 2023-10-20 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0005_alter_project_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="origin",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
