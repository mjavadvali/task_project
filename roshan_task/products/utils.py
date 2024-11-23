import csv
import os
from datetime import datetime
# from django.db.models import F, Max
from products.models import Product
from collections import defaultdict

def get_most_daily_viewed_products_by_category():
    products = Product.objects.all()
    products_with_recent_hits = [
        {
            'product': product,
            'category': product.category,
            'hits_in_last_day': product.hit_count.hits_in_last(days=1)
        }
        for product in products
    ]

    category_hits = defaultdict(lambda: {'product': None, 'hits': 0})

    for item in products_with_recent_hits:
        category = item['category']
        hits = item['hits_in_last_day']
        if hits > category_hits[category]['hits']:
            category_hits[category] = {'product': item['product'], 'hits': hits}

    return category_hits.items()


def generate_csv():

    products = get_most_daily_viewed_products_by_category()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_path = f'media/reports/most_viewed_products_{timestamp}.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['دسته بندی', 'محصول', 'بازدید'])
        for category, data in products:
            writer.writerow([category, data['product'].title, data['hits']])
