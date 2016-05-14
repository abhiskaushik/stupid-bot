#@abhi: 12:45 PM, 14th May

import os
import json

from fuzzywuzzy import fuzz

#load incoming data
data = {'their_data': []}


#load bots brain
brain = {'langs': []}

MINIMUM_SCORE = 100  
sent_count = {}

SPAM_HELP_TEXT = ("Is stupid-bot spamming? If yes type "
                  " 'stupid-bot: Please dont spam")
SEND_SPAM_HELP = 1

def scan_incoming_msg(msg, user):
    """
    Scan the message to see if the user needs help
    """

    if user.lower() in data['their_data']:
        return False

    for lang in brain['langs']:
        for i in lang['signs']:
            if fuzz.partial_ratio(str(i), msg) > MIN_SCORE:
                sent_count[user] = sent_count.get(user, 0) + 1
                if sent_count.get(user, 0) >= SEND_SPAM_HELP:
                    return lang['out'] + [SPAM_HELP_TEXT]
                return lang['out']


