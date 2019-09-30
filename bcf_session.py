import json
import urllib.parse
import urllib.request
import ssl
import sys
from  BCFLAB1 import URL, USER, AUTH, POD





class bcf_session():
    # def __init__(self, url, user, auth, token, pod):
    def __init__(self, url, user, auth,  pod):
        self.base_url = url
        self.user = user
        self.auth = auth
        # self.token = token
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
        ssl._create_default_https_context = ssl._create_unverified_context
        # Python3 / urllib3 does not have a 'context' parameter
        # cookie = self.token
        creds = {'user':'{}'.format(self.user), 'password':'{}'.format(self.auth)}
        params = json.dumps(creds).encode('utf-8')
        authUrl = f"{bcf.baseURL()}/api/v1/auth/login"
        print(authUrl)
        headers={'Content-Type': 'application/json'}

        try:
            post_req = urllib.request.Request(authUrl, headers=headers, data=params)
            resp = urllib.request.urlopen(post_req)
            json_content = json.loads(resp.read().decode('utf8'))
            cookie = json_content['session_cookie']
            print(cookie)
            return cookie
        except urllib.error.HTTPError as e:
            print(e.code)


        # for the POST ,  does the data have to be json-encoded ?



# bcf = bcf_session(URL, USER, PASSWORD, TOKEN, POD)
bcf = bcf_session(URL, USER, AUTH, POD)
# TEST OK:
#print(bcf.podname())
bcf.authentication()
