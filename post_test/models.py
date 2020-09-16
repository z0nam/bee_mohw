from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from Global_Constants import GlobalConstants


author = 'Kyubum Moon<mailto:moonx190@umn.edu>'

doc = """
행동강화물품 사후조사 
"""


class Constants(BaseConstants):
    name_in_url = 'post_test'
    players_per_group = None
    num_rounds = 1

    START_YEAR_MIN = 1959
    START_YEAR_MAX = 2020
    MONTH_MIN = 1
    MONTH_MAX = 12
    DATE_MIN = 1
    DATE_MAX = 31

    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    BINARY_POSSESSION = GlobalConstants.BINARY_POSSESSION

    ACTION_STRENGTHENING_PROP = [
        [1, "물"],
        [2, "식품류(비타민, 캔디, 껌 등)"],
        [3, "손 운동용품(지압봉, 스냅스 등)"],
        [4, "구강청결제(가글 등)"],
        [5, "흡연욕구저하제(아로마금연파이프)"],
        [6, "흡연욕구저하제(체인지 스틱)"],
    ]

    SMOKING_DESIRE_DECREASE_LICKERT = [
        [1, "매우 그렇다"],
        [2, "그렇다"],
        [3, "보통"],
        [4, "그렇지 않다"],
        [5, "전혀 그렇지 않다"],
    ]

    POST_SMOKING_CESSATION_HEALTH_STATUS = [
        [1, "매우 건강이 좋아짐"],
        [2, "조금 건강이 좋아짐"],
        [3, "차이가 없음"],
        [4, "조금 건강이 나빠짐"],
        [5, "많이 건강이 나빠짐"],
    ]

    POST_SMOKING_CESSATION_STRESS_METRIC = [
        [1, "전혀 받지 않음"],
        [2, "별로 받지 않음"],
        [3, "그저 그런 편임"],
        [4, "약간 받는 편"],
        [5, "매우 많이 받음"],
    ]

    SMOKING_CESSATION_PRACTICE_PLAN_CHANGE = [
        [1, "금연에 대해 생각해 본 적 없음"],
        [2, "향후 6개월 이내에 금연할 계획이 있음"],
        [3, "1개월 이내에 금연할 계획이 있음"],
        [4, "금연을 실천한 지 1일 이상이 지났음"],
        [5, "금연을 실천한 지 6개월 이상 되었음"],
    ]

    SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT =[
        [1, "전혀 그렇지않다"],
        [2, "그렇지 않다"],
        [3, "보통"],
        [4, "그렇다"],
        [5, "매우 그렇다"],
    ]

    DAILY_SMOKING_RELATED_EXPERIENCE_LICKERT = [
        [1, "전혀 욕구가 없다"],
        [2, "아무욕구도 없다"],
        [3, "보통"],
        [4, "항상"],
        [5, "매우강하다"],
    ]

    WHY_YOU_COULD_NOT_CONTINUE_QUITTING_SMOKING_AFTER_PAST_ONE_WEEK = [
        [1, "금연유지 중임"],
        [2, "금단증상이 나타나서"],
        [3, "스트레스가 많아서"],
        [4, "의지력이 부족해서"],
        [5, "금연방법을 잘 몰라서"],
        [6, "흡연하는 친구, 동료들의 영향으로"],
        [7, "금연보조제 사용 등 효과가 없는 것 같아서"],
    ]

    CONFIDENCE_LEVEL =[
        [1, "전혀 자신없다"],
        [2, "자신없다"],
        [3, "보통"],
        [4, "자신있다"],
        [5, "매우 자신있다"],
    ]

    TERMINATION_REASON = [
        [1, "금연중"],
        [2, "중간에 흡연(금연실패)"],
        [3, "금연거부"],
        [4, "연락두절"],
        [5, "타지역으로 이사"],
        [6, "질병 및 사망"],
        [7, "미결심자"],
        [8, "기타"],
        [9, "보건소연계"],
        [10, "금연상담전화연계"],
        [11, "병의원 연계"],
        [12, "찾금 연계(일반형)"],
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    action_strengthening_prop_category = models.IntegerField(
        label="귀하께서 지난 1주일 동안 사용한 행동강화물품의 종류는 무엇입니까?",
        choices=Constants.ACTION_STRENGTHENING_PROP,
        widget=widgets.RadioSelect,
    )

    smoking_desire_decrease_lickert = models.IntegerField(
        label="귀하가 사용하는 행동강화물품은 흡연욕구를 저하시키는데 도움이 되었습니까?",
        choices=Constants.SMOKING_DESIRE_DECREASE_LICKERT,
        widget=widgets.RadioSelect,
    )

    post_smoking_cessation_health_status = models.IntegerField(
        label="금연 이후, 귀하가 생각하는 본인의 현재 건강상태는 개선되었다고 생각합니까?",
        choices=Constants.POST_SMOKING_CESSATION_HEALTH_STATUS,
        widget=widgets.RadioSelect,
    )

    post_smoking_cessation_stress_metirc = models.IntegerField(
        label="금연 이후, 평소 귀하의 스트레스 정도는 어떻습니까?",
        choices=Constants.POST_SMOKING_CESSATION_STRESS_METRIC,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_practice_plan_change = models.IntegerField(
        label="현재 귀하께서는 금연 실천할 생각이 변화하였습니까?",
        choices=Constants.SMOKING_CESSATION_PRACTICE_PLAN_CHANGE,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_1 = models.IntegerField(
        label="담배를 피우고 싶은 절심함",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_2 = models.IntegerField(
        label="짜증남/ 좌절/ 분노",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_3 = models.IntegerField(
        label="불안",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_4 = models.IntegerField(
        label="집중하기 어려움",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_5 = models.IntegerField(
        label="안절부절 하지 못함",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_6 = models.IntegerField(
        label="식욕증가",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_7 = models.IntegerField(
        label="수면방",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_8 = models.IntegerField(
        label="우울함",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_adverse_effect_symptom_9 = models.IntegerField(
        label="참지 못함",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    daily_smoking_related_impulses_1 = models.IntegerField(
        label="오늘 담배를 사용하겠다는 충동을 얼마나 많이 느꼈습니까?",
        choices = Constants.DAILY_SMOKING_RELATED_EXPERIENCE_LICKERT,
        widget = widgets.RadioSelect,
    )

    daily_smoking_related_impulses_2 = models.IntegerField(
        label="오늘은 얼마나 강한 충동이 있었습니까?",
        choices = Constants.DAILY_SMOKING_RELATED_EXPERIENCE_LICKERT,
        widget = widgets.RadioSelect,
    )

    reason_for_failure_to_continue_quitting_smoking = models.IntegerField(
        label="지난 1주일 이후 금연에 실패한 가장 큰 이유는 무엇입니까?",
        choices=Constants.WHY_YOU_COULD_NOT_CONTINUE_QUITTING_SMOKING_AFTER_PAST_ONE_WEEK,
        widget=widgets.RadioSelect,
    )

    smoking_perception_1 = models.IntegerField(
        label="흡연은 스트레스를 해소 시켜준다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_perception_2 = models.IntegerField(
        label="흡연은 일에 집중을 더 잘할 수 있도록 도와준다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_perception_3 = models.IntegerField(
        label="흡연을 하면 긴장이 풀리면서 기분이 좋아진다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_perception_4 = models.IntegerField(
        label="흡연은 나의 건강을 해친다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_perception_5 = models.IntegerField(
        label="흡연은 다른 사람의 건강을 해치는 일이다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_perception_6 = models.IntegerField(
        label="흡연의 위험성을 알면서도 흡연하는 것은 어리석은 일이다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    confidence_against_smoking_temptation_1 = models.IntegerField(
        label="술자리에서 음주 시",
        choices=Constants.CONFIDENCE_LEVEL,
        widget=widgets.RadioSelect,
    )

    confidence_against_smoking_temptation_2 = models.IntegerField(
        label="아침에 잠자리에서 일어났을 때",
        choices=Constants.CONFIDENCE_LEVEL,
        widget=widgets.RadioSelect,
    )

    confidence_against_smoking_temptation_3 = models.IntegerField(
        label="걱정거리가 생겼거나 스트레스를 받을 때",
        choices=Constants.CONFIDENCE_LEVEL,
        widget=widgets.RadioSelect,
    )

    confidence_against_smoking_temptation_4 = models.IntegerField(
        label="잡담을 하거나 휴식을 취하면서 커피를 마실 때",
        choices=Constants.CONFIDENCE_LEVEL,
        widget=widgets.RadioSelect,
    )

    confidence_against_smoking_temptation_5 = models.IntegerField(
        label="기운을 낼 필요가 있다고 느낄 때 (업무 등으로 몸이 지쳐있을 때)",
        choices=Constants.CONFIDENCE_LEVEL,
        widget=widgets.RadioSelect,
    )

    confidence_against_smoking_temptation_6 = models.IntegerField(
        label="화가 많이 났을 때",
        choices=Constants.CONFIDENCE_LEVEL,
        widget=widgets.RadioSelect,
    )

    confidence_against_smoking_temptation_7 = models.IntegerField(
        label="가족이나 친구들이 옆에서 담배를 피울 때",
        choices=Constants.CONFIDENCE_LEVEL,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_1 = models.IntegerField(
        label="담배 피우고 싶을 때는 일부러 딴 생각을 하거나 다른 일을 한다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_2 = models.IntegerField(
        label="금연하고 싶을 때는 언제든지 금연할 수 있다고 생각한다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_3 = models.IntegerField(
        label="사회가 흡연자들의 생활을 불편하게 하는 방향으로 변화하고 있다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_4 = models.IntegerField(
        label="금연의 혜택이나 금연방법에 대한 정보를 읽거나 들은 적이 있다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_5 = models.IntegerField(
        label="흡연욕구를 참았을 때 주위사람들로부터 칭찬을 받는다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_6 = models.IntegerField(
        label="흡연은 환경을 오염시키는 원인이 된다고 생각한다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_7 = models.IntegerField(
        label="흡연의 결과에 대한 경고문이나 포스터 등을 보면 걱정이 된다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_8 = models.IntegerField(
        label="담배를 끊지 못하는 내 자신이 실망스럽게 느껴진다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_9 = models.IntegerField(
        label="담배를 끊기 위해 담배, 재떨이 등을 회사나 집에서 모두 치웠다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoking_related_experience_frequency_10 = models.IntegerField(
        label="나의 금연노력을 도와줄 가족이나 친구가 주변에 있다.",
        choices=Constants.SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT,
        widget=widgets.RadioSelect,
    )

    TERMINATION = models.IntegerField(
        label="금연프로그램이 정상적으로 종결되었는지 혹은 중간에 종결되었는지를 선택해 주십시오.",
        choices=[
            [1,"정상종결"],
            [2,"중간종결"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    termination_reason = models.IntegerField(
        label="금연프로그램이 종결된 사유를 선택해주십시오.",
        choices=Constants.TERMINATION_REASON,
        widget=widgets.RadioSelect,
    )








