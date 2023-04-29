from ecgdetectors import Detectors
from flask import Flask, request, jsonify
from biosppy.signals import ecg

app = Flask(__name__)


@app.route('/rr', methods=['POST'])
def rr():
    frequency = 125
    detectors = Detectors(frequency)

    data = request.get_json()
    # pass ecg parameter to the function and get the r peaks
    # ecg model = [-200, -100, -56, 3, 200, ...]
    my_ecg = data['ecg']
    rr_peaks = detectors.engzee_detector(my_ecg)
    int_rr_array = [int(item) for item in rr_peaks]

    out = ecg.ecg(signal=my_ecg, sampling_rate=125, show=False)
    bpm = out["heart_rate"]
    int_bpm_array = [int(item) for item in bpm]

    return jsonify({'rr': int_rr_array, 'bpm': int_bpm_array})


if __name__ == '__main__':
    app.run()
