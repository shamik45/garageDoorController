__author__ = 'shamik.shah'
import httplib2
import ConfigParser
import json

config = ConfigParser.RawConfigParser()
config.read('creds.cfg')

username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')
appId = config.get('Credentials', 'appId')


#print("username " + username);


requestUrl = "https://myqexternal.myqdevice.com/Membership/ValidateUserWithCulture?appId=" + appId + "&username=" + username + "&password=" + password + "&culture=en"
resp, content = httplib2.Http().request(requestUrl)
#print resp
#print content

j = json.loads(content);
#print j['SecurityToken']


doorStateUrl = "http://myqexternal.myqdevice.com/Device/getDeviceAttribute?appId=" + appId + "&securityToken=" + j['SecurityToken'] + "&name=doorstate&devId=234909079"
respDS, contentDS = httplib2.Http().request(doorStateUrl)

#print contentDS
doorStateJson = json.loads(contentDS)

def doorStateDictionary(x):
    return{
        '2': "closed",
        '1':"open"
    } [x]

#print doorStateJson['AttributeValue']
print doorStateDictionary(doorStateJson['AttributeValue'])



