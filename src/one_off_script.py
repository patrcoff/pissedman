import requests

#uri = 'https://prod-43.eastus.logic.azure.com:443/workflows/9f78c92810d541b0859ad2d1e0d42d7a/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=DhZJwS9y-R4gIkQH9SO14XhgWMWH3HrpImuoxELXNQI'
uri = input('enter url:')
body = {
    'file': {
	    'url': 'https://solutions-reference.s3.amazonaws.com/landing-zone-accelerator-on-aws/latest/AWSAccelerator-InstallerStack.template',
	    'filename': 'CLE_demo'
        }
    }

response = requests.post(url=uri,json=body)
print(response)