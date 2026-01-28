from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

@app.route('/time')
def get_time():
    now = datetime.now(pytz.UTC)
    return {
        'timestamp': now.isoformat(),
        'date': now.strftime('%Y-%m-%d'),
        'time': now.strftime('%H:%M:%S'),
        'timezone': 'UTC',
        'human_readable': now.strftime('%A, %B %d, %Y at %I:%M:%S %p')
    }, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
