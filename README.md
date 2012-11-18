GabyBots
========

Awesome Web-crawling Robotz


Installation
============

After you clone the repository, enter the directory and perform the following setup.

1. Create a python virtual environment (optional, but recommended)

        $ python -m virtualenv gpython

2. Activate the virtual environment (you have to do this for every terminal you wish to run GabyBots in)

        $ source ./gpython/bin/activate

3. Download the required python packages

        $ pip install -r requirements.txt

4. Create your database

        $ ./manage.py syncdb
        $ ./manage.py migrate

5. Add the default scrapers (you can use 'minimal' to create a database with no web sources)

        $ ./manage.py loaddata starter


Running A Spider
================

You can run the starter spider, which will scrape the Google News - World RSS Feed. First you must be in the gbots directory.

    $ cd gbots/

Then you can run scrapy.

    $ scrapy crawl google-news -a id=1

If you want it to add the scraped articles to the database, you would use:

    $ scrapy crawl google-news -a id=1 -a do_action=yes
