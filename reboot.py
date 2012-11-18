#!/usr/bin/env python

__author__ = 'coleman'

# TODO make this more Pythonic, avoid using os.system()
# TODO write fixture to temp file and add in checks to avoid blowing away filled-out fixtures!

# This script saves fixtures (or thows away your changes) and runs syncdb, creating a superuser for the sqlite3 database
# Superuser is 'admin', password 'testing123'


import os
from subprocess import Popen
from django.core.management import setup_environ, call_command
from gbots import settings
from gbots.settings import PROJECT_ROOT

setup_environ(settings)

INITIAL_DATA = "gbots/scraping/fixtures/starter.json"

print '\nPROJECT_ROOT variable:' + PROJECT_ROOT
print "./manage.py dumpdata scraping dynamic_scraper --indent=2 > " + PROJECT_ROOT + "/" + INITIAL_DATA + "\n"


decision = raw_input('Overwrite fixture? yes/no: ')
if decision == 'yes' or '':
    os.system(PROJECT_ROOT + "/manage.py dumpdata scraping dynamic_scraper --indent=2 > " + PROJECT_ROOT + "/" + INITIAL_DATA)
else:
    print 'Latest database not saved to fixture.\n'

# trash old database and create new one
os.system("rm " + PROJECT_ROOT + "/db/gabybots.sqlite")
os.system(PROJECT_ROOT + "/manage.py syncdb --noinput")

# migrate
os.system(PROJECT_ROOT + "/manage.py migrate")

# load the fixtures. This will have ALL our scrapers.
print '\nLoading the fixtures. These are our scrapers.'
os.system(PROJECT_ROOT + "/manage.py loaddata " + PROJECT_ROOT + "/" + INITIAL_DATA)



# create superuser
print "\n\n Creating superuser 'admin' with password 'testing123'"
from django.contrib.auth.models import User
User.objects.create_superuser(username='admin', email='admin@example.com', password='testing123')



