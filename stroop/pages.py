# from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        vars_to_return = dict()
        vars_to_return['total_rounds'] = Constants.num_rounds
        return vars_to_return


class Instruction(Page):
    pass


class Stroop(Page):
    pass


class Results(Page):

    def is_displayed(self):
        return self.round_number == 3


page_sequence = [Introduction, Instruction, Stroop, Results]
