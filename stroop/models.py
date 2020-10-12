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

import stroop_test

author = 'Namun Cho (mailto:dr.strangelove@kberi.re.kr)'

doc = """
    프로젝트: 행동강화물품이 금연동기강화 및 금연유지에 미치는 효과분석
    발주처: 보건복지부
    
    행동실험에 사용할 웹 기반 스트룹 테스트 모듈
"""


class Constants(BaseConstants):
    name_in_url = 'stroop'
    players_per_group = None
    num_rounds = len(stroop_test.default_SessionBlocks.name_of_test)

    #todo meta_keycode는 쓰면 안됨: 팝업창(alert) 쓰는 방식으로 진행할 것.
    META_KEYCODE = stroop_test.META_KEYCODE

    META_KEY_NAME = '스페이스 바'


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['SessionBlocks'] = stroop_test.SessionBlocks()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stroop_table = models.LongStringField()
    stroop_event_table = models.LongStringField()
    stroop_item_table = models.LongStringField()

    c_time = models.IntegerField()
    c_error = models.FloatField()
    c_item_size = models.IntegerField()
    w_time = models.IntegerField()
    w_error = models.FloatField()
    w_item_size = models.IntegerField()
    cw_time = models.IntegerField()
    cw_error = models.FloatField()
    cw_item_size = models.IntegerField()

