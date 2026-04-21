# 📡 MQTT Camera Event Pipeline

Une solution légère et robuste pour simuler et monitorer un flux d'événements caméras via le protocole MQTT, entièrement containerisée avec **Docker**.

## 🚀 Architecture

Le projet est composé de trois services principaux :
*   **Mosquitto Broker** : Le serveur central qui gère les messages MQTT.
*   **Camera Publisher** : Un script Python qui génère des événements de caméras aléatoires (mouvement, reconnaissance de personne, perte de connexion, etc.) toutes les 5 secondes.
*   **Event Subscriber** : Un script Python qui s'abonne au topic et affiche les événements de manière structurée et colorée dans les logs.

## 🛠️ Technologies
*   **Langage** : Python 3.9
*   **MQTT Client** : Paho-MQTT (API v2)
*   **Containerisation** : Docker & Docker Compose
*   **Broker** : Eclipse Mosquitto

## 📦 Installation et Lancement

### Prérequis
*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Démarrage
Pour lancer toute l'infrastructure en une seule commande :
```bash
docker compose up -d
```

### Visualiser les événements
Pour voir les messages passer en temps réel entre le publisher et le subscriber :
```bash
docker compose logs -f subscriber publisher
```

## 📂 Structure du projet
*   `publisher.py` : Script de génération d'événements.
*   `subscriber.py` : Script de réception et affichage.
*   `mosquitto.conf` : Configuration du broker (autorise les connexions anonymes).
*   `Dockerfile` : Image personnalisée pour les scripts Python avec installation automatique des dépendances.
*   `docker-compose.yaml` : Orchestration des services et du réseau.

## 🔧 Configuration
Le broker est configuré sur le port par défaut `1883`. Vous pouvez modifier les variables d'environnement dans le fichier `docker-compose.yaml` si nécessaire (notamment `MQTT_BROKER`).

---