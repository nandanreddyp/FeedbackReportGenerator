# tasks/report_tasks.py

from celery import shared_task

from reports.utils import generate_html_from_json, generate_pdf_from_json
from reports.models import Report

import time

@shared_task(bind=True)
def generate_report_task(self, type, json_data, filename):
    try:
        report = Report.objects.get(pk=filename)
        if type == 'PDF':
            filepath = generate_pdf_from_json(json_data, filename)
        elif type == 'HTML':
            filepath = generate_html_from_json(json_data, filename)
        else:
            raise ValueError("Invalid report type. Must be 'PDF' or 'HTML'.")
        # Update report status and file path
        report.file_path = filepath.replace('files/','')
        report.task_status = "COMPLETED"
        time.sleep(6)
        report.save()

    except Exception as e:
        try:
            report = Report.objects.get(pk=filename)
            report.status = "FAILED"
            report.save()
        except Exception:
            pass
        raise self.retry(exc=e, countdown=60, max_retries=3)
