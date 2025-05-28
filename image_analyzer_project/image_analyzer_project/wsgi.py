# 2025-04-22
#yeliz irfan
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_analyzer_project.settings')

application = get_wsgi_application()
