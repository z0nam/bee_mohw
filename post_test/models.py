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
from . import post_test_questions

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
    smoker_type = post_test_questions.SMOKER_TYPE
    satisfaction = post_test_questions.SATISFACTION
    smoking_cessation_adverse_effect = post_test_questions.SMOKING_CESSATION_ADVERSE_EFFECT
    smoking_experience = post_test_questions.SMOKING_DESIRE_EXPERIENCE
    smoking_opinion = post_test_questions.SMOKING_OPINION
    confidence_against_smoking = post_test_questions.CONFIDENCE_AGAINST_SMOKING
    experience_frequency = post_test_questions.EXPERIENCE_FREQUENCY
    L5_CHOICES = GlobalConstants.L5_CHOICES
    L53_CHOICES = GlobalConstants.L53_CHOICES
    L54_CHOICES = GlobalConstants.L54_CHOICES
    L55_CHOICES = GlobalConstants.L55_CHOICES
    L56_CHOICES = GlobalConstants.L56_CHOICES
    ACTION_STRENGTHENING_PROP = [
        [1, "물병"],
        [2, "식품류(캔디)"],
        [3, "손 운동용품(스냅스)"],
        [4, "구강청결제(치약세트)"],
        [5, "흡연욕구저하제(아로마금연파이프)"],
        [6, "흡연욕구저하제(체인지 스틱)"],
    ]

    SMOKING_DESIRE_DECREASE_LICKERT = [
        [1, "① 매우 그렇다"],
        [2, "② 그렇다"],
        [3, "③ 보통"],
        [4, "④ 그렇지 않다"],
        [5, "⑤ 전혀 그렇지 않다"],
    ]

    POST_SMOKING_CESSATION_HEALTH_STATUS = [
        [1, "① 매우 건강이 좋아짐"],
        [2, "② 조금 건강이 좋아짐"],
        [3, "③ 차이가 없음"],
        [4, "④ 조금 건강이 나빠짐"],
        [5, "⑤ 많이 건강이 나빠짐"],
    ]

    POST_SMOKING_CESSATION_STRESS_METRIC = [
        [1, "① 전혀 받지 않음"],
        [2, "② 별로 받지 않음"],
        [3, "③ 그저 그런 편임"],
        [4, "④ 약간 받는 편"],
        [5, "⑤ 매우 많이 받음"],
    ]

    SMOKING_CESSATION_PRACTICE_PLAN_CHANGE = [
        [1, "금연에 대해 생각해 본 적 없음"],
        [2, "향후 6개월 이내에 금연할 계획이 있음"],
        [3, "1개월 이내에 금연할 계획이 있음"],
        [4, "금연을 실천한 지 1일 이상이 지났음"],
        [5, "금연을 실천한 지 6개월 이상 되었음"],
    ]

    SMOKING_CESSATION_ADVERSE_EFFECT_LICKERT = [
        [1, "① 전혀 그렇지않다"],
        [2, "② 그렇지 않다"],
        [3, "③ 보통"],
        [4, "④ 그렇다"],
        [5, "⑤ 매우 그렇다"],
    ]

    DAILY_SMOKING_RELATED_EXPERIENCE_LICKERT = [
        [1, "① 전혀 욕구가 없다"],
        [2, "② 아무욕구도 없다"],
        [3, "③ 보통"],
        [4, "④ 항상"],
        [5, "⑤ 매우강하다"],
    ]

    WHY_YOU_COULD_NOT_CONTINUE_QUITTING_SMOKING_AFTER_PAST_ONE_WEEK = [
        [1, "금연에 실패하지 않았음 (금연유지 중임)"],
        [2, "금단증상이 나타나서"],
        [3, "스트레스가 많아서"],
        [4, "의지력이 부족해서"],
        [5, "금연방법을 잘 몰라서"],
        [6, "흡연하는 친구, 동료들의 영향으로"],
        [7, "금연보조제 사용 등 효과가 없는 것 같아서"],
    ]

    CONFIDENCE_LEVEL = [
        [1, "① 전혀 자신없다"],
        [2, "② 자신없다"],
        [3, "③ 보통"],
        [4, "④ 자신있다"],
        [5, "⑤ 매우 자신있다"],
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


def make_field_smoker_type(index):
    return models.IntegerField(
        label=Constants.smoker_type[index - 1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )


def make_field_satisfaction(index):
    return models.IntegerField(
        label=Constants.satisfaction[index - 1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L53_CHOICES,
    )


def make_field_smoking_cessation_adverse(index):
    return models.IntegerField(
        label=Constants.smoking_cessation_adverse_effect[index - 1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L54_CHOICES,
    )


def make_field_smoking_experience(index):
    return models.IntegerField(
        label=Constants.smoking_experience[index - 1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L55_CHOICES,
    )


def make_field_smoking_opinion(index):
    return models.IntegerField(
        label=Constants.smoking_opinion[index - 1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L54_CHOICES,
    )


def make_field_confidence(index):
    return models.IntegerField(
        label=Constants.confidence_against_smoking[index - 1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L56_CHOICES,
    )


def make_field_experience_frequency(index):
    return models.IntegerField(
        label=Constants.experience_frequency[index - 1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L54_CHOICES,
    )


class Player(BasePlayer):
    # participant_name = models.StringField(
    #     label="귀하의 성명을 홍*동의 형태로 입력해주십시오.",
    #     blank=True,
    # )
    # organization_type = models.StringField(
    #     label="귀하의 소속기관을 입력해주십시오",
    #     blank=True,
    # )
    behavior_strengthening_material_barcode = models.IntegerField(
        label="지급받은 행동물품 일련번호를 입력해주십시오.",
        blank=True,
    )


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

    sa_1 = make_field_smoking_cessation_adverse(0)
    sa_2 = make_field_smoking_cessation_adverse(1)
    sa_3 = make_field_smoking_cessation_adverse(2)
    sa_4 = make_field_smoking_cessation_adverse(3)
    sa_5 = make_field_smoking_cessation_adverse(4)
    sa_6 = make_field_smoking_cessation_adverse(5)
    sa_7 = make_field_smoking_cessation_adverse(6)
    sa_8 = make_field_smoking_cessation_adverse(7)
    sa_9 = make_field_smoking_cessation_adverse(8)

    se_1 = make_field_smoking_experience(0)
    se_2 = make_field_smoking_experience(1)

    reason_for_failure_to_continue_quitting_smoking = models.IntegerField(
        label="지난 1주일 이후 금연에 실패한 가장 큰 이유는 무엇입니까?",
        choices=Constants.WHY_YOU_COULD_NOT_CONTINUE_QUITTING_SMOKING_AFTER_PAST_ONE_WEEK,
        widget=widgets.RadioSelect,
    )

    so_1 = make_field_smoking_opinion(0)
    so_2 = make_field_smoking_opinion(1)
    so_3 = make_field_smoking_opinion(2)
    so_4 = make_field_smoking_opinion(3)
    so_5 = make_field_smoking_opinion(4)
    so_6 = make_field_smoking_opinion(5)

    cas_1 = make_field_confidence(0)
    cas_2 = make_field_confidence(1)
    cas_3 = make_field_confidence(2)
    cas_4 = make_field_confidence(3)
    cas_5 = make_field_confidence(4)
    cas_6 = make_field_confidence(5)
    cas_7 = make_field_confidence(6)

    ef_1 = make_field_experience_frequency(0)
    ef_2 = make_field_experience_frequency(1)
    ef_3 = make_field_experience_frequency(2)
    ef_4 = make_field_experience_frequency(3)
    ef_5 = make_field_experience_frequency(4)
    ef_6 = make_field_experience_frequency(5)
    ef_7 = make_field_experience_frequency(6)
    ef_8 = make_field_experience_frequency(7)
    ef_9 = make_field_experience_frequency(8)
    ef_10 = make_field_experience_frequency(9)

    TERMINATION = models.IntegerField(
        label="행동실험이 정상적으로 종결되었는지 혹은 중간에 종결되었는지를 선택해 주십시오.",
        choices=[
            [1, "정상종결"],
            [2, "중간종결"],
        ],
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )

    termination_reason = models.IntegerField(
        label="행동실험이 종결된 사유를 선택해주십시오.",
        choices=Constants.TERMINATION_REASON,
        widget=widgets.RadioSelect,
        blank=True,
    )
    text_field = models.LongStringField(
        label="메모남겨주실 부분 있으시면 여기에 남겨주시면 감사드리겠습니다.",
        blank=True,
    )

    def vars_for_template(self) -> dict:
        vars_to_return = {}
        vars_to_return['L5'] = [i[1] for i in Constants.L5_CHOICES]
        vars_to_return['L53'] = [i[1] for i in Constants.L53_CHOICES]
        vars_to_return['L54'] = [i[1] for i in Constants.L54_CHOICES]
        vars_to_return['L55'] = [i[1] for i in Constants.L55_CHOICES]
        vars_to_return['L56'] = [i[1] for i in Constants.L56_CHOICES]
        return vars_to_return