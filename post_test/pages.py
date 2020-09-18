from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class post_test(Page):
    form_model = 'player'
    form_fields = [
        'num_post_not',
        'post_action_strengthening_prop_category',
        'post_smoking_desire_decrease_lickert',
        'post_post_smoking_cessation_health_status',
        'post_post_smoking_cessation_stress_metirc',
        'post_smoking_cessation_practice_plan_change',
        'post_sa_1',
        'post_sa_2',
        'post_sa_3',
        'post_sa_4',
        'post_sa_5',
        'post_sa_6',
        'post_sa_7',
        'post_sa_8',
        'post_sa_9',
        'post_se_1',
        'post_se_2',
        'post_reason_for_failure_to_continue_quitting_smoking',
        'post_so_1',
        'post_so_2',
        'post_so_3',
        'post_so_4',
        'post_so_5',
        'post_so_6',
        'post_cas_1',
        'post_cas_2',
        'post_cas_3',
        'post_cas_4',
        'post_cas_5',
        'post_cas_6',
        'post_cas_7',
        'post_ef_1',
        'post_ef_2',
        'post_ef_3',
        'post_ef_4',
        'post_ef_5',
        'post_ef_6',
        'post_ef_7',
        'post_ef_8',
        'post_ef_9',
        'post_ef_10',
        'TERMINATION',
        'termination_reason',
        'text_field',

    ]

    def vars_for_template(self) -> dict:
        vars_to_return = {}
        vars_to_return['L5'] = [i[1] for i in Constants.L5_CHOICES]
        vars_to_return['L53'] = [i[1] for i in Constants.L53_CHOICES]
        vars_to_return['L54'] = [i[1] for i in Constants.L54_CHOICES]
        vars_to_return['L55'] = [i[1] for i in Constants.L55_CHOICES]
        vars_to_return['L56'] = [i[1] for i in Constants.L56_CHOICES]
        return vars_to_return


page_sequence = [post_test, ]
