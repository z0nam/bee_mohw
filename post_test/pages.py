from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class post_test(Page):
    form_model = 'player'
    form_fields = [
        'behavior_strengthening_material_barcode',
        # 'participant_name',
        # 'organization_type',
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
        'TERMINATION',
        'termination_reason',
        'text_field',
    ]

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [post_test]
