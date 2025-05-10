from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assignment/html', views.GenerateHtmlReportView.as_view(), name='generate_html_report'),
    path('assignment/html/<str:task_id>', views.GenerateHtmlReportView.as_view(), name='generate_html_report'),
    path('assignment/pdf', views.GeneratePdfReportView.as_view(), name='generate_pdf_report'),
    path('assignment/pdf/<str:task_id>', views.GeneratePdfReportView.as_view(), name='generate_pdf_report'),
]