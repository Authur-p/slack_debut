from flask import Flask, jsonify, request
import datetime
import pytz
import random

app = Flask(__name__)

@app.route('/api')
def slack():

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    now = datetime.datetime.now()
    day = now.strftime('%A')
    the_utc = datetime.datetime.now(pytz.utc)
    offset_minutes = random.randint(-2, 2)
    offset_time = now + datetime.timedelta(minutes=offset_minutes)
    current_utc_time = offset_time.strftime('%Y-%m-%d %H:%M:%S UTC')
    return jsonify({
        'slack_name': slack_name,
        'day_of_the_week': day,
        'current_utc': current_utc_time,
        'track': track,
        'github_file_url': 'https://www.example.com',
        'github_repo_url': 'https://www.example/repo.com',
        'status': 200
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
