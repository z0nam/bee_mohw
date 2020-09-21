from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class post_test_1(Page):
    form_model = 'player'
    form_fields = [
        'num_post_not',
    ]


class post_test_2(Page):
    form_model = 'player'
    form_fields = [
        'action_strengthening_prop_category',
        'smoking_desire_decrease_lickert',
        'post_smoking_cessation_health_status',
        'post_smoking_cessation_stress_metirc',
        'smoking_cessation_practice_plan_change',
        'sa_1',
        'sa_2',
        'sa_3',
        'sa_4',
        'sa_5',
        'sa_6',
        'sa_7',
        'sa_8',
        'sa_9',
        'se_1',
        'se_2',
        'reason_for_failure_to_continue_quitting_smoking',
        'so_1',
        'so_2',
        'so_3',
        'so_4',
        'so_5',
        'so_6',
        'cas_1',
        'cas_2',
        'cas_3',
        'cas_4',
        'cas_5',
        'cas_6',
        'cas_7',
        'ef_1',
        'ef_2',
        'ef_3',
        'ef_4',
        'ef_5',
        'ef_6',
        'ef_7',
        'ef_8',
        'ef_9',
        'ef_10',
    ]

    def vars_for_template(self):
        return self.player.vars_for_template()

    def is_displayed(self):
        return self.player.num_post_not == 1


class post_test_3(Page):
    form_model = 'player'
    form_fields = [
        'TERMINATION',
        'termination_reason',
        'text_field',
    ]


page_sequence = [post_test_1, post_test_2, post_test_3]
