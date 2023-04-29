from flask import Flask, request, jsonify
from biosppy.signals import ecg

app = Flask(__name__)


@app.route('/rr', methods=['POST'])
def rr():
    frequency = 125

    data = request.get_json()
    my_ecg = data['ecg']

    out = ecg.ecg(signal=my_ecg, sampling_rate=125, show=False)
    # pass ecg parameter to the function and get bpms
    # ecg model = [-200, -100, -56, 3, 200, ...]
    bpm = out["heart_rate"]
    # pass ecg parameter to the function and get the r peaks
    # ecg model = [-200, -100, -56, 3, 200, ...]
    rr_peaks = out["rpeaks"]
    int_rr_array = [int(item) for item in rr_peaks]
    int_bpm_array = [int(item) for item in bpm]

    return jsonify({'rr': int_rr_array, 'bpm': int_bpm_array})


if __name__ == '__main__':
    app.run()
