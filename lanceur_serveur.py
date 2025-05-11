import os
import webbrowser
import time
import subprocess

print("=== Démarrage du script Python ===")

try:
    # Démarrer le serveur Django dans une console indépendante
    print("Démarrage du serveur Django...")
    subprocess.Popen(["python", "manage.py", "runserver"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    # Attendre avant d'ouvrir le navigateur
    print("Attente de 3 secondes pour laisser le serveur démarrer...")
    time.sleep(3)
    
    # Ouvrir le navigateur web
    print("Ouverture du navigateur à l'adresse : http://127.0.0.1:8000")
    webbrowser.open("http://127.0.0.1:8000")
    
    print("=== Script terminé avec succès ===")
except Exception as e:
    print(f"Erreur : {e}")
