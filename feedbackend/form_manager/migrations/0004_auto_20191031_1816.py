# Generated by Django 2.2.6 on 2019-10-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_manager', '0003_auto_20191031_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackform',
            name='form_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
