from ecgdetectors import Detectors
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/rr', methods=['POST'])
def rr():
    detectors = Detectors(125)

    data = request.get_json()
    # pass ecg parameter to the function and get the r peaks
    # ecg model = [-200, -100, -56, 3, 200, ...]
    ecg = data['ecg']
    r_peaks_2 = detectors.engzee_detector(ecg)
    int_array = [int(item) for item in r_peaks_2]

    return jsonify({'rr': int_array})

if __name__ == '__main__':
    app.run()
