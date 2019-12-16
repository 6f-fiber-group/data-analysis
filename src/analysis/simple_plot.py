import os
import sys
import yaml

path = os.path.join(os.path.dirname(__file__), "../features")
sys.path.append(path)

from old_spectrum_analyzer_manager import OldSpectrumAnalyzerManager as OSAM
from new_spectrum_analyzer_manager import NewSpectrumAnalyzerManager as NSAM

path = os.path.join(os.path.dirname(__file__), "../libs")
sys.path.append(path)

import utils
from plot import Plot

utils.set_plot_params()
ls = ["-", "--", "-.", ":"]

def get_plot_data(params):
  if params["equip_type"] == "old_spectrum_analyzer":
    sobj = OSAM(params["data_path"])
  elif params["equip_type"] == "new_spectrum_analyzer":
    sobj = NSAM(params["data_path"])

  if params["calc_type"] == "diff":
    return sobj.diff(params["std_data_file"], params["convolve"])
  else:
    return sobj.raw_data(params["convolve"])

if __name__ == "__main__":
  data_path = r"put path here"
  with open(os.path.join(data_path, "params.yml"), "r") as f:
    params = yaml.safe_load(f)
    params["data_path"] = data_path

  plot_data = get_plot_data(params)

  pobj = Plot(params)
  pobj.plot(plot_data)