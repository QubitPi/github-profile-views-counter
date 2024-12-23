# Copyright Jiaqi Liu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
    }, indent=4))
    f.write("\n")
    f.close()

    
if __name__ == '__main__':
    main()
