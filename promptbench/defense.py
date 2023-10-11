# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from autocorrect import Speller


class Defense(object):
    def __init__(self, lang='en', defense_method='autocorrect'):
        self.defense_method = defense_method
        if self.defense_method == 'autocorrect':
            self.spell = Speller(lang=lang)

    def __call__(self, text):
        if self.defense_method == 'autocorrect':
            return self.spell(text)
        else:
            raise NotImplementedError


if __name__ == '__main__':
    defense = Defense()
    prompt = 'I am a student at the Univrsity of California, Berkeey.'
    print(defense(prompt))