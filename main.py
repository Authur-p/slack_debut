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
    offset_time = the_utc + datetime.timedelta(minutes=offset_minutes)

    current_utc_time = offset_time.strftime("%Y-%m-%d %H:%M:%S")
    current_utc_time = "T".join(current_utc_time.split(' ')) + 'Z'
    print(current_utc_time)

    return jsonify({
        'slack_name': slack_name,
        'current_day': day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': 'https://github.com/Authur-p/slack_debut/blob/main/main.py',
        'github_repo_url': 'https://github.com/Authur-p/slack_debut/tree/main',
        'status': 200
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
