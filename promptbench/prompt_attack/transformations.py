# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from textattack.transformations import Transformation

class CheckListTransformation(Transformation):

    def generate_random_sequences(num, len):
        seqs = []
        import random
        import string

        for _ in range(num):
            seq = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=len))
            seqs.append(seq)

        return seqs
    
    def _get_transformations(self, current_text, indices_to_modify):
        
        # rand_seqs = self.generate_random_sequences(50, 10)

        rand_seqs = ['d6ZQ3u0GBQ', 'vTAjHynoIG', 'OB4KVJzIft', 'LkF0FZxMZ4', 'iia2yL9Uzm', 'CuVpbbkC4c', 
                     'w52rwgo0Av', 'Vq3aBzuZcD', 'hXLpw3bbiw', 'RcRneWo6Iv', 'S6oUV5E54P', 'xikCjkMydH', 
                     'MQnugHcaoy', 'Q47Jmd4lMV', '9vGXgnbWB8', 'IhuBIhoPGc', '5yWbBXztUY', 'AMsRIKZniY', 
                     'EAB4KP2NVY', '9Q3S1F94fE', 'b74X5IVXQY', 'SFPCqpiClT', 'bhrRSokrfa', 'YHQiDfFhw4', 
                     'BWmsLx8xOA', 'PDCGfz6DL9', 'yh912BU8T0', 'ofOQXLxiW4', 'Cev0s49fbe', 'rzu98kF2KF', 
                     'zexKUTWJYG', '5XeflW1ZJc', 'is77sOXAu8', 'XStsD2pUzu', 'fwhUZUQzXW', 'Pbl3tYuoRo', 
                     'MSAddJ4D2a', 'mzjVogkRhM', 'Kw6nrs57gH', 'ItGDrrA1Sc', 'KjPJJ2a7RB', 'mOJ9nEwT4f', 
                     'ofw9fEkN5R', 'njCuciQJpB', '6a4Yn3RGVc', 'SvAp8RlOFn', 'g0vBZf3tQC', 'zq0DcZ5dnI', 
                     'lf8wBa2yEm', 'lWJoGGRdjv']

        transformed_texts = []
        for rand_seq in rand_seqs:
            transformed_texts.append(current_text.insert_text_after_word_index(index=len(current_text.words)-1, text=rand_seq))
        return transformed_texts        


class StressTestTransformation(Transformation):
    def _get_transformations(self, current_text, indices_to_modify):
        texts = [" and true is true ", " and false is not true ", " and true is true "*5]
        transformed_texts = []
        for text in texts:
            transformed_texts.append(current_text.insert_text_after_word_index(index=len(current_text.words)-1, text=text))
            # transformed_texts.append(current_text.insert_text_after_word_index(index=0, text=text))

        return transformed_texts 