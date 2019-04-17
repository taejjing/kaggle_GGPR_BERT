"""

https://www.kaggle.com/kashnitsky/simple-logistic-regression-bert-0-27-lb
https://arxiv.org/abs/1810.04805.

BERT (Bidirectional Embedding Representations from Trnasformers)
is a new method of pre-training language representations which obtains state-of-the-art rseults
on a wide array of Natural Language Processing (NLP) tasks.

"""
import datetime
import json
import os
import pprint
import string
import sys
import tensorflow as tf

from load_data import load_data

load_data()