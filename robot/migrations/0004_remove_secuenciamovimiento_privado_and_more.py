# Generated by Django 5.1.1 on 2024-10-24 07:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("robot", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="secuenciamovimiento",
            name="privado",
        ),
        migrations.RemoveField(
            model_name="secuenciamovimiento",
            name="usuario",
        ),
    ]