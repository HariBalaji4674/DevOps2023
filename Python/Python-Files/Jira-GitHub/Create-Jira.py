# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://abcdhari.atlassian.net/rest/api/3/issue"
# "https://your-domain.atlassian.net/rest/api/3/issue"
API_TOKEN = "ATATT3xFfGF0ALWU6BYiyB0m5aq7oFKVvF3iEq9nqGQzEWVUcYYZchhkNHo6_iTW1cWm4_z3Zp1xmKryRQSlXSXR8SnoRwa_6xzqbp-TDw2z8V677xsczkxXDSKMvAHKHKa31MJAh-vrPIl4evlPEQv-sKMM4s_KSzMCTd6-tNjbF5tKRI0m-qA=55871D7B"
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