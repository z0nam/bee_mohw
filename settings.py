from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    {
        "name": "smoking_cessation_clinic",
        "display_name": "금연클리닉 등록카드",
        "num_demo_participants": 1,
        "app_sequence": [
            "pre_test",
        ]
    },
    {
        "name": "pre_test",
        "display_name": "사전검사",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "pre_test_d",
            "stroop",

        ]
    },
    {
        "name": "post_test_normal",
        "display_name": "사후검사",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "post_test",
            "stroop",

        ]
    },
    {
        "name": "post_test_abnormal",
        "display_name": "사후검사 불참자용 설문",
        "num_demo_participants": 1,
        "app_sequence": [
            "post_test_d",
        ]
    },
    {
        "name": "online_survey",
        "display_name": "온라인 설문조사",
        "num_demo_participants": 1,
        "app_sequence": [
            "online_survey",

        ]
    }

]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ko'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'KRW'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'kzg55!*oiwbf4u$)y3+r90+&6j!&l@m-roa7!^et772ngl#gm!'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
