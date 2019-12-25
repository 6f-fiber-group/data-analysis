import os
import sys
import yaml

path = os.path.join(os.path.dirname(__file__), "../features")
sys.path.append(path)

from flequency_characteristics_manager import FlequencyCharacteristicsrManager as FCM

path = os.path.join(os.path.dirname(__file__), "../libs")
sys.path.append(path)

from plot import Plot

def get_plot_data(params):
  if params["equip_type"] == "flequency_characteristics":
    sobj = FCM(params["data_path"])

  if params["calc_type"] == "diff":
    return sobj.diff(params["std_data_file"], params["convolve"])
  else:
    return sobj.flequency_characteristics(params["convolve"])

if __name__ == "__main__":
  data_path = r"data\20191225"
  with open(os.path.join(data_path, "params.yml"), "r") as f:
    params = yaml.safe_load(f)
    params["data_path"] = data_path

  plot_data = get_plot_data(params)

  pobj = Plot(params)
  pobj.plot(plot_data)