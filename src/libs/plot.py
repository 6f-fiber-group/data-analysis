import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import utils

utils.set_plot_params()
ls = ["-", "--", "-.", ":"]

class Plot():
  def __init__(self, params):
    self.params = params

  def set_params(self):
    plt.xlabel(self.params["xlabel"])
    plt.ylabel(self.params["ylabel"])
    plt.xlim(self.params["xlim"] if self.params["xlim"] else plt.xlim())
    plt.ylim(self.params["ylim"] if self.params["ylim"] else plt.ylim())
    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")

    if self.params["xtick_num"]:
      st, ed = plt.xlim()
      plt.xticks(np.linspace(st, ed, self.params["xtick_num"]))

  def save_fig(self, fig):
    save_file_path = os.path.join(self.params["data_path"], "figs")

    if not os.path.exists(save_file_path):
      os.makedirs(save_file_path)
    if not self.params["fig_name"]:
      self.params["fig_name"] = str(datetime.date.today())

    fig.savefig(
      os.path.join(save_file_path, "{}.png".format(self.params["fig_name"])),
      dpi=200, bbox_inches="tight"
    )

  def plot(self, data):
    fig = plt.figure(figsize=self.params["fig_size"])
    
    data_len = len(data["x"])
    for idx, d in enumerate(zip(data["x"].items(), data["y"].items())):
      x, y = d
      xkey, xval = x
      ykey, yval = y
      plt.plot(xval, yval, label=xkey, ls=ls[(data_len + idx) % len(ls)], lw=3)

    self.set_params()
    plt.show()
    self.save_fig(fig)