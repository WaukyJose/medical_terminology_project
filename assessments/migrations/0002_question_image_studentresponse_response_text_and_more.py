# Generated by Django 5.1.2 on 2024-11-07 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
        migrations.AddField(
            model_name='studentresponse',
            name='response_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MCQ', 'Multiple Choice'), ('FIB', 'Fill-in-the-Blank'), ('TF', 'True/False'), ('SA', 'Short Answer'), ('MQ', 'Matching Questions'), ('OQ', 'Ordering Questions')], max_length=20),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='selected_option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assessments.option'),
        ),
    ]