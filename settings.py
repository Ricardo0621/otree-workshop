from os import environ

SESSION_CONFIGS = [
    dict(
       name='mi_dilema_del_prisionero',
       display_name="Mi Dilema del Prisionero",
       num_demo_participants=2,
       app_sequence=['mi_dilema_del_prisionero']
    ),
dict(
       name='mi_dilema_del_prisionero_re',
       display_name="Mi Dilema del Prisionero 2",
       num_demo_participants=2,
       app_sequence=['mi_dilema_del_prisionero_re']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'qk5lo89=8k*#01de8(4=g18%=j8py8gm9@+xs$&^-$wl!e#7#e'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
