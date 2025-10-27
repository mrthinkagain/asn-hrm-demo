import os
import sys
import webbrowser
import threading
from django.core.management import execute_from_command_line

def open_browser():
    webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horilla.settings')
    threading.Timer(3, open_browser).start()
    execute_from_command_line(['manage.py', 'runserver', '--noreload'])
