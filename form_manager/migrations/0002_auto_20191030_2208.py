# Generated by Django 2.2.6 on 2019-10-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackform',
            name='id',
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='form_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_name',
            field=models.CharField(max_length=50),
        ),
    ]