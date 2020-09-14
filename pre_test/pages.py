from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class pre_test(Page):
    form_model = 'player'
    form_fields=[
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
        'morning_smoking_time',
        'smoking_resistancy',
        'most_tasty_smoking_time',
        'how_many_gaebis_per_day',
        'morning_smoking_more_than_the_rest_of_day',
        'sick_all_day_still_smoking',
        'smoker_typeA_1',
        'smoker_typeA_2',
        'smoker_typeA_3',
        'smoker_typeB_1',
        'smoker_typeB_2',
        'smoker_typeB_3',
        'smoker_typeC_1',
        'smoker_typeC_2',
        'smoker_typeC_3',
        'smoker_typeD_1',
        'smoker_typeD_2',
        'smoker_typeD_3',
        'smoker_typeE_1',
        'smoker_typeE_2',
        'smoker_typeE_3',
        'smoker_typeF_1',
        'smoker_typeF_2',
        'smoker_typeF_3',
        'smoker_typeG_1',
        'smoker_typeG_2',
        'smoker_typeG_3',
        'sm1_1',
        'sm1_2',
        'sm1_3',
        'sm1_4',
        'sm1_5',
        'sm1_6',
        'sm1_7',
        'satisfactory_1',
        'satisfactory_2',
        'satisfactory_3',
        'satisfactory_4',
        'satisfactory_5',
        'satisfactory_6',
        'satisfactory_7',
        'self_reported_health_status',
        'stress_metric_self_reported',
        'afterward_smoking_cessation_yesno',
    ]

    def vars_for_template(self) -> dict:
        return {
            'SATISFACTION_LICKERT': [i[1] for i in Constants.SATISFACTION_LICKERT]
        }

page_sequence = [pre_test,]

