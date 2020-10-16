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
행동강화물품 사후조사 불참자용 설문 
"""


class Constants(BaseConstants):
    name_in_url = 'post_test_d'
    players_per_group = None
    num_rounds = 1

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

    TERMINATION = models.IntegerField(
        label="행동실험이 정상적으로 종결되었는지 혹은 중간에 종결되었는지를 선택해 주십시오.",
        choices=[
            [1, "정상종결"],
            [2, "중간종결"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    termination_reason = models.IntegerField(
        label="행동실험이 종결된 사유를 선택해주십시오.",
        choices=Constants.TERMINATION_REASON,
        widget=widgets.RadioSelect,
    )
    text_field = models.LongStringField(
        label="메모남겨주실 부분 있으시면 여기에 남겨주시면 감사드리겠습니다.",
        blank=True,
    )
