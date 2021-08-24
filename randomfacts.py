"""Random Facts"""
import urllib.request
import json
from errbot import BotPlugin, botcmd


class Randomfacts(BotPlugin):
    """Random Facts"""

    @botcmd
    def random(self, msg, args):
        """Random Fact from https://uselessfacts.jsph.pl/random.json"""
        return self.randomfacts_send(msg, random=False)

    @botcmd
    def random_today(self, msg, args):
        """Today Random Fact of the day"""
        return self.randomfacts_send(msg, random=True)

    def randomfacts_send(self, msg, random):
        """Random Fact"""
        # apodapi.herokuapp.com/api/?date=2001-07-12
        url = 'https://uselessfacts.jsph.pl/random.json'
        page = urllib.request.Request(url)
        response = json.loads(urllib.request.urlopen(page).read().decode('utf-8'))
        if 'text' in response:
            return response['text']
        return 'No fact returned'
