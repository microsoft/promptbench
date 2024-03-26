# Prompt Engineering Benchmark

The Prompt Engineering Module collects a variety of prompting methods and evaluates their performance across multiple datasets. This module currently supports models including GPT-3.5-turbo and GPT-4-1106.

Please contact us if you want the results of your models shown in this leaderboard.

### All Results

| Model           | benchmark               | baseline | CoT   | CoT(zero-shot) | expert prompting | emotion prompt | least to most |
|-----------------|-------------------------|----------|-------|----------------|------------------|----------------|---------------|
| GPT3.5 -Turbo   | gsm8k                   | 47.15    | 40.33 | 18.5           | 21.15            | 57.24          |               |
| GPT3.5 -Turbo   | bigbench_date           | 57.99    | 49.32 | 80.49          | 61.79            | 66.12          |               |
| GPT3.5 -Turbo   | bigbench_object_tracking| 39.2     | 63.2  | 66             | 56.53            | 29.87          |               |
| GPT3.5 -Turbo   | csqa                    | 72.48    | 67.81 | 65.85          | 74.45            | 70.68          |               |
| GPT3.5 -Turbo   | last-letter-concat      | 7.2      |       |                |                  |                | 79.8          |
| GPT4-1106       | gsm8k                   | 92.19    | 85.89 | 87.34          | 88.7             | 90.83          |               |
| GPT4-1106       | bigbench_date           | 87.8     | 92.14 | 87.53          | 87.26            | 87.8           |               |
| GPT4-1106       | bigbench_object_tracking| 96.27    | 90.26 | 99.07          | 98.93            | 95.73          |               |
| GPT4-1106       | csqa                    | 79.69    | 85.59 | 79.85          | 79.85            | 80.34          |               |
| GPT4-1106       | last-letter-concat      | 25.2     |       |                |                  |                | 96.2          |

*"This is very important to my career." is used in emotion prompt*
