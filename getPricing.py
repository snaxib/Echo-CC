import requests
import json
import csv

Settings = json.load(open('settings.json'))


def getAuthToken(user, pw):
  r = requests.post('https://www.echomtg.com/api/user/auth/',
                    data={'email': str(user), 'password': str(pw)})
  responseBody = json.loads(r.text)
  if responseBody['status'] == 'success':
    return responseBody['token']
  else:
    print('Authentication error')
    print(r.text)


def buildCardReferenceList(token):
  cardRequest = requests.get(
      'https://www.echomtg.com/api/stores/card_reference/auth=' + str(token))
  cardResponse = cardRequest.json()
  cardList = cardResponse['cards']
  return cardList


def getNewPrices(token):
  priceRequest = requests.get(
      'https://www.echomtg.com/api/stores/price_reference/auth=' + str(token))
  priceResponse = priceRequest.json()
  priceList = priceResponse['suggested_prices']
  return priceList


def outputCSV(reference, prices):
  with open('priceUpdate.csv', 'w') as csvfile:
    rowwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    rowwriter.writerow(['Product Name', 'Set Name', 'Sell Price'])
    for card, data in prices.items():
      rowwriter.writerow([reference[str(card)]['name'],
                          reference[str(card)]['expansion'], data['price']])


AuthToken = getAuthToken(Settings['username'], Settings['password'])

cardReference = buildCardReferenceList(AuthToken)

priceList = getNewPrices(AuthToken)

outputCSV(cardReference, priceList)
