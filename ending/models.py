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
import time


author = 'Kyubum Moon <mailto: moonx190@umn.edu>'

doc = """
보건복지부 행동강화 물품 연구 
"""


class Constants(BaseConstants):
    name_in_url = 'ending'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    embrain_response = models.StringField()
    elapsed_time_seconds = models.IntegerField()

    def get_elapsed_time_seconds(self):
        start_time = self.particiapnt.vars['start_time']
        current_time = time.time()
        elapsed_time = current_time - start_time
        return int(elapsed_time)

