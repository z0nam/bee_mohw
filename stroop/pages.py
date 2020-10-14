# from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants
from .models import Player
import stroop_test
import random


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        vars_to_return = dict()
        vars_to_return['total_rounds'] = Constants.num_rounds
        return vars_to_return


class Instruction(Page):
    def vars_for_template(self):
        vars_to_return = dict()
        vars_to_return['cbst_image'] = "stroop/CBST_"\
                                       + stroop_test.SessionBlocks.name_of_test[self.round_number - 1].upper()\
                                       + ".png"
        # print(vars_to_return['cbst_image']
        vars_to_return['messages'] = stroop_test.instruction_messages[self.round_number - 1]
        return vars_to_return


class Stroop(Page):
    def vars_for_template(self):
        vars_to_return = dict()

        name_of_test = self.participant.vars['SessionBlocks'].name_of_test[self.round_number - 1]   # c, w, cw
        stroop_items = self.participant.vars['SessionBlocks'].items[name_of_test]
        stroop_correct_answers = []
        stroop_displayed_characters = []
        stroop_displayed_colors = []
        stroop_displayed_color_codes = []
        for item in stroop_items:
            stroop_correct_answers.append(item.correct_answer)
            stroop_displayed_characters.append(item.displayed_character)
            stroop_displayed_color_codes.append(item.displayed_color_code)
            stroop_displayed_colors.append(item.displayed_color)
        vars_to_return['stroop_correct_answers'] = stroop_correct_answers
        vars_to_return['stroop_displayed_characters'] = stroop_displayed_characters
        vars_to_return['stroop_displayed_color_codes'] = stroop_displayed_color_codes
        vars_to_return['stroop_displayed_colors'] = stroop_displayed_colors
        # vars_to_return['seed_for_refresh_js_cache'] = random.random()
        vars_to_return['seed_for_refresh_js_cache'] = 0    # when production, use this

        vars_to_return['color_strs'] = stroop_test.COLOR_STR
        vars_to_return['background_color'] = stroop_test.BACKGROUND_COLOR
        return vars_to_return

    form_model = 'player'
    form_fields = [
        'stroop_event_table',
        'stroop_item_table',
        'stroop_table',
        'c_time',
        'c_error',
        'c_item_size',
        'w_time',
        'w_error',
        'w_item_size',
        'cw_time',
        'cw_error',
        'cw_item_size',
    ]

class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds  # last round


page_sequence = [Introduction, Instruction, Stroop, Results]
