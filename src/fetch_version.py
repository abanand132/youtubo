import requests

def repo_version():
    response = requests.get(url="https://raw.githubusercontent.com/abanand132/youtubo/main/src/version.txt")
    data = float(response.text)
    return data
