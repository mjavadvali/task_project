from celery import shared_task
from django.core.management import call_command




@shared_task
def csv_generate_task():
    call_command("csv_report",)
