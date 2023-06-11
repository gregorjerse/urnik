# Generated by Django 4.2.2 on 2023-06-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("friprosveta", "0004_activity_ready_to_schedule"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="cycles_on_site",
            field=models.IntegerField(
                blank=True,
                default=None,
                help_text="Koliko ciklov zelim izvajati na FRI",
                null=True,
                verbose_name="Cikli na FRI",
            ),
        ),
    ]
