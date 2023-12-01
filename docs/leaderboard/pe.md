# Prompt Engineering Benchmark

The Prompt Engineering Module collects a variety of prompting methods and evaluates their performance across multiple datasets. This module currently supports models including GPT-3.5-turbo and GPT-4-1106.

Please contact us if you want the results of your models shown in this leaderboard.

### All Results

|  | GPT3.5 -Turbo |  |  |  | GPT4-1106 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | gsm8k | bigbench_date | bigbench_object_tracking | csqa | gsm8k | bigbench_date | bigbench_object_tracking | csqa |
| baseline | 47.15 | 57.99 | 39.2 | 72.48 | 92.19 | 87.80 | 96.27 | 79.69 |
| CoT | 40.33 | 49.32 | 63.20 | 67.81 | 85.89 | 92.14 | 90.26 | 85.59 |
| CoT(zero-shot) | 18.50 | 80.49 | 66.00 | 65.85 | 87.34 | 87.53 | 99.07 | 79.85 |
| expert prompting | 21.15 | 61.79 | 56.53 | 74.45 | 88.70 | 87.26 | 98.93 | 79.85 |
| emotion prompt | 57.24 | 66.12 | 29.87 | 70.68 | 90.83 | 87.80 | 95.73 | 80.34 |

|  | GPT3.5-Turbo |  | GPT4-1106 |  |
| --- | --- | --- | --- | --- |
|  | gsm8k | last-letter-concat | gsm8k | last-letter-concat |
| baseline | 47.15 | 7.2 | 92.19 | 25.2 |
| least to most | 75.28 | 79.8 | 79.38 | 96.2 |

*"This is very important to my career." is used in emotion prompt*