import requests

api_key = 'EKyZBSyIiPUwIthZAigQcg'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'url' : 'https://www.linkedin.com/in/muhammad-fariz-b90839226/'
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

print(response.json())