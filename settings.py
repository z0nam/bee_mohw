from os import environ
import os

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

SESSION_CONFIGS = [
    {
        "name": "pre_test_wave2",
        "display_name": "사전검사 (wave 2)",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "pre_test_w2",
            "pre_test_d",
            "stroop",
            "ending",
        ]
    },
    {
        "name": "post_test_normal",
        "display_name": "사후검사",
        "num_demo_participants": 1,
        "app_sequence": [
            # "introduction",
            "post_test",
            "stroop",
            "ending",
        ]
    },
    {
        "name": "post_test_abnormal",
        "display_name": "사후검사 불참자용 설문(연구자 입력용)",
        "num_demo_participants": 1,
        "app_sequence": [
            "post_test_d",
        ]
    },
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
# to set password, $heroku config:set OTREE_ADMIN_PASSWORD="password_you_want"

DEMO_PAGE_TITLE = "흡연 및 금연 경험에 관한 연구 (보건복지부)"

DEMO_PAGE_INTRO_HTML = """ 
<h5> 주관: 한국행동경제학연구소, 금연학회 </h6>
<table>
    <tr>
        <td width="50%"><img width="100%" src="https://kberi.files.wordpress.com/2020/10/kberi_logo200.jpg"></td>
        <td width="50%"><img width="90%" src="http://www.ksrnt.org/img/main/logo_2018.png"></td>
    </tr>
</table>
"""

SECRET_KEY = 'kzg55!*oiwbf4u$)y3+r90+&6j!&l@m-roa7!^et772ngl#gm!'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
