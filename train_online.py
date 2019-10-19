from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import  Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter, RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)

def run_foodie_online(input_channel, interpretor, domain_file='restaurants_domain.yml', training_data_file='data/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpretor)
    agent.train_online(training_data_file,
                input_channel=input_channel,
                max_history=2,
                batch_size=50,
                epochs=200,
                max_training_samples=300)
    return agent

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    nlu_interpretor = RasaNLUInterpreter('models/nlu/default/foodienlu')
    run_foodie_online(ConsoleInputChannel(), nlu_interpretor)