# Generated by Django 3.2.3 on 2021-05-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_hospital_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hospital_url',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]