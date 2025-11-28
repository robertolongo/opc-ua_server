from logging import exception

from opcua import Server
import random
import datetime
import time
import configparser


def run_server(url, namespace, interval, real_var_list):
    # Server initialization
    server = Server()
    server.set_endpoint(url)
    name_space = server.register_namespace(namespace)

    # Adding nodes
    node = server.get_objects_node()

    parameters_object = node.add_object(name_space, "Parameters")

    #parameters_object2 = parameters_object.add_object(name_space, "Parameters")

    temperature_var = parameters_object.add_variable(name_space, "Temperature", 0)
    pressure_var = parameters_object.add_variable(name_space, "Pressure", 0)
    humidity_var = parameters_object.add_variable(name_space, "Humidity", 0)
    timestamp_var = parameters_object.add_variable(name_space, "Timestamp", 0)

    print(temperature_var.nodeid.to_string())
    print(temperature_var.get_display_name().to_string())



    temperature_var.set_writable()
    pressure_var.set_writable()
    humidity_var.set_writable()
    timestamp_var.set_writable()

    variables = []
    for real_var in real_var_list:
        variable_var = parameters_object.add_variable(name_space, real_var, 0)
        variable_var.set_writable()
        variables.append(variable_var)


    # Start server
    server.start()
    print("OPC-UA SERVER started at: {}".format(url))
    print("---------------------------------------")
    print("Temperature   Pressure   Humidity   Timestamp")

    while True:
        temperature = random.uniform(10, 50)
        pressure = random.randint(300, 1000)
        humidity = random.randint(40, 70)
        timestamp = datetime.datetime.now()

        print(round(temperature,4), pressure, humidity, timestamp)
        print("Temperature: ", round(temperature,4))
        print("Pressure: ", pressure)
        print("Humidity: ", humidity)
        print("Timestamp: ", timestamp)

        temperature_var.set_value(temperature)
        pressure_var.set_value(pressure)
        humidity_var.set_value(humidity)
        timestamp_var.set_value(timestamp)

        for real_var in variables:
            print(real_var.nodeid.to_string()," (",real_var.get_display_name().to_string(),"): ", real_var.get_value())

        time.sleep(interval)


if __name__ == "__main__":

    #url = "opc.tcp://127.0.0.1:4840"
    #namespace = "OPC-UA_SERVER"
    #interval = 10

    url = ''
    namespace = ''
    interval = 0

    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        url = config.get('server', 'url')
        namespace = config.get('server', 'namespace')
        interval = int(config.get('settings', 'interval'))
        real_var = config.get('real_var', 'variables').split()

        configuration_loaded = True
    except Exception as e:
        configuration_loaded = False
        print(f"Error reading config file: {e}")

    if configuration_loaded:
        run_server(url, namespace, interval, real_var)
