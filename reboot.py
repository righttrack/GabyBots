__author__ = 'coleman'

import os


# trash old database and create new one
os.system("rm db/gabybots.sqlite")
os.system("./manage.py syncdb --noinput")

# migrate
os.system("./manage.py migrate")

# load the fixtures. This will have ALL our scrapers.
print 'Loading the fixtures. These are our scrapers.'
os.system("./manage.py loaddata fixtures/starter.json")

# create superuser
os.sysconf("./manage.py createsuperuser --username=coleman --email=coleman.mcfarland@gmail.com")

