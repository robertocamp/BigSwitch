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
        headers = {'Cookie': 'session_cookie={}'.format(apiToken)}
        #print(headers)
        url = baseURL + apiPath
        print("connecting to ",  url)
        req = urllib.request.Request(url=url, headers=headers)
        resp  = urllib.request.urlopen(req, None)
        resp_data = resp.read().decode()
        raw_json = json.loads(resp_data)
        return raw_json

    def apiCallPut(self, apiPath, payload):
        try:
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
            resp = urllib.request.urlopen(req, None)
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
            resp = urllib.request.urlopen(req, None)
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

    def getFabricSummary(self):
        apiPath = "/api/v1/data/controller/applications/bcf/info/summary/fabric?single=true"
        getFabricSummary = self.apiCallGet(apiPath)
        print(getFabricSummary)

    def getTenants(self):
        apiPath = "/api/v1/data/controller/applications/bcf/tenant"
        getTenants = self.apiCallGet(apiPath)
        print(getTenants)

    def deployTenant(self, tenant):
        self.tenant = tenant
        apiPath = "/api/v1/data/controller/applications/bcf/tenant"
        payload = {'name': f'{tenant}'}
        deployTenant =  self.apiCallPost(apiPath, payload)
        

    def deployInterfaceGroup(self, name, mode):
        self.name = name
        self.mode = mode
        apiPath = "/api/v1/data/controller/applications/bcf/interface-group"
        payload = {
          "name": f'{name}',
          "mode": f'{mode}',
          "backup-mode": "static",
          "shutdown": False,
          "preempt": False
        }
        deployInterfaceGroup =  self.apiCallPost(apiPath, payload)

    def deployXkubInterfaceGroup(self,name,mode,host,nic1,nic2):
        self.name = name
        self.mode = mode
        self.host = host
        self.nic1 = nic1
        self.nic2 = nic2

        apiPath = "/api/v1/data/controller/applications/bcf/interface-group"
        payload=[ {
          "backup-mode" : "static",
          "host-interface" : [ {
            "host-name" : f'{host}',
            "interface-name" : f'{nic1}',
          }, {
            "host-name" : f'{host}',
            "interface-name" : f'{nic2}'
          } ],
          "mode" : f'{mode}',
          "name" : f'{name}',
          "preempt" : False,
          "shutdown" : False
        } ]

        deployXkubInterfaceGroup = self.apiCallPost(apiPath, payload)







    def deploySystemRoutes(self, tenant):
        self.tenant = tenant
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='{tenant}']/logical-router/tenant-interface[remote-tenant='system']"
        payload = {
              "shutdown": False,
              "import-route": True,
              "remote-tenant": "system"
              }
        deploySystemRoutes =  self.apiCallPut(apiPath, payload)


    def deployTenantSystemInterface(self,tenant):
        self.tenant = tenant
        apiPath = f"/api/v1/data/controller/applications/bcf/tenant[name='system']/logical-router/tenant-interface[remote-tenant='{tenant}']"
        payload = {
              "remote-tenant": f'{tenant}',
              "shutdown": False,
              "export-route": True
            }
        deployTenantSystemInterface = self.apiCallPut(apiPath, payload)

    def deployDefaultRoute(self,tenant):
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


    def deploySegment(self, tenant, name, description ):
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

    def deploySegmentInterfaceRule(self,tenant,segment,vlan,description):
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
        deploySegmentInterfaceRule = self.apiCallPut(apiPath, payload)


    def deploySwitchMembershipRule(self,tenant,segment,vlan,description):
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
        deploySwitchMembershipRule = self.apiCallPut(apiPath, payload)


    def deploySegmentInterface(self,tenant,segment, cidr, dhcpa, dhcpb):
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

    def deployLeaf(self, switchname, role, leafgroup, mac):
        self.switchname = switchname
        self.role = role
        self.leafgroup = leafgroup
        self.mac = mac

        apiPath = f"/api/v1/data/controller/core/switch-config[name='{switchname}']"

        payload = {
          "name": f'{switchname}',
          "fabric-role": f'{role}',
          "leaf-group": f'{leafgroup}',
          "mac-address": f'{mac}',
          "time": {
            "override-enabled": False
          },
          "snmp": {
            "override-enabled": False,
            "trap-enabled": False
          },
          "snmp-trap": {
            "override-enabled": False
          },
          "logging": {
            "override-enabled": False,
            "controller-enabled": True,
            "remote-enabled": True
          },
          "tacacs": {
            "override-enabled": False
          }
        }

        deployLeaf = self.apiCallPut(apiPath,payload)

    def deploySpine(self, switchname, role, mac):
        self.switchname = switchname
        self.role = role
        self.mac = mac

        apiPath = f"/api/v1/data/controller/core/switch-config[name='{switchname}']"

        payload = {
         "name": f'{switchname}',
         "fabric-role": f'{role}',
         "mac-address": f'{mac}',
          "time": {
            "override-enabled": False
          },
          "snmp": {
            "override-enabled": False,
            "trap-enabled": False
          },
          "snmp-trap": {
            "override-enabled": False
          },
          "logging": {
            "override-enabled": False,
            "controller-enabled": True,
            "remote-enabled": True
          },
          "tacacs": {
            "override-enabled": False
          }
        }

        deploySpine = self.apiCallPut(apiPath,payload)





bcf_ops = BCF_operations(podname)

# TEST OK:
#bcf_ops.deployTenant("caas")
#bcf_ops.deploySegment( "caas", "xkub_nodes", "xkub:10.219.84.96/27")
#bcf_ops.deployInterfaceGroup("xkubtestapi", "lacp")
#bcf_ops.deployXkubInterfaceGroup("xkubtestapi", "lacp","xkubtestapi.opr.test.statefarm.org","enp4s0f0","enp5s0f0")
#bcf_ops.fabricSummary()
#bcf_ops.getTenants()
#bcf_ops.segmentInterface()
#bcf_ops.getSegments(tenant)


#bcf_ops.defaultRoute("global")
#bcf_ops.segmentInterfaceRule("vmware","esxi","11","esxi_host")
#bcf_ops.newSegment("global","test","esxi" )
#bcf_ops.switchMembershipRule("global","test","11","esxi")
#bcf_ops.importSystemRoutes("global")
#bcf_ops.tenantSystemInterface("global")
