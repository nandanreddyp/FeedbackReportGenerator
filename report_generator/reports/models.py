from django.db import models

# Create your models here.

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.CharField(max_length=255, db_index=True)
    task_status = models.CharField(max_length=20, default="PENDING")
    report_type = models.CharField(
        max_length=10,
        choices=[("HTML", "HTML"), ("PDF", "PDF")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.report_type} Report - {self.task_id}"