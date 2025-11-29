from opcua import Client

# from opcua.common import node

# Depth limit for recursive browsing (to prevent overload)
MAX_DEPTH = 3

def browse_and_print_nodes(node, depth=0):
    """
    Recursive function to browse and print child nodes.
    """
    if depth > MAX_DEPTH:
        print(f"{'  ' * depth} ... Maximum depth reached.")
        return

    try:
        # Get all child nodes
        children = node.get_children()

        # If no children, exit recursion
        if not children:
            return

        for child in children:
            indent = ''
            # Print basic node information
            try:
                display_name = child.get_display_name().to_string()
                node_id = child.nodeid.to_string()
                try:
                    value = child.get_value()
                except Exception as e:
                    value = None

                # Format output to show depth
                indent = '  ' * depth
                print(f"{indent}├── {display_name} ({node_id}) : {value}")

                # Recursively call the function for child nodes
                browse_and_print_nodes(child, depth + 1)

            except Exception as e:
                # Handle the case where a node is unreadable (e.g., permissions)
                print(f"{indent}└── Error reading child node: {e}")

    except Exception as e:
        print(f"{'  ' * depth}ERROR browsing node: {e}")


def connect_and_browse(url_server):
    client = None
    try:
        print(f"Attempting to connect to **{url_server}**...")
        client = Client(url_server)
        client.connect()
        print("Connection established. Starting tree browsing.")

        # 1. Get the "Objects" node (i=85)
        # This is the standard starting point for all user-defined variables.
        objects_node = client.get_objects_node()

        print("\n--- Starting Node Tree Print (Max Depth: 3) ---")
        display_name_objects = objects_node.get_display_name().to_string()
        print(f"**{display_name_objects}** ({objects_node.nodeid.to_string()})")

        # 2. Start recursive browsing
        browse_and_print_nodes(objects_node, depth=1)

        print("--- Browsing Finished ---")

    except ConnectionRefusedError:
        print(f"❌ ERROR: Connection refused. Ensure the OPC UA server is running at {url_server}.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        # 3. Disconnection
        if client:
            client.disconnect()
            print("\nDisconnected from the server.")


def read_node(server_url, node_id):
    print("read_node")
    client = None
    node_value = None

    try:
        client = Client(server_url)
        client.connect()
        #print("Client connected")


        node = client.get_node(node_id)
        node_value = node.get_value()
        node_desc = node.get_description().Text
        print("id:", node_id, " desc:", node_desc, " display name:", node.get_display_name().to_string(), " value:", node_value)
        node.get_display_name()

    except ConnectionRefusedError:
        print(f"❌ ERROR: Connection refused. Ensure the OPC UA server is running at {server_url}.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        # 3. Disconnection
        if client:
            client.disconnect()
            #print("\nDisconnected from the server.")

    return node_value

def write_node(server_url, node_id, node_value):
    print("write_node")
    client = None

    try:
        client = Client(server_url)
        client.connect()
        #print("Client connected")

        node = client.get_node(node_id)
        node.set_value(node_value)

    except ConnectionRefusedError:
        print(f"❌ ERROR: Connection refused. Ensure the OPC UA server is running at {server_url}.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
    # 3. Disconnection
        if client:
            client.disconnect()
            #print("\nDisconnected from the server.")




def list_nodes(server_url):
    print("list_nodes")
    client = None
    try:
        client = Client(server_url)
        client.connect()
        #print("Client connected")

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
                print(f"Node not found: {e}")


    except ConnectionRefusedError:
        print(f"❌ ERROR: Connection refused. Ensure the OPC UA server is running at {server_url}.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
    # 3. Disconnection
        if client:
            client.disconnect()
            print("\nDisconnected from the server.")


if __name__ == "__main__":

    url = "opc.tcp://127.0.0.1:4840"
    node_id = "ns=2;i=2"  # "ns=2;i=3"

    # Read single node
    node_value = read_node(url, node_id)
    print("old node_value:", node_value)

    print("------------------------------")

    write_node(url, node_id,123.45)

    print("------------------------------")

    node_value = read_node(url, node_id)
    print("new node_value:", node_value)


    list_nodes(url)
    #connect_and_browse(url)



