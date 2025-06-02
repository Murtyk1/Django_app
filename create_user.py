import os
import django
from dotenv import load_dotenv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_prices.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='murat').exists():
    User.objects.create_superuser(
        username= os.getenv ('DJANGO_SUPERUSER_USERNAME'),
        email= os.getenv ('DJANGO_SUPERUSER_EMAIL'),
        password= os.getenv  ('DJANGO_SUPERUSER_PASSWORD')
    )
    print("Суперпользователь создан")
else:
    print("Пользователь уже существует")
