import pathlib
import numpy as np
import pandas as pd

class FlequencyCharacteristics():
  def __init__(self, root):
    self.root = pathlib.Path(root)
    self.flequency = {}
    self.sensitivity = {}
    self.reference = {}
    self.phase_shift = {}

    self.fill_data()

  def fill_data(self):
    data = self.get_flequency_characteristics_data()

    self.flequency = data["freq"]
    self.sensitivity = data["sen"]
    self.reference = data["ref"]
    self.IO_ratio = data["IO"]
    self.phase_shift = data["ps"]

  def get_flequency_characteristics_data(self):
    fleq = {}
    sen = {}
    ref = {}
    IO = {}
    ps = {}
    for f in self.root.iterdir():
        if f.suffix != ".csv":
            continue

        df = pd.read_csv(f, engine='python')

        fleq[f.stem] = df["Freq [Hz]"].tolist()
        sen[f.stem] = df["Sens [dB]"].tolist()
        ref[f.stem] = df["Ref [a.u.]"].tolist()
        IO[f.stem] = df["I/O ratio [dB/a.u.]"].tolist()
        ps[f.stem] = df["Phase Shift [rad]"].tolist()

    return {
      "freq": fleq,
      "sen": sen,
      "ref": ref,
      "IO": IO,
      "ps": ps,
      }
