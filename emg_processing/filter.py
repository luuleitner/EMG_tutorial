import numpy as np
from scipy.signal import butter, lfilter

class Butter():
    def __init__(self, data, lowcut, highcut, fs, order):
        b,a=self.butter_bandpass(lowcut, highcut, fs, order=order)
        self.data_filtered = self.cut_filter_init(lfilter(b,a, data), cut=200)

    def butter_bandpass(self, lowcut, highcut, fs, order=4):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def cut_filter_init(self, data, cut=50):
        data[:cut] = 0
        return data


