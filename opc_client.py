from opcua import Client, ua
import time


def read_node(server_url, node_id):
    client = Client(server_url)
    client.connect()
    print("Client connected")


    node = client.get_node(node_id)
    node_value = node.get_value()
    node_desc = node.get_description().Text
    print("id:", node_id, " desc:", node_desc, " display name:", node.get_display_name().to_string(), " value:", node_value)
    node.get_display_name()

    client.disconnect()
    print("Client disconnected")
    return node_value

def write_node(server_url, node_id, node_value):
    client = Client(server_url)
    client.connect()
    print("Client connected")

    node = client.get_node(node_id)
    node.set_value(node_value)

    client.disconnect()
    print("Client disconnected")


def list_nodes(server_url):
    client = Client(server_url)
    client.connect()
    print("Client connected")

    root = client.get_root_node()
    objects_node = client.get_objects_node()

    display_name_objects = objects_node.get_display_name().to_string()
    print(f"**{display_name_objects}** ({objects_node.nodeid.to_string()})")


    node_list = objects_node.get_children()
    for node in node_list:
        try:
            node_id_str = node.nodeid.to_string()
            # print(f"ID del Nodo: **{node_id_str}**")

            display_name = node.get_display_name().to_string()
            print(f" {display_name} ({node_id_str})")


        except Exception as e:
            print(f"Errore durante la ricerca del nodo per nome: {e}")


    client.disconnect()
    print("Client disconnected")


if __name__ == "__main__":

    url = "opc.tcp://127.0.0.1:4840"
    node_id = "ns=2;i=2"  # "ns=2;i=3"

    # Read single node
    valore = read_node(url, node_id)
    print("valore prima:",valore)

    print("------------------------------")

    write_node(url, node_id,123.45)

    print("------------------------------")

    valore = read_node(url, node_id)
    print("valore dopo:",valore)


    list_nodes(url)



