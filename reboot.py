__author__ = 'coleman'

# TODO make this more Pythonic, avoid using os.system()


import os
from subprocess import Popen
from django.core.management import setup_environ, call_command
from gbots import settings

setup_environ(settings)

print '\nHardcoded dumpdata command:'
print "./manage.py dumpdata scraping dynamic_scraper --indent=2 > fixtures/starter.json\n"


decision = raw_input('Overwrite fixture? yes/no: ')
if decision == 'yes' or '':
    os.system("./manage.py dumpdata scraping dynamic_scraper --indent=2 > fixtures/starter.json")
else:
    print 'Latest database not saved to fixture.\n'

# trash old database and create new one
os.system("rm db/gabybots.sqlite")
os.system("./manage.py syncdb --noinput")

# migrate
os.system("./manage.py migrate")

# load the fixtures. This will have ALL our scrapers.
print '\nLoading the fixtures. These are our scrapers.'
os.system("./manage.py loaddata ./fixtures/starter.json")



# create superuser
print "\n Creating superuser 'admin' with password 'testing123'"
from django.contrib.auth.models import User
User.objects.create_superuser(username='admin', email='admin@example.com', password='testing123')



