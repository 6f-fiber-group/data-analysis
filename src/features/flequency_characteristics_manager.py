import pathlib
import numpy as np
import pandas as pd
import os
import sys

path = os.path.join(os.path.dirname(__file__), "../models")
sys.path.append(path)

path = os.path.join(os.path.dirname(__file__), "../libs")
sys.path.append(path)

import utils
from flequency_characteristics import FlequencyCharacteristics

class FlequencyCharacteristicsrManager(FlequencyCharacteristics):
  def __init__(self, root):
    super().__init__(root)

  def flequency_characteristics(self, convolve=0):
    return {
      "x": self.flequency,
      "y": self.convole(self.IO_ratio, convolve) if convolve else self.IO_ratio
    }

  def convole(self, data, win=5):
    if type(data) == dict:
      return {
        key: utils.convolve(val, win)
        for key, val in data.items()
      }