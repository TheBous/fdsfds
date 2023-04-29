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
    int_array = [int(item) for item in rr_peaks]

    out = ecg.ecg(signal=my_ecg, sampling_rate=125, show=False)
    bpm = out["heart_rate"]

    return jsonify({'rr': int_array, 'bpm': bpm})


if __name__ == '__main__':
    app.run()
