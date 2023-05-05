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
        out_biosppy = ecg.ecg(signal=my_ecg, sampling_rate=frequency, show=False)

        rr_peaks_biosppy = out_biosppy["rpeaks"].tolist()
        bpm_peaks_biosppy = out_biosppy["heart_rate"].tolist()
        x_axis = out_biosppy["heart_rate_ts"].tolist()

        print()
    except Exception as e:
        print(e)
        return jsonify({'error': True, 'rr': [], 'bpm': []})
    finally:
        print("Finished evaluating ecg!")

    return jsonify({ 'rr': rr_peaks_biosppy, 'bpm': bpm_peaks_biosppy, 'xAxis': x_axis })


if __name__ == '__main__':
    app.run()
