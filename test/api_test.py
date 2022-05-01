import json

import requests


def main():
    url = "https://f8iakd.deta.dev/"
    data = {
        'x': 3,
        'y': 4
    }

    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == '__main__':
    main()
