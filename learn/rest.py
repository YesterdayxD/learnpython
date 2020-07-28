import time

import requests

while True:
    time.sleep(5)
    try:
        r = requests.get("https://www.csdn.net/eee", timeout=1)
        print(r.status_code)
        r.raise_for_status()
    except requests.HTTPError as e:
        print(e)
        print(r.status_code)
    except Exception as e:
        print(e)
        print("other")
# print(r.headers)
# print(r.status_code)
#
# print(r.text)
# print(r.encoding)
# print(r.content)
