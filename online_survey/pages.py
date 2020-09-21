from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from datetime import datetime


class online_survey_1(Page):
    form_model = 'player'
    form_fields = []


class online_survey_2(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'born_year',
        'job_position',
        'smoking_in_lifetime_yesno',
        'within_past_one_year_smoking_cessation_attempted',
    ]


class online_survey_3(Page):
    form_model = 'player'
    form_fields = [
        'region',
        'region_size',
        'marriage',
        'final_schooling',
        'occupation',
        'occupation_op',
        'firm_type',
        'firm_type_op',
        'firm_size',
        'household_income',
    ]


class online_survey_4(Page):
    form_model = 'player'
    form_fields = [
        'num_drink_not',
        'drink_freq_1',
        'alc_avg_1_jan',
        'alc_avg_2_jan',
        'mid_act_yesno',
        'mid_act_day',
        'mid_act_type',
        'mid_act_min',
        'overall_health_evaluation',
        'overall_stress_evaluation',
    ]


class online_survey_5_1(Page):
    form_model = 'player'
    form_fields = [
        'tobacco_product_in_use_1',
        'tobacco_product_in_use_2',
        'tobacco_product_in_use_3',
        'tobacco_product_in_use_4',
        'tobacco_product_in_use_5',
        'tobacco_product_in_use_6',
        'tobacco_product_in_use_7',
        'tobacco_product_in_use_8',
        'tobacco_product_in_use_9',
        'tobacco_product_in_use_10',
        'tobacco_product_in_use_11',
        'tobacco_product_in_use_12',
        'do_you_smoke_tobacco',

    ]


class online_survey_5_2(Page):
    form_model = 'player'
    form_fields = [
        'first_time_to_finish_one_stick_of_tobacco',
        'first_time_to_finish_one_stick_or_more',
        'avg_daily_tobacco_smoking_amount',
        'within_past_month_tobacco_smoking_days',
        'tobacco_sticks_per_day',
    ]

    def is_displayed(self):
        return (self.player.do_you_smoke_tobacco == 1) or (self.player.do_you_smoke_tobacco == 2)


class online_survey_5_3(Page):
    form_model = 'player'
    form_fields = [
        'past_tobacco_smoking_years',
        'past_tobacco_smoking_months',
        'past_tobacco_sticks_per_day',
    ]

    def is_displayed(self):
        return self.player.do_you_smoke_tobacco == 3


class online_survey_5_4(Page):
    form_model = 'player'
    form_fields = [
        'hardest_time_to_resist_smoking_1',
        'hardest_time_to_resist_smoking_2',
        'hardest_time_to_resist_smoking_3',
        'hardest_time_to_resist_smoking_4',
        'hardest_time_to_resist_smoking_5',
        'hardest_time_to_resist_smoking_6',
        'hardest_time_to_resist_smoking_7',
        'hardest_time_to_resist_smoking_8',
        'hardest_time_to_resist_smoking_9',
        'hardest_time_to_resist_smoking_10',
        'hardest_time_to_resist_smoking_11',
        'first_tobacco_of_the_day',
        'is_it_hard_to_resist_smoking_in_the_public',
        'when_is_tobacco_the_most_tasty',
        'number_of_sticks_per_day_in_the_past',
        'is_morning_tobacco_more_tasty_than_the_rest',
        'sick_all_day_still_smoking',
    ]

    def is_displayed(self):
        return self.player.do_you_smoke_tobacco != 4


class online_survey_6_1(Page):
    form_model = 'player'
    form_fields = [
        'do_you_use_liquid_cigarette',
    ]


class online_survey_6_2(Page):
    form_model = 'player'
    form_fields = [
        'liquid_cigarette_start_year',
        'liquid_cigarette_start_month',
        'liquid_cigarette_end_year',
        'liquid_cigarette_end_month',
    ]

    def is_displayed(self):
        return self.player.do_you_use_liquid_cigarette != 4


class online_survey_6_3(Page):
    form_model = 'player'
    form_fields = [
        'most_recent_month_liquid_cigarette_use_days',
        'liquid_amount_of_liquid_cigarette_recent_week',

    ]

    def is_displayed(self):
        return (self.player.do_you_use_liquid_cigarette != 4) and (
                (self.player.liquid_cigarette_end_year == int(datetime.now().strftime('%Y'))) and (
                    int(datetime.now().strftime('%m')) - self.player.liquid_cigarette_end_month <= 1))


