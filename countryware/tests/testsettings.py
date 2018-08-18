DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
SECRET_KEY = "un33k"
INSTALLED_APPS = ['countryware']
MIDDLEWARE_CLASSES = []
PRIORITY_COUNTRY_CODES = ['CA', 'US']