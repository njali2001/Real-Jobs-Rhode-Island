# Generated by Django 2.0.6 on 2018-06-19 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20180619_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector_partnerships',
            name='plan_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='sector_partnerships',
            name='organization_link',
            field=models.URLField(null=True),
        ),
    ]