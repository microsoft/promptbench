# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

""" Setup
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
import pathlib

import pkg_resources

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# requirements
with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='promptbench',
    version='0.0.3',
    description='PromptBench is a powerful tool designed to scrutinize and analyze the interaction of large language models with various prompts. It provides a convenient infrastructure to simulate **black-box** adversarial  **prompt attacks** on the models and evaluate their performances.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/microsoft/promptbench',
    author='',
    author_email='',

    # Note that this is a string of words separated by whitespace, not a list.
    keywords='pytorch, large language models, prompt tuning, dyval, evaluation',
    packages=find_packages(exclude=['examples', 'imgs', 'docs']),
    include_package_data=True,
    # install_requires=['torch >= 1.8', 'torchvision', 'torchaudio', 'transformers', 'timm', 'progress', 'ruamel.yaml', 'scikit-image', 'scikit-learn', 'tensorflow', ''],
    install_requires=install_requires,
    python_requires='>=3.9',
)
