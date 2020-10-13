from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class post_test_d(Page):
    form_model = 'player'
    form_fields = [
        'participant_name',
        'organization_type',
        'TERMINATION',
        'termination_reason',
        'text_field',
    ]


page_sequence = [post_test_d]
