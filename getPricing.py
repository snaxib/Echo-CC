import requests
import json

def getAuthToken(user, pw):
	r = requests.post('https://www.echomtg.com/api/user/auth/', data={'email':str(user),'password':str(pw)})
	responseBody = json.loads(r.text)
	if responseBody['status'] == 'success':
		return responseBody['token']
	else:
		print('Authentication error')
		print(r.text)


print(getAuthToken('poop@poop.com', 'poop'))
