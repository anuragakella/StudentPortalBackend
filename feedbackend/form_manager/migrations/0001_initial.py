# Generated by Django 2.2.6 on 2019-10-30 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeid', models.CharField(max_length=10)),
                ('is_prof', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('question_type', models.CharField(choices=[('SLDR', 'Slider/ Rating'), ('BOOL', 'Boolean Question'), ('TEXT', 'Text Based Question'), ('MULC', 'Multiple Choice Question')], default='SLDR', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=30)),
                ('subject_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_manager.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_answer', models.TextField()),
                ('form_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_manager.Subject')),
                ('form_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='form_manager.Profile')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_manager.Question')),
            ],
        ),
    ]
