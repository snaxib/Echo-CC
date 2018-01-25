import requests
import json

AuthSettings = json.load(open('auth.json'))

def getAuthToken(user, pw):
  #print(str(user))
  #print(str(pw))
  r = requests.post('https://www.echomtg.com/api/user/auth/', data={'email':str(user),'password':str(pw)})
  responseBody = json.loads(r.text)
  if responseBody['status'] == 'success':
    return responseBody['token']
  else:
    print('Authentication error')
    print(r.text)

def buildCardList(token):
  cardRequest = requests.get('https://www.echomtg.com/api/stores/card_reference/auth=' + str(token))
  #print(cardRequest.text)
  cardResponse = json.loads(cardRequest.text)
  cardList = cardResponse['cards']
  cardFile = open('cardList.json', 'w')
  cardFile.write(str(cardList))
  cardFile.close()


AuthToken = getAuthToken(AuthSettings['username'], AuthSettings['password'])

buildCardList(AuthToken)
