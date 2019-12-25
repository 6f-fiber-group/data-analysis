import pathlib
import csv
import numpy as np
import pandas as pd

class NewSpectrumAnalyzer():
  def __init__(self, root):
    self.root = pathlib.Path(root)
    self.wavelength = {}
    self.intensity = {}

    self.fill_data()

  def fill_data(self):
    data = self.get_new_spectrum_analyzer_data()

    self.wavelength = data["wl"]
    self.intensity = data["it"]

  def get_new_spectrum_analyzer_data(self):
    wl = {}
    it = {}
    for f in self.root.iterdir():
        if f.suffix != ".CSV":
            continue

        df = self.read_csv_data(f)
        wl[f.stem] = df[0].tolist()
        it[f.stem] = df[1].tolist()

    return {"wl": wl, "it": it}

  def read_csv_data(self, csv_file):
    with open(csv_file, "r") as f:
        data = list(csv.reader(f))

        for idx, d in enumerate(data):
            if d and '[TRACE DATA]' == d[0]:
                read_from = idx + 1
                break

    return pd.DataFrame(data[read_from:], columns=None).astype(float)
