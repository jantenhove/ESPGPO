# ESPGPO
Script for setting GPO on ESP2866 which is running the firmware from 'ESP2866 Universal IO Bridge': https://github.com/eriksl/esp8266-universal-io-bridge.
After uploading the firmware setup the GPO using tbe provided instructions, you can use this script to switch them. 
## Script parameters
* --server: IP address or hostname of the ESP2866
* --gpo: The GPO port to set
* --value: The value to set the gpo to
* --port: (not required)The port on the ESP2866 to connect to. Default: 24
* --timeout: (not required)The timeout to use for setting the GPO (Default: 5 seconds)

