from flask import Flask, request, jsonify
from biosppy.signals import ecg
import neurokit2 as nk
import heartpy as hp

app = Flask(__name__)

@app.route('/rr', methods=['POST'])
def rr():
    data = request.get_json()
    my_ecg = data['ecg']
    frequency = data['frequency']

    try:
        print("Starting evaluating ecg...", type(my_ecg))
        # signals, info = nk.ecg_process(ecg_signal=my_ecg, sampling_rate=frequency)
        # rpeaks_neuro = signals["ECG_R_Peaks"]
        # bpm_neuro = signals["ECG_Rate"]
        out_biosppy = ecg.ecg(signal=my_ecg, sampling_rate=frequency, show=False)

        rr_peaks_biosppy = out_biosppy["rpeaks"].tolist()
        bpm_peaks_biosppy = out_biosppy["heart_rate"].tolist()
        x_axis = out_biosppy["heart_rate_ts"].tolist()

        # wd, m = hp.process(hrdata=my_ecg, sample_rate=frequency, bpmmin=20, bpmmax=150)
        # rpeaks_py = wd["peaklist"]
        # bpm_heartpy = m["bpm"]
        # rr_interval_py = hp.analysis.calc_rr(peaklist=rr_peaks_biosppy, sample_rate=frequency)
        # rr_interval_py = hp.analysis.calc_rr(peaklist=rr_peaks_biosppy, sample_rate=frequency)
        # rr_list = rr_interval_py["RR_list"]

        # bpm_list = [] 
        # for rr_interval_ms in rr_list:
        #     rr_interval_s = rr_interval_ms / 1000
        #     bpm = 60 / rr_interval_s
        #     bpm_list.append(bpm) 

        # enhanced_peaks = hp.enhance_peaks(hrdata=my_ecg)

        print()
    except Exception as e:
        print(e)
        return jsonify({'error': True, 'rr': [], 'bpm': []})
    finally:
        print("Finished evaluating ecg!")

    # pass ecg parameter to the function and get bpms
    # ecg model = [-200, -100, -56, 3, 200, ...]

    # bpm = out["heart_rate"]

    # pass ecg parameter to the function and get the r peaks
    # ecg model = [-200, -100, -56, 3, 200, ...]
    # rr_peaks_biosppy = out["rpeaks"]
    # rr_peaks_biosppy = out["rpeaks"]
    # int_rr_array = [int(item) for item in rr_peaks_biosppy]
    # int_rr_array = [int(item) for item in rr_peaks_biosppy]
    # int_bpm_array = [int(item) for item in bpm]

    # cleaned_list = rpeaks.tolist()

    return jsonify({ 'rr': rr_peaks_biosppy, 'bpm': bpm_peaks_biosppy, 'xAxis': x_axis })


if __name__ == '__main__':
    app.run()
