import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import errorcode

import json

import requests

# define database connection parameters
config = {
  'user': 'samy',
  'password': '3141',
  'host': 'localhost',
  'database': 'esp32_api',
  'raise_on_warnings': True
}

# connect to database
#try:
#  cnx = mysql.connector.connect(**config)
#  cursor = cnx.cursor()
#except mysql.connector.Error as err:
#  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#    print("Something is wrong with your user name or password")
#  elif err.errno == errorcode.ER_BAD_DB_ERROR:
#    print("Database does not exist")
#  else:
#    print(err)

# define callback function for message
def on_message(client, userdata, message):
  payload = message.payload.decode('utf-8')
  print(payload)

  try:
    data = json.loads(payload)
    temperatura = data['temperatura']
    humedad = data['humedad']
    voltajeradiacion = data['voltajeradiacion']
    valorradiacion = data['valorradiacion']
    agua = data['agua']
    url = 'http://localhost:8000/api/esp32'
    esp={'temperatura': temperatura, 'humedad': humedad, 'voltajeradiacion': voltajeradiacion, 'valorradiacion': valorradiacion, 'agua': agua}

    x = requests.post(url, json=esp)
    #print("Esp en json:" + esp)
    print(x.text)
  except json.JSONDecodeError as e:
    print("error")
  # insert data into database
  #add_data = "INSERT INTO table_name (data) VALUES (%s);"
  #cursor.execute(add_data, (payload,))
  #cnx.commit()

# connect to MQTT broker and subscribe to topic
client = mqtt.Client()
client.on_message = on_message
client.connect("192.168.137.1", 1883, 60)
client.subscribe("/temperatura")
client.loop_forever()

# close database connection
#cursor.close()
#cnx.close()
