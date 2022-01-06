import numpy as np
import pandas as pd
from scipy import signal
from matplotlib import pyplot as plt
from emg_processing.filter import Butter


ARG_FILE_PATH = 'C:/Users/chule/OneDrive/003_USLOCOMOTOR_GitREPO/EMG_tutorial/bbcontractions.csv'
#EMG_data = np.genfromtxt(ARG_FILE_PATH, delimiter=',')
EMG_data = pd.read_csv(ARG_FILE_PATH, sep=',').to_numpy()
EMG_data = np.ravel(EMG_data[:, 0])

ARG_SAMPLING_RATE = 1000
ARG_BPF_N = 4
ARG_BPF_LOW = 20
ARG_BPF_HIGH = 320


EMG_data_filtered = Butter(EMG_data, ARG_BPF_LOW, ARG_BPF_HIGH, ARG_SAMPLING_RATE, order=ARG_BPF_N)

# fig = plt.figure(figsize=(6,9), dpi = 300)
# ax_1 = fig.add_subplot(211)
# ax_1.plot(EMG_data,
#           markersize = 1,
#           color='blue',
#           label = 'x')
# ax_1.set_ylabel('EMG raw [uV]')
# ax_1.grid()
#
# ax_2 = fig.add_subplot(212)
# ax_2.plot(EMG_data_filtered.data_filtered,
#           markersize = 1,
#           color='red',
#           label = 'x')
# ax_2.set_ylabel('EMG filtered [uV]')
# ax_2.set_xlabel('Samples')
# ax_2.grid()
#
# plt.subplots_adjust(hspace=0.2)
# plt.show()


## Welch's Power Spectrum
f, Pxx_den = signal.welch(EMG_data_filtered.data_filtered, ARG_SAMPLING_RATE, nperseg=1024)
fig1 = plt.figure(figsize=(6,3), dpi = 300)
ax_1 = fig1.add_subplot(111)
ax_1.plot(f, Pxx_den,
          markersize = 1,
          color='blue',
          label = 'x')
ax_1.set_xlabel('Frequency [Hz]')
ax_1.set_ylabel('Power [W/Hz]')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax_1.yaxis.major.formatter._useMathText = True
plt.show()

P_AOC = np.sum(Pxx_den)
P_norm = Pxx_den / sg
mnf = np.sum(f.T * gn)