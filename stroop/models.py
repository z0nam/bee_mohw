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

    META_KEYCODE = stroop_test.META_KEYCODE

    META_KEY_NAME = '스페이스 바'


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['SessionBlocks'] = stroop_test.SessionBlocks()
                # print("SessionBlocks() called. item size:", len(p.participant.vars['SessionBlocks'].items['c']))
                # print("DEFAULT_BLOCK_NUMBER:", stroop_test.DEFAULT_BLOCK_NUMBER)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    stroop_table = models.LongStringField()
    stroop_event_table = models.LongStringField()
    stroop_item_table = models.LongStringField()

    c_time = models.IntegerField(blank=True,)
    c_error = models.FloatField(blank=True,)
    c_item_size = models.IntegerField(blank=True,)
    w_time = models.IntegerField(blank=True,)
    w_error = models.FloatField(blank=True,)
    w_item_size = models.IntegerField(blank=True,)
    cw_time = models.IntegerField(blank=True,)
    cw_error = models.FloatField(blank=True,)
    cw_item_size = models.IntegerField(blank=True,)

