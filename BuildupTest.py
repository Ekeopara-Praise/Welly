# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


class Horners:

    def __init__(self, data, Hp, Pws, rw, h, ct, visc, B, poro, q, Sw, Np):
        self.rw = rw
        self.h = h
        self.ct = ct
        self.visc = visc
        self.B = B
        self.poro = poro
        self.q = q
        self.Sw = Sw
        self.Np = Np
        self.data = data
        self.Hp = Hp
        self.Pws = Pws

        global slope
        global intercept
        global coeff

        slope = np.polyfit(np.log(self.data[Hp]), self.data[Pws], 3)[0]
        intercept = np.polyfit(np.log(self.data[Hp]), self.data[Pws], 3)[1]
        coeff = np.polyfit(np.log(self.data[Hp]), self.data[Pws], 3)


    def getCoeff(self):

        return np.poly1d(coeff)

    def hornersplot(self):

        # set up the figure sizes
        plt.figure(figsize=(8, 6))
        plt.style.use('grayscale')

        # plot of the log-log graph
        plt.semilogx(self.data[self.Hp], self.data[self.Pws])

        # # the scatter plot
        # plt.scatter(self.data[self.q_column], self.data[self.psd_column], color='r')

        # define the labels for the graph
        plt.title("Honers Plot", fontweight='bold', fontsize=20)
        plt.xlabel('Hp', fontweight='bold', fontsize=15)
        plt.ylabel('Pws, Psi', fontweight='bold', fontsize=15)
        plt.grid(visible=True)
        plt.show()

    def permeability(self):
        k = (162.6 * self.q * self.B * self.visc) / (slope * self.h)

        return round(k, 2)

    def initial_pressure(self):

        return intercept + slope * 1

    def skin(self, Pws_0):
        tp = (24 * self.Np) / self.q
        P1hr = intercept + slope * (tp + 1)

        s = 1.15 * (((P1hr - Pws_0)/slope) - np.log(self.permeability() / self.poro * self.visc * self.ct * (self.rw**2)) + 3.23)

        if s > 0:
            return f"The skin is {round(s, 3)} and this implies that the well is damaged"
        elif s < 0:
            return f"The skin is {round(s, 3)} and this implies that the well is stimulated"
        else:
            return f"The skin is {s} and this implies that the well is neither stimulated nor damaged"

    def m(self):
        return slope, intercept

h_df = pd.read_csv('horner_data.csv')
tp = (24 * 2780) / 385

# Pws_0 = 3534
h_df['Hp'] = (tp + h_df['∆t_hr']) / h_df['∆t_hr']
hon = Horners(h_df, 'Hp', 'Pws_psia', 0.25, 36, 11*10**-6, 0.75, 1.67, 0.13, 385, 0.35, 2780)
# print(h_df.head())
# data, Hp, Pws, rw, h, ct, visc, B, poro, q, Sw, Np

# print(hon.permeability())
print(hon.hornersplot())
# print(hon.m())
# print(hon.getCoeff())
print(hon.test())
