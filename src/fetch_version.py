import requests

def repo_version():
    response = requests.get(url="https://raw.githubusercontent.com/abanand132/demo-repo/main/version.txt")
    data = float(response.text)
    return data
