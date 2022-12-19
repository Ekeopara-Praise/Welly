import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from WellTests import GasTest


class Isochronal(GasTest):

    def __init__(self, data=None):
        GasTest.__init__(self, dataset=None)
        self.data = data

        if self.data is None:
            self.data = self.dataset

    def n_factor(self, q_column, psd_column):

        slope = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[0]

        return 1 / slope

    def c_factor(self, Qstable, Prstable, Pwfstable):

        return Qstable / (Prstable ** 2 - Pwfstable ** 2) ** self.n_factor()

    def IPR_equation(self):

        return f"Qg = {round(self.c_factor(), 4)}(Pr^2 - Pwf^2)^{round(self.n_factor(), 4)}"

    def pressure_squared_graph(self, q_column, psd_column):

        slope = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[0]
        intercept = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[1]

        def abline(slope, intercept):
            axes = plt.gca()
            x_vals = np.array(axes.get_xlim())
            y_vals = intercept + slope * x_vals
            plt.plot(x_vals, y_vals, '--')

        plt.scatter(np.log(self.data[q_column]), np.log(self.data[psd_column]))
        print(abline(slope, intercept))

        plt.show()

    def AOF(self, Pr):
        Qmax = self.c_factor() * ((Pr ** 2 - 14.73 ** 2) ** self.n_factor())

        return Qmax


df = pd.read_csv('test_data.csv')
df['psq'] = 3360 ** 2 - df['P'] ** 2
iso = Isochronal(df)
# print(iso.pressure_squared_graph('Qg', 'psq'))
print(iso.n_factor('Qg', 'psq'))