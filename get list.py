import requests
import json
import urllib3

# Disable SSL warnings (be cautious with this in a production environment)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the connection details
base_url = 'http://your-microstrategy-server/MicroStrategyLibrary/api'
username = 'your_username'
password = 'your_password'

def connect(base_url, username, password):
    """Establishes a session with the MicroStrategy server."""
    auth_url = f'{base_url}/auth/login'
    auth_body = {
        "username": username,
        "password": password,
        "loginMode": 1  # Standard login mode
    }
    response = requests.post(auth_url, json=auth_body, verify=False)
    if response.ok:
        return response.headers.get('X-MSTR-AuthToken')
    else:
        raise ConnectionError("Authentication Failed")

def get_projects(base_url, auth_token):
    """Retrieves a list of projects from the MicroStrategy server."""
    projects_url = f'{base_url}/projects'
    headers = {'X-MSTR-AuthToken': auth_token}
    response = requests.get(projects_url, headers=headers, verify=False)
    if response.ok:
        return json.loads(response.text)
    else:
        raise RuntimeError("Failed to retrieve projects")

def disconnect(base_url, auth_token):
    """Ends the session with the MicroStrategy server."""
    logout_url = f'{base_url}/auth/logout'
    headers = {'X-MSTR-AuthToken': auth_token}
    response = requests.post(logout_url, headers=headers, verify=False)
    if not response.ok:
        raise RuntimeError("Failed to end the session properly")

# Usage
try:
    auth_token = connect(base_url, username, password)
    projects = get_projects(base_url, auth_token)
    print(projects)
    disconnect(base_url, auth_token)
except Exception as e:
    print(f'An error occurred: {str(e)}')