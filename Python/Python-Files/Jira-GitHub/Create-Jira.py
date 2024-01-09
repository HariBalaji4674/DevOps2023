# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import numpy
url = "https://abcdhari1.atlassian.net/rest/api/3/issue"
# "https://your-domain.atlassian.net/rest/api/3/issue"
API_TOKEN = "ATATT3xFfGF03p8jdhyTRSS8TkIjIF6sVDj08BXu8iiPQhm7DgDJq9_xmaFHqsvg6yTsMuWrLgynTD7y3i61SudhrPWYQBJayoE79ltydmx17TL0w9AUe32ylKI_F05aIyH4t1O2JD3gTvIoOc0VkiUo7kiw9SdbEjPNz6ludZGr1jk1-HFOSjk=D1E0896C"
auth = HTTPBasicAuth("hari.balaji4674@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))