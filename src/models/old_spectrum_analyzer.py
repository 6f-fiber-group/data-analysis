import pathlib
import numpy as np
import pandas as pd

class OldSpectrumAnalyzer():
  def __init__(self, root):
    self.root = pathlib.Path(root)
    self.wavelength = []
    self.intensity = {}

    self.fill_data()

  def fill_data(self):
    data = self.get_old_spectrum_analyzer_data()

    self.wavelength = data["wavelength"]
    self.intensity = data["intensity"]

  def get_old_spectrum_analyzer_data(self):
    intensity = {}
    for f in self.root.iterdir():
        if f.suffix != ".txt":
            continue

        df = pd.read_csv(f, header=None, engine='python', sep="\t")
        intensity[f.stem] = df[1].tolist()

    return {
      "wavelength": df[0].tolist(),
      "intensity": intensity
      }
