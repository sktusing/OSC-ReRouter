from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

# remap osc args to message
def remap(message, *args):
    new_message = prefix + str(message) + '/' + str(args)
    client.send_message(new_message, '0')
    print('Sent: ', new_message)

# get osc config
rxip = input("Enter the RX IP Address: ")
rxport = input("Enter the RX Port: ")
txip = input("Enter the TX IP Address: ")
txport = input("Enter the TX Port: ")
rxlisten = input("Enter the message to listen for (* is wildcard, ex: /eos/out/get*): ")
prefix = input("Enter the new message prefix (ex: /reRouter): ")

# OSC Setup
dispatcher = Dispatcher()
dispatcher.map(rxlisten, remap)

# create client
client = SimpleUDPClient(txip, int(txport))

# create server
server = BlockingOSCUDPServer((rxip, int(rxport)), dispatcher)
server.serve_forever()