GabyBots
========

Awesome Web-crawling Robotz

Installation
============

1. Create a python virtual environment (optional, but recommended)

        $ python -m virtualenv gpython

2. Activate the virtual environment (you have to do this for every terminal you wish to run GabyBots in)

        $ source ./gpython/bin/activate

3. Download the required python packages

        $ pip install -r requirements.txt

4. Create your database

        $ ./manage.py syncdb
        $ ./manage.py migrate