class online_survey_6_4(Page):
    form_model = 'player'
    form_fields = [
        'liquid_cigarette_density',
        'liquid_cigarette_hardest_to_resist_when_1',
        'liquid_cigarette_hardest_to_resist_when_2',
        'liquid_cigarette_hardest_to_resist_when_3',
        'liquid_cigarette_hardest_to_resist_when_4',
        'liquid_cigarette_hardest_to_resist_when_5',
        'liquid_cigarette_hardest_to_resist_when_6',
        'liquid_cigarette_hardest_to_resist_when_7',
        'liquid_cigarette_hardest_to_resist_when_8',
        'liquid_cigarette_hardest_to_resist_when_9',
        'liquid_cigarette_hardest_to_resist_when_10',
        'liquid_cigarette_hardest_to_resist_when_11',
        'liquid_cigarette_first_in_the_day',
        'is_it_hard_to_resist_smoking_liquid_cigarette_in_public',
        'when_is_the_liquid_cigarette_the_most_tasty',
        'liquid_cigarette_use_frequency_per_day',
        'liquid_cigarette_morning_is_more_tasty_than_the_rest',
        'liquid_cigarette_sick_all_day_still_smoking',
    ]

    def is_displayed(self):
        return self.player.do_you_use_liquid_cigarette != 4


class online_survey_7_1(Page):
    form_model = 'player'
    form_fields = [
        'do_you_use_tobacco_type_e_cigarette',
    ]


class online_survey_7_2(Page):
    form_model = 'player'
    form_fields = [
        'tobacco_type_e_cigarette_start_year',
        'tobacco_type_e_cigarette_start_month',
        'tobacco_type_e_cigarette_end_year',
        'tobacco_type_e_cigarette_end_month',
    ]

    def is_displayed(self):
        return self.player.do_you_use_tobacco_type_e_cigarette != 4


class online_survey_7_3(Page):
    form_model = 'player'
    form_fields = [
        'within_recent_month_days_of_use_for_tobacco_type_e_cigarette',
    ]

    def is_displayed(self):
        return (self.player.do_you_use_tobacco_type_e_cigarette != 4) and (
                (self.player.tobacco_type_e_cigarette_end_year == int(datetime.now().strftime('%Y'))) and (
                int(datetime.now().strftime('%m')) - self.player.tobacco_type_e_cigarette_end_month <= 1))


class online_survey_7_4(Page):
    form_model = 'player'
    form_fields = [
        'tobacco_type_e_cigarette_avg_sticks_per_day',
        'tobacco_type_e_cigarette_hardest_to_resist_when_1',
        'tobacco_type_e_cigarette_hardest_to_resist_when_2',
        'tobacco_type_e_cigarette_hardest_to_resist_when_3',
        'tobacco_type_e_cigarette_hardest_to_resist_when_4',
        'tobacco_type_e_cigarette_hardest_to_resist_when_5',
        'tobacco_type_e_cigarette_hardest_to_resist_when_6',
        'tobacco_type_e_cigarette_hardest_to_resist_when_7',
        'tobacco_type_e_cigarette_hardest_to_resist_when_8',
        'tobacco_type_e_cigarette_hardest_to_resist_when_9',
        'tobacco_type_e_cigarette_hardest_to_resist_when_10',
        'tobacco_type_e_cigarette_hardest_to_resist_when_11',
        'tobacco_type_e_cigarette_first_in_the_day',
        'tobacco_type_e_cigarette_hard_to_resist_in_public',
        'tobacco_type_e_cigarette_most_tasty_in_the_day',
        'tobacco_type_e_cigarette_sticks_per_day',
        'tobacco_e_cig_more_tasty_in_the_morning',
        'tobacco_type_e_cigarette_sick_all_day_still_smoking',
    ]

    def is_displayed(self):
        return self.player.do_you_use_tobacco_type_e_cigarette != 4


