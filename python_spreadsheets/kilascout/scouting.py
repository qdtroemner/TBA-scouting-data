import pandas as pd
import matplotlib.pyplot as plt

class Scouting:
	def __init__(self, data:str):
		self.data = pd.read_excel(data).set_index("Unnamed: 0")
		self.data.index.name = "Team"

	def get_dataframe(self):
		return self.data

	def plot_stat_sums(self):
		keys = ["CCWM", "OPR", "DPR"]
		data_copy = self.data
		data_copy["sum"] = data_copy[keys].sum(axis=1)
		data_copy.sort_values("sum").plot(y=keys, kind="barh", stacked=True)
		plt.show()

	def plot_avg_sums(self):
		keys = ["Ranking Score", "Avg Match", "Avg Hangar", "Avg Taxi + Auto Cargo"]
		data_copy = self.data
		data_copy["sum"] = data_copy[keys].sum(axis=1)
		data_copy.sort_values("sum").plot(y=keys, kind="barh", stacked=True)
		plt.show()

	def plot_all_sums(self):
		keys = ["CCWM", "OPR", "DPR", "Ranking Score", "Avg Match", "Avg Hangar", "Avg Taxi + Auto Cargo"]
		data_copy = self.data
		data_copy["sum"] = data_copy[keys].sum(axis=1)
		data_copy.sort_values("sum").plot(y=keys, kind="barh", stacked=True)
		plt.show()