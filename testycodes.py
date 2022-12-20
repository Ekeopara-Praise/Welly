class GasTest:

    def __init__(self, dataset=None):
        self.dataset = dataset

        if dataset is None:
            self.dataset = []
        # self.data = self.dataset
        self.dataset = self.dataset


# slope = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[0]
        # intercept = np.polyfit(np.log(self.data[q_column]), np.log(self.data[psd_column]), 1)[1]
        #
        # def abline(slope, intercept):
        #     axes = plt.gca()
        #     x_vals = np.array(axes.get_xlim())
        #     y_vals = intercept + slope * x_vals
        #     plt.plot(x_vals, y_vals, '--')
        #
        # plt.scatter(np.log(self.data[q_column]), np.log(self.data[psd_column]))
        # print(abline(slope, intercept))

