import requests
import json
import sys

#api_key is passed as an argument
api_key = sys.argv[1]

headers = {
    "x-cisco-meraki-api-key": api_key,
    "content-type": "application/json"
    }

url = "https://dashboard.meraki.com/api/v0/organizations"

def get_organizations(headers, url):
    """
    This function will return a list of Organizations that the user has privileges on
    arguments: headers and url
    """
    response = requests.request("GET", url, headers=headers)
    organizations_number = len(response.json())
    list_organizations = []
    for i in range(organizations_number):
        list_organizations.append(response.json()[i]['id'])
    return list_organizations

if __name__ == "__main__":
    print get_organizations(headers, url)
