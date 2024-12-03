from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    # Fetch GitHub user statistics
    try:
        # Replace with your GitHub username
        username = 'hey-granth'

        # Fetch GitHub user profile
        profile_url = f'https://api.github.com/users/{username}'
        profile_response = requests.get(profile_url)
        profile_data = profile_response.json()

        # Fetch GitHub repositories
        repos_url = f'https://api.github.com/users/{username}/repos'
        repos_response = requests.get(repos_url)
        repos_data = repos_response.json()

        # Sort repositories by stars and most recent
        repos_data.sort(key=lambda x: x['stargazers_count'], reverse=True)

        return render_template('index.html',
                               profile=profile_data,
                               repos=repos_data)
    except Exception as e:
        print(f"Error fetching GitHub data: {e}")
        return render_template('index.html',
                               profile=None,
                               repos=None)


if __name__ == '__main__':
    app.run(debug=True)