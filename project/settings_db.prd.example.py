# Database for production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hello',
        'USER': 'hello',
        'PASSWORD': 'hello',
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'OPTIONS': {
            # 'init_command': 'SET storage_engine={ENGINE},character_set_connection=utf8,collation_connection=utf8_unicode_ci,sql_mode=STRICT_TRANS_TABLES'.format(ENGINE=ENGINE),  # For mysql
        },
        'TEST': {
            'NAME': 'test_hello',
            # 'CHARSET': 'utf8',  # For mysql
            # 'COLLATION': 'utf8_unicode_ci',  # For mysql
        }
    }
}
