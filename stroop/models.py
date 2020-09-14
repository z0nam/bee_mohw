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


author = 'Namun Cho (mailto:namun.cho@gmail.com)'

doc = """
    프로젝트: 행동강화물품이 금연동기강화 및 금연유지에 미치는 효과분석
    발주처: 보건복지부
    
    행동실험에 사용할 웹 기반 스트룹 테스트 모듈
"""


class Constants(BaseConstants):
    name_in_url = 'stroop'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
