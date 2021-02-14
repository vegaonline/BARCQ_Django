# Generated by Django 3.1.3 on 2020-12-10 14:31

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_savedcircuit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SavedCircuit',
        ),
        migrations.AddField(
            model_name='customer',
            name='circuit',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]