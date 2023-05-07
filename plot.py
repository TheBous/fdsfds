import json
import time
from biosppy.signals import ecg
import neurokit2 as nk
import heartpy as hp
import pylab

with open('./20230502T210934Z_223430000028_ecg_stream.json', 'r') as json_file:
    data = json.load(json_file)

data_key = data['data']    

array_flatten = []

for obj in data_key:
    misurazioni = obj["ecg"]["Samples"]
    array_flatten.extend(misurazioni)

start_time = time.time()

# out_biosppy = ecg.ecg(signal=array_flatten, sampling_rate=125, show=True)
# _, rpeaks = nk.ecg_peaks(ecg_cleaned=array_flatten, sampling_rate=125)
# plot = nk.events_plot(rpeaks['ECG_R_Peaks'], array_flatten)

half_length = len(array_flatten)
first_half = array_flatten[300000:400000]
signals, info = nk.ecg_process(array_flatten, sampling_rate=125)
end_time = time.time()
execution_time = end_time - start_time
print("Tempo impiegato:", execution_time, "secondi")

nk.ecg_plot(signals, sampling_rate=125)
pylab.show()
pylab.ion()
# _, waves_peak = nk.ecg_delineate(array_flatten, rpeaks, sampling_rate=125, method="dwt", show=True)


# rr_peaks_biosppy = out_biosppy["rpeaks"].tolist()
# bpm_peaks_biosppy = out_biosppy["heart_rate"].tolist()

# print(rr_peaks_biosppy)