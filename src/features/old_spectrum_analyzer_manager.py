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
from old_spectrum_analyzer import OldSpectrumAnalyzer

class OldSpectrumAnalyzerManager(OldSpectrumAnalyzer):
  def __init__(self, root):
    super().__init__(root)

  def raw_data(self, convolve=0):
    return {
      "x": self.wavelength,
      "y": self.convole(self.intensity, convolve) if convolve else self.intensity
    }

  def diff(self, std_key, convolve=0):
    diff_intensity = {
      key: list(map(lambda a, b: a - b, val, self.intensity[std_key]))
      for key, val in self.intensity.items()
    }

    return {
      "x": self.wavelength,
      "y": self.convole(diff_intensity, convolve) if convolve else diff_intensity 
    }

  def normalize(self, std_key, convolve=0):
    normalized_intensity = {
      key: list(map(lambda a, b: a / b, val, self.intensity[std_key]))
      for key, val in self.intensity.items()
    }

    return {
      "x": self.wavelength,
      "y": self.convole(normalized_intensity, convolve) if convolve else normalized_intensity 
    }

  def convole(self, data, win=5):
    if type(data) == dict:
      return {
        key: utils.convolve(val, win)
        for key, val in data.items()
      }