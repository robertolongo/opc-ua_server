from opcua import Server
import random
import datetime
import time

url = "opc.tcp://127.0.0.1:4840"
name = "OPC-UA_SERVER"

if __name__ == "__main__":
    # Server initialization
    server = Server()
    server.set_endpoint(url)
    name_space = server.register_namespace(name)

    # Adding nodes
    node = server.get_objects_node()

    Parameters_object = node.add_object(name_space, "Parameters")

    Temperature_var = Parameters_object.add_variable(name_space, "Temperature", 0)
    Pressure_var = Parameters_object.add_variable(name_space, "Pressure", 0)
    Humidity_var = Parameters_object.add_variable(name_space, "Humidity", 0)
    Timestamp_var = Parameters_object.add_variable(name_space, "Timestamp", 0)

    Temperature_var.set_writable()
    Pressure_var.set_writable()
    Humidity_var.set_writable()
    Timestamp_var.set_writable()

    # Start server
    server.start()
    print("OPC-UA SERVER started at: {}".format(url))
    print("---------------------------------------")
    print("Temperature   Pressure   Humidity   Timestamp")

    while True:
        Temperature = random.uniform(10, 50)
        Pressure = random.randint(300, 1000)
        Humidity = random.randint(40, 70)
        Timestamp = datetime.datetime.now()

        print(round(Temperature,4), Pressure, Humidity, Timestamp)

        Temperature_var.set_value(Temperature)
        Pressure_var.set_value(Pressure)
        Humidity_var.set_value(Humidity)
        Timestamp_var.set_value(Timestamp)

        time.sleep(30)