class online_survey_8(Page):
    form_model = 'player'
    form_fields = [
        'smoking_cessation_attempt_count',
        'within_one_month_do_you_plan_to_quit_smoking',
        'within_past_five_days_last_time_to_use_nicotine_alternatives',
        'ate_food_products_when_smoking_desire_arose',
        'effect_of_food_product_in_resisting_smoking_desire',
        'drink_water_when_desiring_to_smoke',
        'effect_of_water_in_resisting_smoking_desire',
        'pressure_tool_when_desiring_to_smoke',
        'effect_of_pressure_tool_in_resisting_smoking_desire',
        'mouth_wash_when_resisting_smoking_desire',
        'effect_of_mouth_wash_in_resisting_smoking_desire',
        'aroma_pipe_or_change_stick_when_resisting_smoking_desire',
        'effect_of_aroma_stick_against_smoking_desire',
        'smoking_cessation_method_self_will',
        'smoking_cessation_method_call_center',
        'smoking_cessation_method_clinic',
        'smoking_cessation_method_pharmaceuticals',
        'smoking_cessation_method_champix',
        'smoking_cessation_method_internet',
        'smoking_cessation_method_other',
    ]


class online_survey_9(Page):
    form_model = 'player'
    form_fields = [
        'smoking_cessation_failure_reason_1',
        'smoking_cessation_failure_reason_2',
        'smoking_cessation_failure_reason_3',
        'smoking_cessation_failure_reason_4',
        'smoking_cessation_failure_reason_5',
        'smoking_cessation_failure_reason_6',
        'smoking_cessation_failure_reason_7',
        'reason_to_quit_smoking_this_time_primary',
        'reason_to_quit_smoking_this_time_primary_op',
        'reason_to_quit_smoking_this_time_secondary',
        'reason_to_quit_smoking_this_time_secondary_op',
        'reason_to_quit_smoking_this_time_tertiary',
        'reason_to_quit_smoking_this_time_tertiary_op',
        'smoking_cessation_helper_1',
        'smoking_cessation_helper_2',
        'smoking_cessation_helper_3',
        'smoking_cessation_helper_4',
        'smoking_cessation_helper_5',
        'smoking_cessation_helper_6',
        'smoking_cessation_helper_7',
        'smoking_cessation_helper_8',
        'smoking_cessation_helper_9',
        'smoking_cessation_helper_10',
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
        'smoking_cessation_importance',
        'smoking_cessation_confidence',
        'smoking_cessation_readiness',
    ]


class online_survey_10(Page):
    form_model = 'player'
    form_fields = [
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

    def vars_for_template(self):
        return self.player.vars_for_template()


class online_survey_11(Page):
    form_model = 'player'
    form_fields = [
        'sa_1',
        'sa_2',
        'sa_3',
        'sa_4',
        'sa_5',
        'sa_6',
        'sa_7',
        'sa_8',
    ]

    def vars_for_template(self):
        return self.player.vars_for_template()


class online_survey_12(Page):
    form_model = 'player'
    form_fields = [
        'sn_1',
        'sn_2',
    ]

    def vars_for_template(self):
        return self.player.vars_for_template()

    # def vars_for_template(self) -> dict:
    #     vars_to_return = {}
    #     vars_to_return['L5'] = [i[1] for i in Constants.L5_CHOICES]
    #     vars_to_return['L52'] = [i[1] for i in Constants.L52_CHOICES]
    #     return vars_to_return
    #


class online_survey_13(Page):
    form_model = 'player'
    form_fields = [
        'pbc_1',
        'pbc_2',
    ]

    def vars_for_template(self):
        return self.player.vars_for_template()


class online_survey_14(Page):
    form_model = 'player'
    form_fields = [
        'i_1',
        'i_2',
        'i_3',
        'i_4',
    ]

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [online_survey_1, online_survey_2, online_survey_3, online_survey_4, online_survey_5_1,
                 online_survey_5_2, online_survey_5_3, online_survey_5_4, online_survey_6_1, online_survey_6_2,
                 online_survey_6_3, online_survey_6_4, online_survey_7_1, online_survey_7_2, online_survey_7_3,online_survey_7_4,
                 online_survey_8, online_survey_9, online_survey_10, online_survey_11, online_survey_12,
                 online_survey_13, online_survey_14, ]
