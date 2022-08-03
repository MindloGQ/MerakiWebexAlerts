#!/usr/bin/env python3

import meraki
from creds import orgKey, orgId, netId, roomId, webexBearer
import requests
from requests_toolbelt import MultipartEncoder


#instantiate the dashboardAPI by providing the Meraki Organization Key
dashboard = meraki.DashboardAPI(orgKey)

#retrive the status of the uplinks from the dashboard API by providing the Organization ID
response = dashboard.appliance.getOrganizationApplianceUplinkStatuses(orgId, total_pages='all')

#iterate through the uplinks and send an alert message to the Webex room if any of the uplinks are not in an "active" state
for entry in response:
    if entry["networkId"] == netId:
        for uplink in entry["uplinks"]:
            if uplink["status"] != "active":
                upLinkDown = uplink["interface"]
                upLinkStatus = uplink["status"]
                
                m = MultipartEncoder({'roomId': roomId, 'text': ("Please note that interface " + upLinkDown + " is in " + upLinkStatus + " status")})

                r = requests.post('https://webexapis.com/v1/messages', data=m, headers={'Authorization': 'Bearer ' + webexBearer, 'Content-Type': m.content_type})