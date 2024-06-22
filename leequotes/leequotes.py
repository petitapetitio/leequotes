import random as rdm
import importlib.resources as ressources
from leequotes import data


def random() -> str:
    filepath = ressources.files(data) / "quotes.tsv"
    with filepath.open() as f:
        lines = f.readlines()[1:]
        quote_column_index = 1
        return rdm.choice(lines).split("\t")[quote_column_index].strip()
