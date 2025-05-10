from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from reports.models import Report
from reports.utils import validate_json, generate_html_from_json, generate_pdf_from_json

from tasks.report_tasks import generate_report_task

import time, json
import secrets

# Create your views here.

def index(request):
    recent_reports = Report.objects.order_by('-created_at')[:5]
    return render(request, template_name='index.html', context={'recent_reports': recent_reports}, status=200)

class GenerateHtmlReportView(View):
    """
    View to generate a report.
    """
    def get(self, request, task_id=None, *args, **kwargs):
        if task_id is None:
            return render(request, template_name='upload.html', context={'jsonData':jsonData, 'uploadType': 'html'}, status=200)
        report = Report.objects.filter(task_id=task_id).first()
        return render(request, template_name='report.html', context={'report': report}, status=200)

    def post(self, request, task_id=None, *args, **kwargs):
        if task_id is not None: task_id = None
        time.sleep(3) # Simulate a long-running task
        body_data = json.loads(request.body)
        jsondata = json.loads(body_data.get('jsondata', ''))
        if not validate_json(jsondata):
            raise ValueError("Invalid JSON data")
        report = Report.objects.create(report_type='HTML')
        task_info = generate_report_task.delay('HTML', jsondata, filename=report.id)
        report.task_id = task_info.id
        report.save()
        return JsonResponse({"task_id": task_info.id, "message": "Task created!"}, status=200)

class GeneratePdfReportView(View):
    """
    View to generate a PDF report.
    """
    def get(self, request, task_id=None, *args, **kwargs):
        if task_id is None:
            return render(request, template_name='upload.html', context={'jsonData':jsonData, 'uploadType': 'pdf'}, status=200)
        report = Report.objects.filter(task_id=task_id).first()
        return render(request, template_name='report.html', context={'report': report}, status=200)

    def post(self, request, task_id=None, *args, **kwargs):
        if task_id is not None: task_id = None
        # time.sleep(3)
        body_data = json.loads(request.body)
        jsondata = json.loads(body_data.get('jsondata', ''))
        if not validate_json(jsondata):
            raise ValueError("Invalid JSON data")
        report = Report.objects.create(report_type='PDF')
        task_info = generate_report_task.delay('PDF', jsondata, filename=report.id)
        report.task_id = task_info.id
        report.save()
        return JsonResponse({"task_id": task_info.id, "message": "Task created!"}, status=200)

jsonData = '''
{
    "namespace": "ns_example",
    "student_id": "00a9a76518624b02b0ed57263606fc26",
    "events": [
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:04:55.939000+00:00",
            "unit": "17"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:05:27.027000+00:00",
            "unit": "17"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:05:56.155000+00:00",
            "unit": "17"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:06:21.131000+00:00",
            "unit": "17"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:06:42.786000+00:00",
            "unit": "17"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:06:52.228000+00:00",
            "unit": "17"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 03:06:53.025000+00:00",
            "unit": "17"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:09:03.787000+00:00",
            "unit": "17"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:25:17.781000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:26:18.605000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:26:48.110000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:27:18.011000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:28:18.226000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:28:48.329000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:29:17.690000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:29:22.741000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:29:57.637000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:29:59.248000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:30:35.805000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:30:59.816000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:31:41.130000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:31:43.916000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:32:19.551000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:32:26.550000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:33:03.876000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:33:23.044000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:33:35.024000+00:00",
            "unit": "6"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 02:33:35.861000+00:00",
            "unit": "6"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:35:16.158000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:35:45.855000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:36:15.507000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:36:45.721000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:37:16.185000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:38:18.883000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:38:45.154000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:38:47.435000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:38:58.194000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:39:34.118000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:40:48.809000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:41:11.028000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:41:34.285000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:41:43.499000+00:00",
            "unit": "7"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 02:41:44.528000+00:00",
            "unit": "7"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:43:54.835000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:44:26.539000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:45:27.207000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:45:55.695000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:46:25.357000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:46:50.984000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:47:01.954000+00:00",
            "unit": "10"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 02:47:02.702000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:47:12.078000+00:00",
            "unit": "10"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 02:47:12.886000+00:00",
            "unit": "10"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:47:55.067000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:48:24.036000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:48:54.440000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:49:25.614000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:49:53.119000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:50:25.253000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:50:52.978000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:51:24.925000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:51:24.936000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:52:00.927000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:52:38.848000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:52:51.456000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:53:29.377000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:53:32.183000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:54:01.510000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:54:29.011000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:54:38.183000+00:00",
            "unit": "12"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 02:54:38.928000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:54:49.162000+00:00",
            "unit": "12"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 02:54:49.959000+00:00",
            "unit": "12"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:58:05.234000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:58:36.547000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:59:05.213000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 02:59:35.762000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:00:06.099000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:00:35.901000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:01:36.505000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:02:37.620000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:02:46.697000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:03:13.362000+00:00",
            "unit": "14"
        },
        {
            "type": "saved_code",
            "created_time": "2024-07-21 03:03:25.660000+00:00",
            "unit": "14"
        },
        {
            "type": "submission",
            "created_time": "2024-07-21 03:03:26.568000+00:00",
            "unit": "14"
        }
    ]
}
'''