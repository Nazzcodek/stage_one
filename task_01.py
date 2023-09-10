from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info() -> dict:
    """
    Get information from query parameters and return a JSON response.

    Returns:
        dict: A JSON response containing the retrieved information.
    """
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day and time
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Define GitHub URLs
    github_repo_url = 'https://github.com/Nazzcodek/stage_one'
    github_file_url = 'https://github.com/Nazzcodek/stage_one/blob/master/task_01.py'

    # Create response dictionary
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    # Return JSON response
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
