# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from textattack.constraints import PreTransformationConstraint

class LabelConstraint(PreTransformationConstraint):
    """
    A constraint that does not allow to attack the labels (or any words that is important for tasks) in the prompt.
    """

    def __init__(self, labels=[]):
        self.labels = labels

    def _get_modifiable_indices(self, current_text):
        modifiable_indices = set()
        for i, word in enumerate(current_text.words):
            if str(word).lower() not in self.labels:
                modifiable_indices.add(i)
        
        return modifiable_indices

    def check_compatibility(self, transformation):
        """
        It is always true.
        """
        return True