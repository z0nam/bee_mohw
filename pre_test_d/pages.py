from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class pre_test_d(Page):
    form_model = 'player'
    form_fields = [
        'behavior_strengthening_material_barcode',
        'self_reported_health_status',
        'stress_metric_self_reported',
        'afterward_smoking_cessation_yesno',
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
        'gender',
        'birth_year',
        'region',
        'region_size',
        'marriage',
        'job_position',
        'firm_type',
        'firm_type_op',
        'firm_size',
        'household_income',
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


page_sequence = [pre_test_d]
