import os
import sys

# Add your project directory to the sys.path
project_home = '/home/farbee9258/social-media-api'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'  # matches your settings.py inside config folder

# Activate your virtualenv
activate_this = '/home/farbee9258/.virtualenvs/social-media-api/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Serve Django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
