# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from textattack.search_methods import SearchMethod

class BruteForceSearch(SearchMethod):
    def perform_search(self, initial_result):
        text = initial_result.attacked_text
        transformed_text_candidates = self.get_transformations(text, original_text=text)
        results, _ = self.get_goal_results(transformed_text_candidates)
        results = sorted(results, key=lambda x: -x.score)     

        return results[0]
    
    @property
    def is_black_box(self):
        return True