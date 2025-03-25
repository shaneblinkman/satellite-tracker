from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iss-location')
def get_iss_location():
    # Fetch ISS location from Open Notify API
    response = requests.get('http://api.open-notify.org/iss-now.json')
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'latitude': float(data['iss_position']['latitude']),
            'longitude': float(data['iss_position']['longitude']),
            'timestamp': data['timestamp']
        })
    return jsonify({'error': 'Failed to fetch ISS location'}), 500

if __name__ == '__main__':
    app.run(debug=True)
