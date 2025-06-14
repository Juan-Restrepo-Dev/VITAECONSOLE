
import csv
import io
from textual.demo.data import COUNTRIES, DUNE_BIOS, MOVIES, MOVIES_TREE

ROWS = list(csv.reader(io.StringIO(MOVIES)))


print(ROWS)