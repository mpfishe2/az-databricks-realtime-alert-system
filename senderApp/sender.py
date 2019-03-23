import uuid
import time
import random
import json
import time
from azure.servicebus import ServiceBusService

NAMESPACE_NAME = "<event-hub-namespace-name>"
KEY_NAME = "RootManageShareAccessKey"
KEY_VALUE = "<primary-key-value>"

if NAMESPACE_NAME == "<event-hub-namespace-name>" or NAMESPACE_NAME == "":
    NAMESPACE_NAME = input("What is the name of your Event Hub Namespace?:")

if KEY_VALUE == "<event-hub-namespace-name>" or KEY_VALUE == "":
    KEY_VALUE = input("What is the primary key of your Event Hub Namespace:")


# service_namespace = Azure Event Hub Namespace name
# shared_access_key_value = Access Key, found in Azure Portal for Azure Event Hub Namespace
sbs = ServiceBusService(service_namespace=NAMESPACE_NAME, shared_access_key_name=KEY_NAME, shared_access_key_value=KEY_VALUE)
# -------------------------------------------------------
# This is the global variables to create some sample data
# --------------------------------------------------------
storeids = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
products = [
    [1, "Chef's Knife", "Kitchen", 15.99],
    [2, "Spatula", "Kitchen", 2.99],
    [3, "Wooden Spoon", "Kitchen", 1.99],
    [4, "Knife Block", "Kitchen", 10.99],
    [5, "Roasting Pan", "Kitchen", 17.99],
    [6, "Saucepan", "Kitchen", 21.99],
    [7, "Blender", "Kitchen", 25.99],
    [8, "Toaster", "Kitchen", 30.99],
    [9, "Rice Cooker", "Kitchen", 29.99],
    [10, "Cutting Board", "Kitchen", 12.99],
    [11, "Grill", "Outdoors", 159.99],
    [12, "Dog Bed", "Pets", 30.00],
    [13, "Litter Box", "Pets", 30.00],
    [14, "Cough Syrup", "Medicine", 15.00]
]
# --------------------------------------------------------
# --------------------------------------------------------
keepRunning = True
# This will run for about 2.5 hours which should be fine for labs and demos
for y in range(0,2000):
    # Get a product from the products variable
    product = products[random.randint(0,10)]
    # define a reading as a python dictionary object
    reading = {'storeId': storeids[random.randint(0, 10)], 
                'timestamp': time.time(),
                'producttype': product[0],
                'name': product[1],
                'category': product[2],
                'price': product[3],
                'quantity': random.randint(1,3)
    }

    # Add some intrigue...
    if product[1] == "Cough Syrup":
        reading['quantity'] += 10
    

    # use json.dumps to convert the dictionary to a JSON format
    s = json.dumps(reading)
    # send to Azure Event Hub
    sbs.send_event("ingestion", s)
    print(s)
    # wait 5 seconds
    time.sleep(5)