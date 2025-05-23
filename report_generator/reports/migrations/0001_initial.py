# Generated by Django 5.2 on 2025-05-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task_id', models.CharField(db_index=True, max_length=255)),
                ('task_status', models.CharField(default='PENDING', max_length=20)),
                ('report_type', models.CharField(choices=[('HTML', 'HTML'), ('PDF', 'PDF')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
