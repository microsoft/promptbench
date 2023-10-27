# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from autocorrect import Speller


class Defense(object):
    def __init__(self, defense_method='spellcorrect', lang='en'):
        self.defense_method = defense_method
        if self.defense_method == 'spellcorrect':
            self.spell = Speller(lang=lang)

    def __call__(self, text):
        if self.defense_method == 'spellcorrect':
            return self.spell(text)
        else:
            raise NotImplementedError


if __name__ == '__main__':
    defense = Defense()
    prompt = 'I am a student at the Univrsity of California, Berkeey.'
    print(defense(prompt))