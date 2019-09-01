import json
import urllib.parse
import urllib.request
import ssl
import sys
from  BCFPOD1 import URL, USER, PASSWORD, TOKEN, POD



class bcf_session():
    def __init__(self, url, user, passwd, token, pod):
        self.base_url = url
        self.user = user
        self.passwd = passwd
        self.token = token
        self.pod = pod


    def baseURL(self):
        base_url = self.base_url
        #print(base_url)
        return base_url

    def podname(self):
        pod = self.pod
        #print(pod)
        return pod

    def authentication(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        cookie = self.token
        creds = {'user':'{}'.format(self.user), 'password':'{}'.format(self.passwd)}
        #print(type(creds))
        #print(creds)
        #print(creds)
        params = json.dumps(creds).encode('utf-8')
        #print(params)
        #print(type(params))
        #encoded_data = json.dumps(data).encode('utf-8')
        authUrl = f"{bcf.baseURL()}/api/v1/auth/login"
        #bcf.podname()
        print(authUrl)
        #return authUrl
        headers={'Content-Type': 'application/json'}

        try:
            post_req = urllib.request.Request(authUrl, headers=headers, data=params)
            resp = urllib.request.urlopen(post_req)
            #cookie = response['session_cookie']
            #print(cookie)
            #print(resp)
            #print("Now do json loads and print cookie")
            #print("Podname is ", self.pod)
            json_content = json.loads(resp.read().decode('utf8'))
            cookie = json_content['session_cookie']
            print(cookie)
            return cookie
        except urllib.error.HTTPError as e:
            print(e.code)


 

bcf = bcf_session(URL, USER, PASSWORD, TOKEN, POD)
# TEST OK:
#print(bcf.podname())
bcf.authentication()
