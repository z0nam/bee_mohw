from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class online_survey(Page):
    form_model='player'
    form_fields=[
        'gender',
        'born_year',
        'job_position',
        'smoking_in_lifetime_yesno',
        'within_past_one_year_smoking_cessation_attempted',
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
        'num_drink_not',
        'drink_freq_1',
        'drink_freq_2',
        'drink_freq_3',
        'alc_avg_1_jan',
        'alc_avg_1_bot',
        'alc_avg_1_can',
        'alc_avg_1_cc',
        'alc_avg_2_jan',
        'alc_avg_2_bot',
        'alc_avg_2_can',
        'alc_avg_2_cc',
        'alc_avg_3_jan',
        'alc_avg_3_bot',
        'alc_avg_3_can',
        'alc_avg_3_cc',
        'alc_avg_4_jan',
        'alc_avg_4_bot',
        'alc_avg_4_can',
        'alc_avg_4_cc',
        'alc_avg_5_jan',
        'alc_avg_5_bot',
        'alc_avg_5_can',
        'alc_avg_5_cc',
        'high_act_day',
        'high_act_hour',
        'high_act_min',
        'mid_act_day',
        'mid_act_hour',
        'mid_act_min',
        'muscle_act_days',

        'overall_health_evaluation',
        'overall_stress_evaluation',

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
        'first_time_to_finish_one_stick_of_tobacco',
        'first_time_to_finish_one_stick_or_more',
        'avg_daily_tobacco_smoking_amount',
        'within_past_month_tobacco_smoking_days',
        'tobacco_sticks_per_day',
        'past_tobacco_smoking_years',
        'past_tobacco_smoking_months',
        'past_tobacco_sticks_per_day',
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
    def born_year_error_message(self, value):
        if (value > Constants.BORN_YEAR_MAX or value < Constants.BORN_YEAR_MIN):
            return str.format("태어나신 해는 유효한 네자리 숫자 (가령 {} - {} 사이의 숫자) 로 입력하셔야 합니다.", Constants.BORN_YEAR_MIN, Constants.BORN_YEAR_MAX)

    def work_type_error_message(self, value):
        if (value == Constants.UNPAID):
            return str.format("안녕하십니까? 본 연구는 보건복지부의 위탁을 받아 행동강화 물품이 금연동기강화 및 금연유지에 미치는 효과를 연구하기 위한 목적에 따라, 현재 6개월 이상 재직자를 대상으로 연구참여를 제한하게 된 점 양해 부탁드립니다. 감사합니다.") # todo: 이것을 클릭했을 경우 alert 뜨고 종료로 안내하도록 수정하기

    def not_a_smoker_error_message(self, value):
        if (value == 999 | value==9999):
            return str.format("안녕하십니까? 본 연구는 보건복지부의 위탁을 받아 행동강화 물품이 금연동기강화 및 금연유지에 미치는 효과를 연구하기 위한 목적에 따라, 5갑(100개비)이상 흡연자를 대상으로 진행되기에 귀하의 연구참여를 제한합니다. ")
    def smoking_cessation_experience_no_error_message(self, value):
        if (value == 99999):
            return str.format("본 연구는 보건복지부의 위탁을 받아 행동강화물품이 금연동기강화 및 금연유지에 미치는 효과를 연구하기 위한 목적에 따라, 최근 1년 동안 담배를 끊고자 하루(24시간) 이상 금연한 적이 있는 분들만을 대상으로 하는 연구입니다. 따라서 귀하의 연구 참가를 제한합니다. ")

page_sequence = [online_survey,]
