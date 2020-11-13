from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class BasicInfo(Page):
    form_model = 'player'
    form_fields = [
        'behavior_strengthening_material_barcode',
        'registration_type',
        'smoking_cessation_start_year',
        'smoking_cessation_start_month',
        'smoking_cessation_start_date',
        'support_service_registration_year',
        'support_service_registration_month',
        'support_service_registration_date',
        'smoking_cessation_resolution_year',
        'smoking_cessation_resolution_month',
        'smoking_cessation_resolution_date',
        'smoking_cessation_supporter_1',
        'smoking_cessation_supporter_2',
        'smoking_cessation_supporter_3',
        'smoking_cessation_supporter_4',
        'smoking_cessation_supporter_5',
        'smoking_cessation_supporter_6',
        'smoking_cessation_supporter_7',
        'smoking_cessation_supporter_8',
        'smoking_cessation_supporter_9',
        'smoking_cessation_supporter_10',
        'support_service_registration_source_1',
        'support_service_registration_source_2',
        'support_service_registration_source_3',
        'support_service_registration_source_4',
        'support_service_registration_source_5',
        'support_service_registration_source_6',
        'support_service_registration_source_7',
        'support_service_registration_source_8',
        'support_service_registration_source_9',
    ]


class HealthInfo(Page):
    form_model = 'player'
    form_fields = [
        'height',
        'weight',
        'waist_circumference',
        'carbon_monoxide',
        'systolic_blood_pressure',
        'diastolic_blood_pressure',
        'disease_history_1',
        'disease_history_2',
        'disease_history_3',
        'disease_history_4',
        'disease_history_5',
        'disease_history_6',
        'disease_history_7',
        'disease_history_8',
        'disease_history_9',
        'disease_history_10',
        'disease_history_11',
        'disease_history_12',
        'disease_history_13',
        'disease_history_14',
        'disease_history_15',
        'disease_history_16',
        'disease_history_17',
        'disease_history_18',
        'disease_history_19',
        'disease_history_20',
        'disease_history_21',
        'disease_history_22',
        'disease_history_23',
        'disease_history_24',
        'disease_history_25',
        'disease_history_26',
        'disease_history_27',
        'disease_history_28',
        'disease_history_29',
        'disease_history_30',
        'disease_history_31',
        'drug_in_use',
        'did_you_drink_within_the_last_one_year',
        'drinking_amount_per_drinking_outing',
        'drinking_frequency_per_week',
        'intense_workout_yes_no',
        'type_of_workout',
        'workout_frequency',
        'workout_minutes_per_time',
        'age_of_first_smoking',
        'avg_daily_smoking_amount_in_gaebi',
        'total_smoking_years',
        'nicotine_patch_adverse_effect',
        'nicotine_patch_adverse_effect_op',
        'tobacco_type_in_use_1',
        'tobacco_type_in_use_2',
        'tobacco_type_in_use_3',
        'tobacco_type_in_use_4',
        'tobacco_type_in_use_5',
        'tobacco_type_in_use_6',
        'tobacco_type_in_use_7',
        'tobacco_type_in_use_8',
        'tobacco_type_in_use_9',
        'tobacco_type_in_use_10',
        'tobacco_type_in_use_11',
        'tobacco_type_in_use_12',
        'tobacco_type_in_use_13',
        'medical_guarantee',
        'highest_schooling',
        'occupation',
        'occupation_op',
    ]


class SmokerEvaluation(Page):
    form_model = 'player'
    form_fields = [
        'within_last_one_year_smoking_cessation_tryout_yesno',
        'within_last_one_year_smoking_cessation_tryout_yesno_op_month',
        'within_last_one_year_smoking_cessation_tryout_yesno_op_days',
        'smoking_cessation_method_1',
        'smoking_cessation_method_2',
        'smoking_cessation_method_3',
        'smoking_cessation_method_4',
        'smoking_cessation_method_5',
        'smoking_cessation_method_6',
        'smoking_cessation_failure_reason_1',
        'smoking_cessation_failure_reason_2',
        'smoking_cessation_failure_reason_3',
        'smoking_cessation_failure_reason_4',
        'smoking_cessation_failure_reason_5',
        'smoking_cessation_failure_reason_6',
        'smoking_cessation_this_time_reason_primary',
        'smoking_cessation_this_time_reason_primary_op',
        'smoking_cessation_this_time_reason_secondary',
        'smoking_cessation_this_time_reason_secondary_op',
        'smoking_cessation_this_time_reason_tertiary',
        'smoking_cessation_this_time_reason_tertiary_op',
        'hardest_event_to_resist_smoking_desire_1',
        'hardest_event_to_resist_smoking_desire_2',
        'hardest_event_to_resist_smoking_desire_3',
        'hardest_event_to_resist_smoking_desire_4',
        'hardest_event_to_resist_smoking_desire_5',
        'hardest_event_to_resist_smoking_desire_6',
        'hardest_event_to_resist_smoking_desire_7',
        'hardest_event_to_resist_smoking_desire_8',
        'hardest_event_to_resist_smoking_desire_9',
        'hardest_event_to_resist_smoking_desire_10',
        'smoking_cessation_motivation',
        'smoking_cessation_confidence',
        'smoking_cessation_readiness',
    ]


class NicotineDependence(Page):
    form_model = 'player'
    form_fields = [
        'morning_smoking_time',
        'smoking_resistancy',
        'most_tasty_smoking_time',
        'how_many_gaebis_per_day',
        'morning_smoking_more_than_the_rest_of_day',
        'sick_all_day_still_smoking',
    ]

class SmokerType(Page):
    form_model = 'player'
    form_fields=[
        'st_1',
        'st_2',
        'st_3',
        'st_4',
        'st_5',
        'st_6',
        'st_7',
        'st_8',
        'st_9',
        'st_10',
        'st_11',
        'st_12',
        'st_13',
        'st_14',
        'st_15',
        'st_16',
        'st_17',
        'st_18',
        'st_19',
        'st_20',
        'st_21',
    ]


    def vars_for_template(self) -> dict:
        vars_to_return = {}
        vars_to_return['L5'] = [i[1] for i in Constants.L5_CHOICES]
        vars_to_return['L53'] = [i[1] for i in Constants.L53_CHOICES]
        vars_to_return['L54'] = [i[1] for i in Constants.L54_CHOICES]
        vars_to_return['L55'] = [i[1] for i in Constants.L55_CHOICES]
        vars_to_return['L56'] = [i[1] for i in Constants.L56_CHOICES]
        return vars_to_return

class Satisfaction(Page):
    form_model='player'
    form_fields = [
        's_1',
        's_2',
        's_3',
        's_4',
        's_5',
        's_6',
        's_7',
    ]

    def vars_for_template(self) -> dict:
        vars_to_return = {}
        vars_to_return['L5'] = [i[1] for i in Constants.L5_CHOICES]
        vars_to_return['L53'] = [i[1] for i in Constants.L53_CHOICES]
        vars_to_return['L54'] = [i[1] for i in Constants.L54_CHOICES]
        vars_to_return['L55'] = [i[1] for i in Constants.L55_CHOICES]
        vars_to_return['L56'] = [i[1] for i in Constants.L56_CHOICES]
        return vars_to_return

class pre_test(Page):
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


page_sequence = [BasicInfo, HealthInfo, SmokerEvaluation, NicotineDependence, SmokerType, Satisfaction]
