#test
import numpy as np # linear algebra
import pandas as pd # data processing
import re
from transformers import pipeline

movies = pd.read_csv("movie_test.csv")
movies.head()