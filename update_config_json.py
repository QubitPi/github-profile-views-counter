import json
import requests

URL_TEMPLATE = "https://api.github.com/users/QubitPi/repos?page={page}&per_page={per_page}"

def main():
    page = 1
    per_page = 30

    names = []

    while True:
        paged = [repo["name"] for repo in requests.get(url=URL_TEMPLATE.format(page=page, per_page=per_page)).json()]
        if len(paged) > 0:
            names += paged
            page += 1
        else:
            break

    f = open("config.json", "w")
    f.write(json.dumps({
        "devMode": "false",
        "advancedMode": "false",
        "language": "en-US",
        "repository": names
    }))
    f.write("\n")
    f.close()

    
if __name__ == '__main__':
    main()
