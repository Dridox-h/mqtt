import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import datetime
import os

# Configuration du broker
BROKER = os.getenv("MQTT_BROKER", "127.0.0.1")
PORT = 1883
TOPIC = "camera/events"

# Callback lors de la connexion
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Publisher connecté au broker MQTT !")
    else:
        print(f"Échec de la connexion, code : {reason_code}")

# Initialisation du client MQTT (Publisher)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "CameraPublisher")
client.on_connect = on_connect

# Connexion au broker
try:
    client.connect(BROKER, PORT, 60)
except Exception as e:
    print(f"Erreur de connexion : {e}")
    exit(1)

# Lancement de la boucle réseau en arrière-plan
client.loop_start()

# Variables pour simuler des événements
events = ["motion_detected", "person_recognized", "vehicle_detected", "connection_lost", "tamper_detected"]
cameras = ["cam_front", "cam_back", "cam_garage", "cam_garden"]

print("Début de la publication des événements caméras...\n")

try:
    while True:
        # Création d'un faux événement
        payload = {
            "camera_id": random.choice(cameras),
            "event_type": random.choice(events),
            "timestamp": datetime.now().isoformat(),
            "confidence": round(random.uniform(0.60, 0.99), 2)
        }
        
        # Conversion du dictionnaire en chaîne JSON
        message = json.dumps(payload)
        
        # Publication du message
        client.publish(TOPIC, message)
        print(f"Publié : {message}")
        
        # Attente de 5 secondes
        time.sleep(5)
except KeyboardInterrupt:
    print("\nArrêt du publisher à la demande de l'utilisateur...")
finally:
    client.loop_stop()
    client.disconnect()
