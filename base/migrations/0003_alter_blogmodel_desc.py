# Generated by Django 4.1.4 on 2022-12-10 10:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_blogmodel_desc_alter_blogmodel_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogmodel",
            name="desc",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
