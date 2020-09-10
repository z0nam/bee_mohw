from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class post_test(Page):
    form_model='player'
    form_fields = [
        'action_strengthening_prop_category',
        'smoking_desire_decrease_lickert',
        'post_smoking_cessation_health_status',
        'post_smoking_cessation_stress_metirc',
        'smoking_cessation_practice_plan_change',
        'smoking_cessation_adverse_effect_symptom_1',
        'smoking_cessation_adverse_effect_symptom_2',
        'smoking_cessation_adverse_effect_symptom_3',
        'smoking_cessation_adverse_effect_symptom_4',
        'smoking_cessation_adverse_effect_symptom_5',
        'smoking_cessation_adverse_effect_symptom_6',
        'smoking_cessation_adverse_effect_symptom_7',
        'smoking_cessation_adverse_effect_symptom_8',
        'smoking_cessation_adverse_effect_symptom_9',
        'daily_smoking_related_impulses_1',
        'daily_smoking_related_impulses_2',
        'reason_for_failure_to_continue_quitting_smoking',
        'smoking_perception_1',
        'smoking_perception_2',
        'smoking_perception_3',
        'smoking_perception_4',
        'smoking_perception_5',
        'smoking_perception_6',
        'confidence_against_smoking_temptation_1',
        'confidence_against_smoking_temptation_2',
        'confidence_against_smoking_temptation_3',
        'confidence_against_smoking_temptation_4',
        'confidence_against_smoking_temptation_5',
        'confidence_against_smoking_temptation_6',
        'confidence_against_smoking_temptation_7',
        'smoking_related_experience_frequency_1',
        'smoking_related_experience_frequency_2',
        'smoking_related_experience_frequency_3',
        'smoking_related_experience_frequency_4',
        'smoking_related_experience_frequency_5',
        'smoking_related_experience_frequency_6',
        'smoking_related_experience_frequency_7',
        'smoking_related_experience_frequency_8',
        'smoking_related_experience_frequency_9',
        'smoking_related_experience_frequency_10',
        'TERMINATION',
        'termination_reason',

    ]


page_sequence = [post_test,]
