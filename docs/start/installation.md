# Installation

There are two ways to install promptbench. If you want to simply use as it is, install via `pip`. If you want to make any changes and play around, install it from source.

We recommend to build virtual environment via [anaconda/miniconda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) or [python virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to better manage your python library.



## Install via `pip`
We provide a Python package *promptbench* for users who want to start evaluation quickly. Simply run 
```sh
pip install promptbench
```


## Install via github

First, clone the repo:
```sh
git clone git@github.com:microsoft/promptbench.git
```

Then, 

```sh
cd promptbench
```

To install the required packages, you can create a conda environment:

```sh
conda create --name promptbench python=3.9
```

then use pip to install required packages:

```sh
pip install -r requirements.txt
```

Note that this only installed basic python packages. For Prompt Attacks, it requires to install textattacks.
