# Database for production

# import psycopg2.extensions


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hello',
        'USER': 'hello',
        'PASSWORD': 'hello',
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'OPTIONS': {
            # 'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
        },
        'TEST': {
            'NAME': 'test_hello',
            # 'CHARSET': 'utf8',  # For mysql
            # 'COLLATION': 'utf8_unicode_ci',  # For mysql
        }
    }
}
