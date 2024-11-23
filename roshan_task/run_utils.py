import os
import django
import sys
import django

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Replace 'your_project_name' with your Django project name
django.setup()

# Import and run your utility functions
from products.utils import generate_csv

if __name__ == '__main__':
    generate_csv()
    print("CSV file generated successfully!")
