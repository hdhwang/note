# Generated by Django 3.2.7 on 2021-09-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20210818_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='ip',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
