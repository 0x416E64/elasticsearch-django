# Generated by Django 2.0.5 on 2018-08-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch_django', '0007_update_json_field_encoders'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquery',
            name='search_terms',
            field=models.CharField(
                blank=True,
                help_text='Free text search terms used in the query, stored for easy reference.',
                max_length=400
            ),
        ),
    ]
