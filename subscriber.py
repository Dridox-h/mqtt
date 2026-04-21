import paho.mqtt.client as mqtt
import json
import os

# Configuration du broker
BROKER = os.getenv("MQTT_BROKER", "127.0.0.1")
PORT = 1883
TOPIC = "camera/events"

# Callback lors de la connexion
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Subscriber connecté avec succès au broker MQTT !\n")
        # On s'abonne au topic dès qu'on est connecté
        client.subscribe(TOPIC)
        print(f"En attente des messages sur le topic '{TOPIC}'...\n")
        print("-" * 50)
    else:
        print(f"Échec de la connexion, code de retour : {reason_code}")

# Callback lors de la réception d'un message
def on_message(client, userdata, msg):
    try:
        # Décodage du message JSON
        payload = json.loads(msg.payload.decode("utf-8"))
        
        # Affichage structuré du message
        print(f"🚨 [NOUVEL ÉVÉNEMENT] reçu le {payload.get('timestamp')}")
        print(f" ├─ Caméra    : {payload.get('camera_id')}")
        print(f" ├─ Événement : {payload.get('event_type')}")
        print(f" └─ Confiance : {payload.get('confidence') * 100:.1f} %\n")
        print("-" * 50)
        
    except json.JSONDecodeError:
        # Au cas où le message ne serait pas du JSON valide
        print(f"[REÇU] Topic: {msg.topic} | Message (brut): {msg.payload.decode('utf-8')}")

# Initialisation du client MQTT (Subscriber)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "CameraSubscriber")
client.on_connect = on_connect
client.on_message = on_message

# Connexion au broker
try:
    client.connect(BROKER, PORT, 60)
except Exception as e:
    print(f"Erreur de connexion : {e}")
    exit(1)

# Lancement de la boucle réseau bloquante
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nArrêt du subscriber à la demande de l'utilisateur...")
    client.disconnect()
