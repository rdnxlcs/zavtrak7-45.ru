import os
import sys

try:
  sys.path.remove('/usr/lib/python3/dist-packages')
except:
  pass

sys.path.append('/home/c/centromebel/zavtrak745/public_html/zavtrak745/')
sys.path.append('/home/c/centromebel/zavtrak745/venv/lib/python3.10/site-packages/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZK.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()