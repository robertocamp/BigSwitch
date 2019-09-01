import json
import urllib.parse
import urllib.request
import ssl
import sys
import csv
from bcf_session import bcf

podname = bcf.podname()
baseURL = bcf.baseURL()
apiToken = bcf.authentication()



class BCF_operations:
    def __init__(self, podname):
        self.podname = podname
        print("Current active POD:")
        print(podname)



    def apiCallGet(self, apiPath):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        headers = {'Cookie': 'session_cookie={}'.format(apiToken)}
        #print(headers)
        url = baseURL + apiPath
        print("connecting to ",  url)
        req = urllib.request.Request(url=url, headers=headers)
        resp  = urllib.request.urlopen(req, None, context=ctx)
        resp_data = resp.read().decode()
        raw_json = json.loads(resp_data)
        return raw_json

    def apiCallPut(self, apiPath, payload):
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            headers = {'Cookie': 'session_cookie={}'.format(apiToken)}
            #print(headers)
            url = baseURL + apiPath
            print("Connecting to ", url)
            #DATA = urllib.parse.urlencode(payload).encode('utf8')
            DATA = json.dumps(payload).encode('utf8')
            req = urllib.request.Request(url=url, method='PUT', data=DATA, headers=headers)
            req.add_header("Content-Type", "application/json")
            print(DATA)
            #print(type(DATA))
            resp = urllib.request.urlopen(req, None, context=ctx)
            #return resp
            #print(resp)
            ret_code = resp.status
            print(ret_code)
            return resp
            print(resp)
        except urllib.error.HTTPError as e:
            print(e.code, ":  Error updating controller " , podname)
            #sys.exit()

    def apiCallPost(self, apiPath, payload):
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            headers = {'Cookie': 'session_cookie={}'.format(apiToken)}
            #print(headers)
            url = baseURL + apiPath
            print("Connecting to ", url)
            #DATA = urllib.parse.urlencode(payload).encode('utf8')
            DATA = json.dumps(payload).encode('utf8')
            req = urllib.request.Request(url=url, data=DATA, headers=headers)
            req.add_header("Content-Type", "application/json")
            #print(DATA)
            #print(type(DATA))
            resp = urllib.request.urlopen(req, None, context=ctx)
            ret_code = resp.status
            print(ret_code)
            return resp
            print(resp)
        except urllib.error.HTTPError as e:
            print(e.code, ":  Error updating controller " , podname)


    def getSegments(self, tenant):
        self.tenant = tenant
        # tenant = "VMWARE"
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/segment"
        getSegmentsJson = self.apiCallGet(apiPath)
        print(getSegmentsJson)

    def fabricSummary(self):
        apiPath = "/api/v1/data/controller/applications/bcf/info/summary/fabric?single=true"
        fabricSummaryJson = self.apiCallGet(apiPath)
        print(fabricSummaryJson)

    def getTenants(self):
        apiPath = "/api/v1/data/controller/applications/bcf/tenant"
        getTenantsJson = self.apiCallGet(apiPath)
        print(getTenantsJson)

    def newTenant(self, tenant):
        self.tenant = tenant
        apiPath = "/api/v1/data/controller/applications/bcf/tenant"
        payload = {'name': f'{tenant}'}
        deployTenant =  self.apiCallPost(apiPath, payload)
        #return deployTenant

    def importSystemRoutes(self, tenant):
        self.tenant = tenant
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/logical-router/tenant-interface[remote-tenant='system']"
        payload = {
              "shutdown": False,
              "import-route": True,
              "remote-tenant": "system"
              }
        deployTenantSystemInterface =  self.apiCallPut(apiPath, payload)


    def tenantSystemInterface(self,tenant):
        self.tenant = tenant
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='system']/logical-router/tenant-interface[remote-tenant='{tenant}']"
        payload = {
              "remote-tenant": f'{tenant}',
              "shutdown": False,
              "export-route": True
            }
        deployTenantSystemInterface = self.apiCallPut(apiPath, payload)

    def defaultRoute(self,tenant):
        self.tenant = tenant
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/logical-router/static-route[dst-ip-subnet='0.0.0.0/0'][preference=1]"
        payload = {
                  "preference": 1,
                  "dst-ip-subnet": "0.0.0.0/0",
                  "next-hop": {
                    "tenant": "system"
                      }
                }
        deployDefaultRoute =  self.apiCallPut(apiPath, payload)


    def newSegment(self, tenant, name, description ):
        self.tenant = tenant
        self.name = name
        self.description = description
        payload = {
                'name': f'{name}',
                'description': f'{description}'
                    }
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/segment"
        deploySegment =  self.apiCallPost(apiPath, payload)
        #print(apiPath)
        #print(payload)

    def segmentInterfaceRule(self,tenant,segment,vlan,description):
        self.tenant = tenant
        self.segment = segment
        self.vlanid = vlan
        self.description = description
        payload = {
          "vlan": f"{vlan}",
          "interface-group": "any",
          "description": f"{description}"
          }

        #apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='']/segment[name='']/interface-group-membership-rule[interface-group="any"]"
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/segment[name='{segment}']/interface-group-membership-rule[interface-group='any'][vlan={vlan}]"
        deployInterfaceRule = self.apiCallPut(apiPath, payload)


    def switchMembershipRule(self,tenant,segment,vlan,description):
        self.tenant = tenant
        self.segment = segment
        self.vlan = vlan
        self.description = description
        payload = {
          "vlan": f"{vlan}",
          "switch": "any",
          "interface": "any",
          "description": f"{description}"
          }

        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/segment[name='{segment}']/switch-port-membership-rule[switch='any'][interface='any'][vlan={vlan}]"
        deployInterfaceRule = self.apiCallPut(apiPath, payload)


    def segmentInterface(self,tenant,segment, cidr, dhcpa, dhcpb):
        self.tenant = tenant
        self.segment = segment
        self.cidr = cidr
        self.dhcpa = dhcpa
        self.dhcpb = dhcpb

        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/logical-router/segment-interface[segment='{segment}']"
        payload = {
                  "segment": f'{segment}',
                  "shutdown": False,
                  "private": False,
                  "ip-subnet": [
                    {
                      "ip-cidr": f'{cidr}',
                      "directed-broadcast": False,
                      "withdraw": False,
                      "no-autoconfig": False
                    }
                  ],
                  "dhcp-relay": [
                    {
                      "server-ip": f'{dhcpa}'
                    },
                    {
                      "server-ip": f'{dhcpb}'
                    }
                  ],
                  "ipv6-nd-managed": False,
                  "ipv6-suppress-ra": False
                }
        deploySegmentInterface =  self.apiCallPut(apiPath, payload)


bcf_ops = BCF_operations(podname)

# TEST OK:
#bcf_ops.fabricSummary()
#bcf_ops.getTenants()
#bcf_ops.segmentInterface()
#bcf_ops.getSegments(tenant)
#bcf_ops.newSegment( "vmware", "vsan_vlan_12", "vsan:10.219.84.96/27")
#bcf_ops.newTenant("global")
#bcf_ops.defaultRoute("global")
#bcf_ops.segmentInterfaceRule("vmware","esxi","11","esxi_host")
# bcf_ops.newSegment("global","test","esxi" )
#bcf_ops.switchMembershipRule("global","test","11","esxi")
#bcf_ops.importSystemRoutes("global")
#bcf_ops.tenantSystemInterface("global")
