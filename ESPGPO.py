#!/usr/bin/env python

import telnetlib
import socket
import argparse

parser = argparse.ArgumentParser(prog='ESPGPO', description='Set GPO on ESP2866 with ESP2866 universal io bridge.')
parser.add_argument("-s", "--server", dest='host', required=True, type=str)
parser.add_argument("-g", "--gpo", dest='gpio', required=True, type=int)
parser.add_argument("-v", "--value", dest='gpioVal', required=True, type=int)
parser.add_argument("-p", "--port", dest='port', required=False, default=24, type=int)
parser.add_argument("-t", "--timeout", dest='timeout', required=False, default=5, type=int)

args = parser.parse_args()

print("Connecting to " + args.host + ":" + str(args.port) + "...")
try:
    tn = telnetlib.Telnet(args.host, args.port, args.timeout)
except socket.timeout:
    dataReceived = ""
else:
    print("Connected!")
    dataToSend = "gs " + str(args.gpio) + " " + str(1 if args.gpioVal > 0 else 0) + "\n"
    # print("Sending: " + dataToSend)
    tn.write(dataToSend.encode('ascii'))
    dataReceived = str(tn.read_until("\n".encode('ascii'), args.timeout))
    tn.close()

# check the return type for success. display the message and return success

if len(dataReceived) <= 0:
    print("Timed out. Please check the hostname/port")
    exit(1)
else:
    # correct response is: gpio: X, name: gpioX, mode: output, state: on, startup: off\n'
    # all others means not correct (and we can display it)
    state = "on" if args.gpioVal > 0 else "off"
    if "gpio: " + str(args.gpio) in dataReceived and "state: " + state in dataReceived:
        print("GPO: " + str(args.gpio) + " successfully set to " + state)
        exit(0)
    else:
        print("Error while setting GPO " + str(args.gpio) + "\nResponse from ESP2866: " + dataReceived)
