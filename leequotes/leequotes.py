import os
import random as rdm


def random() -> str:
    filepath = os.path.join(os.path.dirname(__file__), "quotes.tsv")

    with open(filepath) as f:
        lines = f.readlines()[1:]
        quote_column_index = 1
        return rdm.choice(lines).split("\t")[quote_column_index].strip()
