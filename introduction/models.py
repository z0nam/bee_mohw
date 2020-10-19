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


author = 'Kyubum Moon <mailto:moonx190@umn.edu>'

doc = """
흡연 및  금연 경험에 관한 연구 
"""


class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    panel_id = models.StringField()
    fgi_will = models.BooleanField(
        label="<-- 그룹인터뷰 참여의사가 있으신 분은 체크해주세요. 향후 모집시 우선 연락드릴 것입니다. ",
        blank=True,
        widget=widgets.CheckboxInput,
    )
