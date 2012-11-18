from gbots.settings import *

NOSE_ARGS = [
    '--with-fixture-bundling',
#    '--with-doctest',  # disabled because this causes the tests to take WAY to long
]

DATABASES = {
    'default': {
        # postgresql_psycopg2, postgresql, mysql, sqlite3 or oracle
        'ENGINE': 'django.db.backends.sqlite3',
        # Path to database file (if using sqlite3)
        'NAME': ':memory:', # Use an in-memory database
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}
