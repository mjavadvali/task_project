from django.core.management.base import BaseCommand, CommandError
import csv
import os
from datetime import datetime
from products.utils import get_most_daily_viewed_products_by_category

class Command(BaseCommand):
    help = "This command is responsible for generating the most viewed products per category"


    def handle(self, *args, **options):
        
        products = get_most_daily_viewed_products_by_category()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = f'media/reports/most_viewed_products_{timestamp}.csv'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['دسته بندی', 'محصول', 'بازدید'])
            for category, data in products:
                writer.writerow([category, data['product'].title, data['hits']])


        self.stdout.write("The csv report created.")