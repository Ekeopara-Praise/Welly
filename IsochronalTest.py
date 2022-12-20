import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Isochronal:

    def __init__(self, data, Pr, q_column, psd_column, Qstable, Pwfstable):

        self.data = data
        self.q_column = q_column
        self.psd_column = psd_column
        self.Qstable = Qstable
        self.Pwfstable = Pwfstable
        self.Pr = Pr

        global slope
        global intercept

        slope = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[0]
        intercept = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[1]

    def n_factor(self):

        return round(1 / slope, 4)

    def c_factor(self):

        return round(self.Qstable / (self.Pr ** 2 - self.Pwfstable ** 2) ** self.n_factor(), 4)

    def IPR_equation(self):

        return f"Qg = {round(self.c_factor(), 4)}(Pr^2 - Pwf^2)^{round(self.n_factor(), 4)}"

    def pressure_squared_graph(self):

        plt.figure(figsize=(8, 6))
        plt.loglog(self.data[self.q_column], self.data[self.psd_column])

        plt.scatter(self.data[self.q_column], self.data[self.psd_column], color='r')
        plt.xlabel('Qg, Mscf/d')
        plt.ylabel('Pressure squared, psi^2')
        plt.show()

    def AOF(self):

        Qmax = self.c_factor() * ((self.Pr ** 2 - 14.73 ** 2) ** self.n_factor())

        return round(Qmax, 4)


df = pd.read_csv('test_data.csv')
df['psq'] = 1798 ** 2 - df['P'] ** 2
print(df.head())

iso = Isochronal(df, 1798, 'Qg', 'psq', 6300, 1600)
print("n =", iso.n_factor())
print("c =", iso.c_factor())
print("IPR equation is", iso.IPR_equation())
print("AOF =", iso.AOF())
print(iso.pressure_squared_graph())
