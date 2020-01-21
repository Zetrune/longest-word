# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests

class Game():
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if word == "":
            return False
        if is_word_in_dictionary(word) is False:
            return False
        for letter in word:
            if letter not in self.grid:
                return False
        return True

def is_word_in_dictionary(word):
    api_request = requests.get("https://wagon-dictionary.herokuapp.com/" + str(word))
    if api_request.status_code != 200:
        return False
    response = api_request.json()
    return response["found"]
