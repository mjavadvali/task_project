from celery import shared_task
from ..products.utils import generate_csv

@shared_task
def schedule_csv_generation():
    generate_csv()