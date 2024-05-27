
import os
import json
import textwrap
from types import SimpleNamespace

import promptbench as pb
from tqdm import tqdm
import torch

from aphrodite_client import AphroditeClient


# TODO: parameterize these
file_questions = open("finance_qa.json")
test_cases = json.load(file_questions, object_hook=lambda d: SimpleNamespace(**d)) 

username = os.getenv("APOKTO_USER") 
password = os.getenv("APOKTO_PASSWORD")

def benchmark():

    client = AphroditeClient(username, password)

    for test_case in test_cases[:-1]:

        question = test_case.question

        for reference in test_case.reference:

            reference_output_aphrodite = reference.aphrodite_response
            reference_output_human = reference.response

            aphrodite_output = client.do_aphrodite_query(
                "f7197f6c-e765-4b3d-abba-820725344726",
                question,
                test_case.start_date,
                test_case.end_date,
                test_case.report_type
            )

            print("===============================")
            print(" Question:\n")
            print(textwrap.fill(question,
                                74, initial_indent='\t', subsequent_indent='\t'))
            print("\n Reference Aphrodite:\n")
            print(textwrap.fill(reference_output_aphrodite,
                                74, initial_indent='\t', subsequent_indent='\t'))
            print("\n Reference Human:\n")
            print(textwrap.fill(reference_output_human,
                                74, initial_indent='\t', subsequent_indent='\t'))
            print("\n Aphrodite Output:\n")
            print(textwrap.fill(aphrodite_output,
                                74, initial_indent='\t', subsequent_indent='\t'))

            result_bleu_aphrodite = pb.Eval.compute_bleu(
                [reference_output_aphrodite],
                [aphrodite_output]
            )

            result_bleu_human = pb.Eval.compute_bleu(
                [reference_output_human],
                [aphrodite_output]
            )

            result_rouge_aphrodite = pb.Eval.compute_rouge(
                [reference_output_aphrodite],
                [aphrodite_output]
            )

            result_rouge_human = pb.Eval.compute_rouge(
                [reference_output_human],
                [aphrodite_output]
            )

            result_meteor_aphrodite = pb.Eval.compute_meteor(
                [reference_output_aphrodite],
                [aphrodite_output]
            )

            result_meteor_human = pb.Eval.compute_meteor(
                [aphrodite_output],
                [reference_output_human]
            ) 

            print("\n Results:\n")
            # BLEU score notes
            #  Anything that's > 0.3 is generally considered a good score
            #  Seems that it's not a good guage of accuracy, but how close the output is to reference, verbatim
            #  Hence, this seems to be good for checking whether Aphrodite's new answers
            #   stray too far from old answers
            print(f"\tBLEU Score (Aphrodite): {result_bleu_aphrodite}")
            print(f"\tBLEU Score (Human): {result_bleu_human}\n")

            if result_bleu_aphrodite >= 0.3:
                print(textwrap.fill(
                    "Based on the BLEU score, Aphrodite's current output is fairly consistent with previous output\n",
                    74, initial_indent='\t', subsequent_indent='\t')
                )
            elif result_bleu_aphrodite >= 0.2:
                print(textwrap.fill(
                    "Based on the BLEU score, Aphrodite's output is moderately different from previous output\n",
                    74, initial_indent='\t', subsequent_indent='\t')
                )
            else:
                print(textwrap.fill(
                    "Based on the BLEU score, Aphrodite's output is radically different from previous output\n",
                    74, initial_indent='\t', subsequent_indent='\t')
                )

            # METEOR score - like BLEU, except the Precision computation 
            #  corresponds to proportion of words that are in the output and correct
            #  and no brevity penalty
            #  Also uses corpus from nltk_data
            print(f"\n\tMETEOR Score (Aphrodite): {result_meteor_aphrodite}")
            print(f"\tMETEOR Score (Human): {result_meteor_human}\n")

            if result_meteor_human >= 0.3:
                print(textwrap.fill(
                    "Based on the METEOR score, most of the statements in the Human-generated reference are found in Aphrodite's output\n",
                    74, initial_indent='\t', subsequent_indent='\t')
                )
            elif result_meteor_human >= 0.2:
                print(textwrap.fill(
                    "Based on the METEOR score, some of the statements in the Human-generated reference were found in Aphrodite's output\n",
                    74, initial_indent='\t', subsequent_indent='\t')
                )
            else:
                print(textwrap.fill(
                    "Based on the METEOR score, few, if any of the statements in the Human-generated reference were found in Aphrodite's output\n",
                    74, initial_indent='\t', subsequent_indent='\t')
                )

            # A good ROUGE score varies by summarization task and metric. 
            #  ROUGE-1 scores are excellent around 0.5, with scores above 0.5 considered good and 0.4 to 0.5 moderate. 
            #  For ROUGE-2, scores above 0.4 are good, and 0.2 to 0.4 are moderate. 
            #  ROUGE-L scores are good around 0.4 and low at 0.3 to 0.4.
            #  Note: doesn't matter which is put in preds/gts - score remains the same
            print(f"\n\tROUGE-1 Score (Aphrodite): {result_rouge_aphrodite['rouge_1']}")
            print(f"\tROUGE-2 Score (Aphrodite): {result_rouge_aphrodite['rouge_2']}")
            print(f"\tROUGE-L Score (Aphrodite): {result_rouge_aphrodite['rouge_l']}")
            print(f"\tROUGE-1 Score (Human): {result_rouge_human['rouge_1']}")
            print(f"\tROUGE-2 Score (Human): {result_rouge_human['rouge_2']}")
            print(f"\tROUGE-L Score (Human): {result_rouge_human['rouge_l']}\n")

benchmark()
