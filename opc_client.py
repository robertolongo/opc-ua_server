from opcua import Client
import time

url = "opc.tcp://127.0.0.1:4840"
node_id = "ns=2;i=2"    # "ns=2;i=3"

client = Client(url)

client.connect()
print("Client connected")


node = client.get_node(node_id)
node_value = node.get_value()
node_desc = node.get_description().Text
print("id:", node_id, " desc:", node_desc, " value:", node_value)

client.disconnect()
print("Client disconnected")

