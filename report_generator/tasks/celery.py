# tasks/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'report_generator.settings')

# Initialize Celery application with your project name
app = Celery('tasks')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks within the 'tasks' app
app.autodiscover_tasks(lambda: ['tasks'])