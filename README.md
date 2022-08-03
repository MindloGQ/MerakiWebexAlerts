# MerakiWebexAlerts
This script leverages the Meraki and Webex Rest API to retrieves the status of the uplinks on the Meraki platform and sends an alert messages to a Webex room in the event that one or both of the links are down


## Environment
The script requires a python3 evironement with the following modules and versions

meraki==1.18.2

requests==2.22.0

requests-oauthlib==1.3.0

## Credentials
The following credentials to work:

Meraki Organization Key

Meraki Organization ID

Meraki Network ID

Webex Room ID

Webex Bearer token

for security reasons credentials should be stored in a separate file or as environment variables and imported into the script instead of being embedded in the script itself.

## Execution
The script can be run in multiple ways:

1. From terminal by typing: python3 /path/to/merakiWebexAlerts.py

2. From any IDE that supports python3

3. As a cronjob
