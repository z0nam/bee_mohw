from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from Global_Constants import GlobalConstants
import time


class Consent_IRB(Page):
    def vars_for_template(self):
        self.player.panel_id = self.participant.label or GlobalConstants.DEFAULT_PANEL_ID
        self.participant.label = self.player.panel_id
        self.participant.vars['panel_id'] = self.player.panel_id
        return {
            'panel_id': self.player.panel_id
        }

class Consent_confirm(Page):
    def before_next_page(self):
        # print("#### before_next_page called")
        self.participant.vars['expiry'] = time.time() + GlobalConstants.EXPIRE_SECONDS
        self.participant.vars['start_time'] = time.time()
        # print("expiry = ", self.participant.vars['expiry'])

    def vars_for_template(self):
        expiry_minutes = int(round(GlobalConstants.EXPIRE_SECONDS / 60, 0))
        return {
            "EXPIRY_MINUTES": expiry_minutes,
        }


page_sequence = [
    Consent_IRB,
    Consent_confirm,
]
