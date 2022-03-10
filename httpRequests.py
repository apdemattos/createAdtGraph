import asyncio
import requests

async def oauthLogin():
    url = 'http://localhost:5000/api/login'
    body = {"username": "", "password": ""}
    header = {'accept': '*/*'}
    r = requests.post(url, json=body, headers=header)
    return r.json()

async def getForgeToken():
    oathResponse = await oauthLogin()
    headers = {'Authorization': 'Bearer ' + oathResponse['responseData'][0]['token'], 'accept': '*/*'}
    url = 'http://localhost:5000/api/forge/oauth/token'
    r = requests.get(url, headers=headers)
    return r.json()

async def getModelList(urn):
    forgeRes = await getForgeToken()
    forgeToken = forgeRes['responseData']['dictionary']['access_token']
    headers = {'Authorization': 'Bearer ' + forgeRes['responseData']['dictionary']['access_token']}
    r = requests.get('https://developer.api.autodesk.com/modelderivative/v2/designdata/' + urn + '/metadata', headers=headers)
    return r.json()

async def getModelHigharchy(urn):
    forgeRes = await getForgeToken()
    forgeToken = forgeRes['responseData']['dictionary']['access_token']
    modelList = await getModelList(urn)
    guid = modelList['data']['metadata'][1]['guid']
    headers = {'Authorization': 'Bearer ' + forgeToken}
    r = requests.get('https://developer.api.autodesk.com/modelderivative/v2/designdata/' + urn + '/metadata/' + guid, headers=headers)
    return r.json()

async def getModelProperties(urn):
    forgeRes = await getForgeToken()
    forgeToken = forgeRes['responseData']['dictionary']['access_token']
    modelList = await getModelList(urn)
    guid = modelList['data']['metadata'][1]['guid']
    headers = {'Authorization': 'Bearer ' + forgeToken}
    r = requests.get('https://developer.api.autodesk.com/modelderivative/v2/designdata/' + urn + '/metadata/' + guid + '/properties?forceget=true', headers=headers)
    print('https://developer.api.autodesk.com/modelderivative/v2/designdata/' + urn + '/metadata/' + guid + '/properties?forceget=true')
    return r.json()