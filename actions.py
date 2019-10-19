from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import Restarted
import zomatopy
import json
import re
import pandas as pd

class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'

    def run(self, dispatcher, tracker, domain):
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        email_check = tracker.get_slot('email')
        if email_check is not None:
            if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_check):
                return [SlotSet('email', email_check)]
            else:
                dispatcher.utter_message("Sorry this is not a valid email. please check for typing errors")
                return [SlotSet('email', None)]
        else:
            dispatcher.utter_message(
                "Sorry I could not understand the email address which you provided? Please provide again")
            return [SlotSet('email', None)]
            

class ActionValidateBudget(Action):
    def name(self):
        return 'action_validate_budget'

    def run(self, dispatcher, tracker, domain):
        cost_queried = tracker.get_slot('budget')
        if cost_queried == 'less than 300' or cost_queried == 'lesser than 300' or cost_queried == '< 300' or (
                "cheap" in cost_queried):
            return [SlotSet('budget', 'low')]
        elif cost_queried == 'more than 700' or cost_queried == 'greater than 700' or cost_queried == '> 700' or (
                "costly" in cost_queried) or ("expensive" in cost_queried):
            return [SlotSet('budget', 'high')]
        else:
            return [SlotSet('budget', 'mid')]  # always return mid budget by default
