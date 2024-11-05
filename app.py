from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/api/ipinfo', methods=['GET'])
def get_ip_info():
    """Fetch IP information from ipapi.co and return as JSON."""
    try:
        response = requests.get('https://ipapi.co/json/')
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        data = response.json()
        return jsonify(data)
    except requests.RequestException as e:
        # Handle request errors and return a JSON error response
        return jsonify({'error': 'Failed to retrieve IP information', 'details': str(e)}), 500

@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('index.html')

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)