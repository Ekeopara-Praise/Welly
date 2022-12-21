import pandas as pd
from IsochronalTest import Isochronal

df = pd.read_csv('test_data.csv')
df['psq'] = 1798 ** 2 - df['P'] ** 2
print(df.head())

iso = Isochronal(df, 1798, 'Qg', 'psq', 6300, 1600)
print(f"n = {iso.n_factor()}")
print(f"c = {iso.c_factor()}")
print(f"IPR equation is: {iso.IPR()}")
print(f"AOF = {iso.AOF()}Mscf/d", )
print(iso.pressure_squared_graph())
















# class GasTest:
#
#     def __init__(self, dataset=None):
#         self.dataset = dataset
#
#         if dataset is None:
#             self.dataset = []
#         # self.data = self.dataset
#         self.dataset = self.dataset
#
#
# # slope = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[0]
#         # intercept = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[1]
#         #
#         # def abline(slope, intercept):
#         #     axes = plt.gca()
#         #     x_vals = np.array(axes.get_xlim())
#         #     y_vals = intercept + slope * x_vals
#         #     plt.plot(x_vals, y_vals, '--')
#         #
#         # plt.scatter(np.log(self.data[q_column]), np.log(self.data[psd_column]))
#         # print(abline(slope, intercept))

